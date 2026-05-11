import { ChatInterface } from "@/components/chat/ChatInterface";
import { auth } from "@clerk/nextjs/server";
import { connectToDatabase } from "@/lib/mongodb";
import { Session } from "@/lib/models/Session";
import { Message } from "@/lib/models/Message";
import mongoose from "mongoose";

interface ChatPageProps {
    params: Promise<{
        chatId: string;
    }>;
}

export default async function ChatPage({ params }: ChatPageProps) {
    const { chatId } = await params;

    let initialMessages: Array<{
        id: string;
        sender: "user" | "assistant";
        content: string;
        createdAt: string;
        sources?: string[];
        confidence?: string;
        model?: string;
    }> = [];

    try {
        const { userId } = await auth();

        if (userId && mongoose.Types.ObjectId.isValid(chatId)) {
            await connectToDatabase();

            const session = await Session.findOne({ _id: chatId, userId })
                .select("_id")
                .lean();

            if (session) {
                const messages = await Message.find({ sessionId: session._id })
                    .sort({ createdAt: 1 })
                    .lean();

                initialMessages = messages.map((m) => ({
                    id: (m._id as object).toString(),
                    sender: m.sender,
                    content: m.content,
                    createdAt: new Date(m.createdAt as Date).toISOString(),
                    sources: m.sources ?? [],
                    confidence: m.confidence ?? undefined,
                    model: m.model ?? undefined,
                }));
            }
        }
    } catch (err) {
        console.error("[ChatPage] Failed to load session messages:", err);
        initialMessages = [];
    }

    return (
        <ChatInterface
            conversationId={chatId}
            initialMessages={initialMessages}
        />
    );
}
