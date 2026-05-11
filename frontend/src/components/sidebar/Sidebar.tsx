"use client";

import { useUser } from "@clerk/nextjs";
import { MessageSquarePlus, Menu, ChevronLeft, Moon, Sun, Trash2, Bot, Zap } from "lucide-react";
import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { cn } from "@/lib/utils";
import { useState, useEffect, useCallback } from "react";
import Image from "next/image";
import { useTheme } from "@/contexts/ThemeContext";

interface Conversation {
    id: string;
    title: string;
    mode: string;
    updatedAt: string;
}

interface SidebarProps {
    conversations: Conversation[];
    isCollapsed?: boolean;
    onToggle?: () => void;
}

export function Sidebar({ conversations: initialConversations, isCollapsed: controlledCollapsed, onToggle }: SidebarProps) {
    const pathname = usePathname();
    const router = useRouter();
    const [internalCollapsed, setInternalCollapsed] = useState(false);
    const { user } = useUser();
    const { theme, toggleTheme } = useTheme();

    // Local copy so we can optimistically remove deleted sessions
    const [conversations, setConversations] = useState<Conversation[]>(initialConversations);
    const [deletingId, setDeletingId] = useState<string | null>(null);
    const [hoveredId, setHoveredId] = useState<string | null>(null);

    const refreshConversations = useCallback(async () => {
        try {
            const res = await fetch("/api/sessions", { cache: "no-store" });
            if (!res.ok) return;

            const data = await res.json();
            if (!Array.isArray(data.sessions)) return;

            setConversations(data.sessions);
        } catch {
            // Ignore transient refresh failures; sidebar keeps existing data
        }
    }, []);

    // Sync if parent re-renders with new data
    useEffect(() => {
        setConversations(initialConversations);
    }, [initialConversations]);

    // Listen for client-side session updates (e.g., first message creates a new session)
    useEffect(() => {
        const onRefresh = () => {
            void refreshConversations();
        };

        window.addEventListener("sessions:refresh", onRefresh);
        return () => window.removeEventListener("sessions:refresh", onRefresh);
    }, [refreshConversations]);

    const isCollapsed = controlledCollapsed ?? internalCollapsed;
    const handleToggle = onToggle ?? (() => setInternalCollapsed(!internalCollapsed));

    const [isMobile, setIsMobile] = useState(false);
    useEffect(() => {
        const checkMobile = () => setIsMobile(window.innerWidth < 768);
        checkMobile();
        window.addEventListener("resize", checkMobile);
        return () => window.removeEventListener("resize", checkMobile);
    }, []);

    // ─── Delete handler ───────────────────────────────────────────────────────
    const handleDelete = async (e: React.MouseEvent, convId: string) => {
        e.preventDefault();
        e.stopPropagation();

        if (!window.confirm("Delete this conversation? This cannot be undone.")) return;

        setDeletingId(convId);

        try {
            const res = await fetch(`/api/sessions/${convId}`, { method: "DELETE" });
            if (res.ok) {
                // Optimistic UI: remove immediately
                setConversations((prev) => prev.filter((c) => c.id !== convId));

                // If we deleted the currently-open chat, navigate to /chat
                if (pathname.includes(convId)) {
                    router.push("/chat");
                }
            } else {
                alert("Failed to delete the conversation. Please try again.");
            }
        } catch {
            alert("Network error while deleting. Please try again.");
        } finally {
            setDeletingId(null);
        }
    };

    return (
        <>
            {/* Mobile Overlay */}
            {isMobile && !isCollapsed && (
                <div
                    className="fixed inset-0 bg-black/50 backdrop-blur-sm z-40"
                    onClick={handleToggle}
                />
            )}

            {/* Sidebar */}
            <div className={cn(
                "h-screen bg-white dark:bg-[#1E293B] border-r border-slate-200 dark:border-slate-700/50 flex flex-col transition-all duration-300 z-50",
                isCollapsed ? "w-16" : "w-72",
                isMobile && "fixed",
                isMobile && isCollapsed && "-translate-x-full",
                !isMobile && "relative"
            )}>
                {/* Collapsed: Expand button at top */}
                {isCollapsed && !isMobile && (
                    <div className="p-3 flex justify-center border-b border-gray-200/50 dark:border-gray-800/50">
                        <button
                            onClick={handleToggle}
                            className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-all"
                            aria-label="Expand sidebar"
                            title="Expand sidebar"
                        >
                            <ChevronLeft size={18} className="text-gray-500 dark:text-gray-400 rotate-180" />
                        </button>
                    </div>
                )}

                {/* Header */}
                {(!isCollapsed || isMobile) && (
                    <div className="p-3 border-b border-gray-200/50 dark:border-gray-800/50">
                        <div className="flex items-center justify-between">
                            <div className="flex items-center gap-3">
                                <div className="w-10 h-10 rounded-xl bg-indigo-500 dark:bg-sky-500 flex items-center justify-center shadow-md flex-shrink-0">
                                    <Bot size={18} className="text-white" />
                                </div>
                                <h1 className="text-base font-semibold text-gray-900 dark:text-white whitespace-nowrap">
                                    Workflow Orchestrator
                                </h1>
                            </div>
                            {!isMobile && (
                                <button
                                    onClick={handleToggle}
                                    className="p-1.5 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-all"
                                    aria-label="Collapse sidebar"
                                >
                                    <ChevronLeft size={16} className="text-gray-500 dark:text-gray-400" />
                                </button>
                            )}
                        </div>
                    </div>
                )}

                {/* New Chat Button */}
                <div className={cn("p-3", isCollapsed && !isMobile && "px-2")}>
                    <Link
                        href="/chat"
                        onClick={() => isMobile && handleToggle()}
                        className={cn(
                            "flex items-center gap-2 rounded-xl bg-indigo-500 hover:bg-indigo-600 dark:bg-sky-500 dark:hover:bg-sky-400 text-white font-medium transition-all hover:scale-[1.02] active:scale-[0.98] shadow-lg shadow-indigo-500/25 dark:shadow-sky-500/25",
                            isCollapsed && !isMobile ? "justify-center p-3" : "px-4 py-3 w-full"
                        )}
                        title="New Conversation"
                    >
                        <MessageSquarePlus size={18} />
                        {!isCollapsed && <span className="text-sm">New Conversation</span>}
                    </Link>
                </div>

                {/* Conversations List */}
                <div className="flex-1 overflow-y-auto px-2">
                    {conversations.length === 0 && !isCollapsed && (
                        <p className="text-xs text-slate-400 dark:text-slate-500 text-center mt-4 px-2">
                            No conversations yet. Start a new chat!
                        </p>
                    )}
                    <div className="space-y-1">
                        {conversations.map((conv) => {
                            const isActive = pathname.includes(conv.id);
                            const isDeleting = deletingId === conv.id;

                            return (
                                <div
                                    key={conv.id}
                                    className="relative group"
                                    onMouseEnter={() => setHoveredId(conv.id)}
                                    onMouseLeave={() => setHoveredId(null)}
                                >
                                    <Link
                                        href={`/chat/${conv.id}`}
                                        onClick={() => isMobile && handleToggle()}
                                        className={cn(
                                            "block rounded-xl transition-all",
                                            isCollapsed && !isMobile ? "p-3 flex justify-center" : "px-4 py-3 pr-10",
                                            isActive
                                                ? "bg-indigo-50 dark:bg-sky-900/20 text-indigo-700 dark:text-sky-300 border-l-2 border-indigo-500 dark:border-sky-500"
                                                : "hover:bg-slate-100 dark:hover:bg-slate-800/50 text-slate-700 dark:text-slate-300",
                                            isDeleting && "opacity-40 pointer-events-none"
                                        )}
                                        title={conv.title || "Untitled Conversation"}
                                    >
                                        {isCollapsed && !isMobile ? (
                                            <span className="inline-flex items-center justify-center">
                                                {conv.mode === "workflow_planning" ? (
                                                    <Zap size={16} className="text-indigo-600 dark:text-sky-400" />
                                                ) : (
                                                    <Bot size={16} className="text-indigo-600 dark:text-sky-400" />
                                                )}
                                            </span>
                                        ) : (
                                            <div className="flex items-start justify-between">
                                                <div className="flex-1 min-w-0">
                                                    <p className="text-sm font-medium truncate">
                                                        {conv.title || "Untitled Conversation"}
                                                    </p>
                                                    <p className="text-xs opacity-60 mt-1">
                                                        {conv.mode === "workflow_planning" ? "Zapier" : "n8n"}
                                                    </p>
                                                </div>
                                            </div>
                                        )}
                                    </Link>

                                    {/* Delete button — only visible on hover, only when expanded */}
                                    {!isCollapsed && !isMobile && hoveredId === conv.id && (
                                        <button
                                            onClick={(e) => handleDelete(e, conv.id)}
                                            disabled={isDeleting}
                                            className={cn(
                                                "absolute right-2 top-1/2 -translate-y-1/2",
                                                "p-1.5 rounded-lg",
                                                "text-slate-400 hover:text-red-500 dark:text-slate-500 dark:hover:text-red-400",
                                                "hover:bg-red-50 dark:hover:bg-red-900/20",
                                                "transition-all duration-150",
                                                isDeleting && "opacity-50 cursor-not-allowed"
                                            )}
                                            title="Delete conversation"
                                            aria-label="Delete conversation"
                                        >
                                            {isDeleting ? (
                                                <div className="w-3.5 h-3.5 border border-current border-t-transparent rounded-full animate-spin" />
                                            ) : (
                                                <Trash2 size={14} />
                                            )}
                                        </button>
                                    )}
                                </div>
                            );
                        })}
                    </div>
                </div>

                {/* Bottom Section: User Profile + Theme Toggle */}
                <div className={cn(
                    "p-3 border-t border-gray-200/50 dark:border-gray-800/50",
                    isCollapsed && !isMobile && "px-2"
                )}>
                    <div className={cn(
                        "flex",
                        isCollapsed && !isMobile ? "flex-col items-center gap-3" : "items-center justify-between gap-3"
                    )}>
                        {/* User Profile */}
                        <div className={cn(
                            "flex items-center",
                            isCollapsed && !isMobile ? "justify-center" : "gap-3 flex-1 min-w-0"
                        )}>
                            {user?.imageUrl ? (
                                <Image
                                    src={user.imageUrl}
                                    alt={user.fullName || "User"}
                                    width={36}
                                    height={36}
                                    className="rounded-full ring-2 ring-gray-200 dark:ring-gray-700 flex-shrink-0"
                                />
                            ) : (
                                <div className="w-9 h-9 rounded-full bg-gradient-to-br from-gray-700 to-gray-800 dark:from-gray-600 dark:to-gray-700 flex items-center justify-center ring-2 ring-gray-200 dark:ring-gray-700 flex-shrink-0">
                                    <span className="text-white font-medium text-sm">
                                        {user?.firstName?.[0] || "U"}
                                    </span>
                                </div>
                            )}
                            {!isCollapsed && (
                                <div className="min-w-0">
                                    <p className="text-sm font-medium text-gray-900 dark:text-white truncate">
                                        {user?.fullName || "My Account"}
                                    </p>
                                    <p className="text-xs text-gray-500 dark:text-gray-400 truncate">
                                        {user?.primaryEmailAddress?.emailAddress || ""}
                                    </p>
                                </div>
                            )}
                        </div>

                        {/* Theme Toggle */}
                        <button
                            onClick={toggleTheme}
                            className={cn(
                                "rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-all duration-200 flex-shrink-0",
                                isCollapsed && !isMobile ? "p-2" : "p-2"
                            )}
                            aria-label="Toggle theme"
                            title={theme === "light" ? "Switch to dark mode" : "Switch to light mode"}
                        >
                            {theme === "light" ? (
                                <Moon size={18} className="text-gray-600 dark:text-gray-400" />
                            ) : (
                                <Sun size={18} className="text-gray-400" />
                            )}
                        </button>
                    </div>
                </div>
            </div>

            {/* Mobile Toggle Button */}
            {isMobile && isCollapsed && (
                <button
                    onClick={handleToggle}
                    className="fixed top-4 left-4 z-50 p-2 rounded-lg bg-white dark:bg-gray-900 shadow-lg border border-gray-200 dark:border-gray-700"
                    aria-label="Open sidebar"
                >
                    <Menu size={20} className="text-gray-700 dark:text-gray-300" />
                </button>
            )}
        </>
    );
}
