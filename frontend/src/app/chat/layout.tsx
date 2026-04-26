import { ReactNode } from "react";
import { auth } from "@clerk/nextjs/server";
import { Sidebar } from "@/components/sidebar/Sidebar";
import { connectToDatabase } from "@/lib/mongodb";
import { Session } from "@/lib/models/Session";

interface ConversationShape {
    id: string;
    title: string;
    mode: string;
    updatedAt: string;
}

async function getUserSessions(): Promise<ConversationShape[]> {
    try {
        const { userId } = await auth();
        if (!userId) return [];

        await connectToDatabase();

        const sessions = await Session.find({ userId })
            .sort({ updatedAt: -1 })
            .select("_id title mode updatedAt")
            .lean();

        return sessions.map((s) => ({
            id: (s._id as object).toString(),
            title: s.title || "Untitled Conversation",
            mode: s.mode,
            updatedAt: new Date(s.updatedAt as Date).toISOString(),
        }));
    } catch (err) {
        // Graceful degradation — sidebar shows empty if DB is unreachable
        console.error("[ChatLayout] Failed to load sessions:", err);
        return [];
    }
}

export default async function ChatLayout({ children }: { children: ReactNode }) {
    const conversations = await getUserSessions();

    return (
        <div className="flex h-screen overflow-hidden bg-slate-50 dark:bg-[#0F172A]">
            <Sidebar conversations={conversations} />
            <main className="flex-1 overflow-hidden">{children}</main>
        </div>
    );
}
