"use client";

import { useUser } from "@clerk/nextjs";
import { MessageSquarePlus, Menu, X } from "lucide-react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { cn } from "@/lib/utils";
import { useState } from "react";
import Image from "next/image";

interface Conversation {
    id: string;
    title: string;
    mode: string;
    updatedAt: string;
}

interface SidebarProps {
    conversations: Conversation[];
}

export function Sidebar({ conversations }: SidebarProps) {
    const pathname = usePathname();
    const [isCollapsed, setIsCollapsed] = useState(false);
    const { user } = useUser();

    return (
        <>
            {/* Mobile Overlay */}
            {!isCollapsed && (
                <div
                    className="md:hidden fixed inset-0 bg-black/50 backdrop-blur-sm z-40"
                    onClick={() => setIsCollapsed(true)}
                />
            )}

            {/* Mobile Toggle Button */}
            <button
                onClick={() => setIsCollapsed(!isCollapsed)}
                className="md:hidden fixed top-4 left-4 z-50 p-2 rounded-lg bg-white dark:bg-gray-900 shadow-lg border border-gray-200 dark:border-gray-700"
            >
                {isCollapsed ? <Menu size={20} /> : <X size={20} />}
            </button>

            {/* Sidebar */}
            <div className={cn(
                "w-72 h-screen bg-white dark:bg-gray-900 border-r border-gray-200/50 dark:border-gray-800/50 flex flex-col transition-transform duration-300 z-50",
                "md:relative md:translate-x-0",
                isCollapsed ? "-translate-x-full fixed" : "translate-x-0 fixed md:relative"
            )}>
                {/* Header with App Icon */}
                <div className="p-5 border-b border-gray-200/50 dark:border-gray-800/50">
                    <div className="flex items-center gap-3">
                        <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-purple-500 to-purple-600 flex items-center justify-center shadow-md">
                            <span className="text-white font-bold text-base">WO</span>
                        </div>
                        <h1 className="text-base font-semibold text-gray-900 dark:text-white">
                            Workflow Orchestrator
                        </h1>
                    </div>
                </div>

                {/* New Chat Button */}
                <div className="p-4">
                    <Link
                        href="/chat"
                        onClick={() => setIsCollapsed(true)}
                        className="w-full flex items-center gap-2 px-4 py-3 rounded-xl bg-gradient-to-r from-purple-500 to-purple-600 hover:from-purple-600 hover:to-purple-700 text-white font-medium transition-all hover:scale-[1.02] active:scale-[0.98] shadow-lg shadow-purple-500/30"
                    >
                        <MessageSquarePlus size={18} />
                        <span className="text-sm">New Conversation</span>
                    </Link>
                </div>

                {/* Conversations List */}
                <div className="flex-1 overflow-y-auto px-3">
                    <div className="space-y-1">
                        {conversations.map((conv) => {
                            const isActive = pathname.includes(conv.id);
                            return (
                                <Link
                                    key={conv.id}
                                    href={`/chat/${conv.id}`}
                                    onClick={() => setIsCollapsed(true)}
                                    className={cn(
                                        "block px-4 py-3 rounded-xl transition-all",
                                        isActive
                                            ? "bg-purple-50 dark:bg-purple-900/20 text-purple-700 dark:text-purple-300"
                                            : "hover:bg-gray-100 dark:hover:bg-gray-800 text-gray-700 dark:text-gray-300"
                                    )}
                                >
                                    <div className="flex items-start justify-between">
                                        <div className="flex-1 min-w-0">
                                            <p className="text-sm font-medium truncate">
                                                {conv.title || "Untitled Conversation"}
                                            </p>
                                            <p className="text-xs opacity-60 mt-1">
                                                {conv.mode === "workflow_planning" ? "📋 Workflow Planning" : "💬 General"}
                                            </p>
                                        </div>
                                    </div>
                                </Link>
                            );
                        })}
                    </div>
                </div>

                {/* User Profile with Clerk Image */}
                <div className="p-4 border-t border-gray-200/50 dark:border-gray-800/50">
                    <div className="flex items-center gap-3">
                        {user?.imageUrl ? (
                            <Image
                                src={user.imageUrl}
                                alt={user.fullName || "User"}
                                width={40}
                                height={40}
                                className="rounded-full ring-2 ring-gray-200 dark:ring-gray-700"
                            />
                        ) : (
                            <div className="w-10 h-10 rounded-full bg-gradient-to-br from-gray-700 to-gray-800 dark:from-gray-600 dark:to-gray-700 flex items-center justify-center ring-2 ring-gray-200 dark:ring-gray-700">
                                <span className="text-white font-medium text-sm">
                                    {user?.firstName?.[0] || "U"}
                                </span>
                            </div>
                        )}
                        <div className="flex-1 min-w-0">
                            <p className="text-sm font-medium text-gray-900 dark:text-white truncate">
                                {user?.fullName || "My Account"}
                            </p>
                            <p className="text-xs text-gray-500 dark:text-gray-400 truncate">
                                {user?.primaryEmailAddress?.emailAddress || ""}
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}
