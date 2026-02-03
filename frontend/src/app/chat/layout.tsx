import { ReactNode } from "react";
import { Sidebar } from "@/components/sidebar/Sidebar";
import { Header } from "@/components/header/Header";

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
        <div className="flex h-screen overflow-hidden">
            <Sidebar conversations={conversations} />
            <div className="flex-1 flex flex-col overflow-hidden">
                <Header />
                <main className="flex-1 overflow-hidden">{children}</main>
            </div>
        </div>
    );
}
