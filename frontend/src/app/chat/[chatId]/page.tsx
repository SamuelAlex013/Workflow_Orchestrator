import { ChatInterface } from "@/components/chat/ChatInterface";

interface ChatPageProps {
    params: Promise<{
        chatId: string;
    }>;
}

export default async function ChatPage({ params }: ChatPageProps) {
    const { chatId } = await params;

    // Mock messages - in production, fetch from API based on chatId
    const mockMessages = [
        {
            id: "1",
            sender: "user" as const,
            content: "How do I create a webhook automation?",
            createdAt: new Date().toISOString(),
        },
        {
            id: "2",
            sender: "assistant" as const,
            content:
                "I'll help you create a webhook automation. First, you'll need to set up a Webhook node as a trigger...",
            createdAt: new Date().toISOString(),
        },
    ];

    return (
        <ChatInterface
            conversationId={chatId}
            initialMessages={mockMessages}
        />
    );
}
