"use client";

import { useUser } from "@clerk/nextjs";
import { MessageSquarePlus, Menu, ChevronLeft, Moon, Sun } from "lucide-react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { cn } from "@/lib/utils";
import { useState, useEffect } from "react";
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

export function Sidebar({ conversations, isCollapsed: controlledCollapsed, onToggle }: SidebarProps) {
    const pathname = usePathname();
    const [internalCollapsed, setInternalCollapsed] = useState(false);
    const { user } = useUser();
    const { theme, toggleTheme } = useTheme();

    // Use controlled state if provided, otherwise use internal state
    const isCollapsed = controlledCollapsed ?? internalCollapsed;
    const handleToggle = onToggle ?? (() => setInternalCollapsed(!internalCollapsed));

    // Handle mobile state - always start collapsed on mobile
    const [isMobile, setIsMobile] = useState(false);
    
    useEffect(() => {
        const checkMobile = () => setIsMobile(window.innerWidth < 768);
        checkMobile();
        window.addEventListener('resize', checkMobile);
        return () => window.removeEventListener('resize', checkMobile);
    }, []);

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
                // Width transitions
                isCollapsed ? "w-16" : "w-72",
                // Mobile positioning
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
                            <ChevronLeft 
                                size={18} 
                                className="text-gray-500 dark:text-gray-400 rotate-180" 
                            />
                        </button>
                    </div>
                )}

                {/* Header with App Icon & Toggle - only when expanded */}
                {(!isCollapsed || isMobile) && (
                    <div className="p-3 border-b border-gray-200/50 dark:border-gray-800/50">
                        <div className="flex items-center justify-between">
                            <div className="flex items-center gap-3">
                                <div className="w-10 h-10 rounded-xl bg-indigo-500 dark:bg-sky-500 flex items-center justify-center shadow-md flex-shrink-0">
                                    <span className="text-white font-bold text-base">WO</span>
                                </div>
                                <h1 className="text-base font-semibold text-gray-900 dark:text-white whitespace-nowrap">
                                    Workflow Orchestrator
                                </h1>
                            </div>
                            
                            {/* Desktop Collapse Button */}
                            {!isMobile && (
                                <button
                                    onClick={handleToggle}
                                    className="p-1.5 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-all"
                                    aria-label="Collapse sidebar"
                                >
                                    <ChevronLeft 
                                        size={16} 
                                        className="text-gray-500 dark:text-gray-400" 
                                    />
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
                    <div className="space-y-1">
                        {conversations.map((conv) => {
                            const isActive = pathname.includes(conv.id);
                            return (
                                <Link
                                    key={conv.id}
                                    href={`/chat/${conv.id}`}
                                    onClick={() => isMobile && handleToggle()}
                                    className={cn(
                                        "block rounded-xl transition-all",
                                        isCollapsed && !isMobile ? "p-3 flex justify-center" : "px-4 py-3",
                                        isActive
                                            ? "bg-indigo-50 dark:bg-sky-900/20 text-indigo-700 dark:text-sky-300 border-l-2 border-indigo-500 dark:border-sky-500"
                                            : "hover:bg-slate-100 dark:hover:bg-slate-800/50 text-slate-700 dark:text-slate-300"
                                    )}
                                    title={conv.title || "Untitled Conversation"}
                                >
                                    {isCollapsed && !isMobile ? (
                                        <span className="text-lg">
                                            {conv.mode === "workflow_planning" ? "📋" : "💬"}
                                        </span>
                                    ) : (
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
                                    )}
                                </Link>
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

            {/* Mobile Toggle Button (Fixed position when sidebar is collapsed) */}
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
