import { ReactNode } from "react";
import { Sidebar } from "@/components/sidebar/Sidebar";

export default function ChatLayout({ children }: { children: ReactNode }) {
    // Mock conversations - in production, fetch from API
    const conversations = [
        {
            id: "1",
            title: "Getting started with n8n",
            mode: "general",
            updatedAt: new Date().toISOString(),
        },
        {
            id: "2",
            title: "Webhook automation workflow",
            mode: "workflow_planning",
            updatedAt: new Date().toISOString(),
        },
    ];

    return (
        <div className="flex h-screen overflow-hidden bg-slate-50 dark:bg-[#0F172A]">
            <Sidebar conversations={conversations} />
            <main className="flex-1 overflow-hidden">{children}</main>
        </div>
    );
}
