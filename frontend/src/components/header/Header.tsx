"use client";

import { Moon, Sun } from "lucide-react";
import { useTheme } from "@/contexts/ThemeContext";
import { cn } from "@/lib/utils";

type Mode = "general" | "workflow_planning";

interface HeaderProps {
    mode: Mode;
    onModeChange: (mode: Mode) => void;
}

export function Header({ mode, onModeChange }: HeaderProps) {
    const { theme, toggleTheme } = useTheme();

    return (
        <div className="h-16 border-b border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950 flex items-center justify-between px-6">
            {/* Mode Switcher */}
            <div className="flex gap-2 bg-gray-100 dark:bg-gray-900 p-1 rounded-lg">
                <button
                    onClick={() => onModeChange("general")}
                    className={cn(
                        "px-4 py-2 rounded-md text-sm font-medium transition-all",
                        mode === "general"
                            ? "bg-white dark:bg-gray-800 text-gray-900 dark:text-white shadow-sm"
                            : "text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white"
                    )}
                >
                    General Conversation
                </button>
                <button
                    onClick={() => onModeChange("workflow_planning")}
                    className={cn(
                        "px-4 py-2 rounded-md text-sm font-medium transition-all",
                        mode === "workflow_planning"
                            ? "bg-white dark:bg-gray-800 text-gray-900 dark:text-white shadow-sm"
                            : "text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white"
                    )}
                >
                    Workflow Planning
                </button>
            </div>

            {/* Theme Toggle */}
            <button
                onClick={toggleTheme}
                className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-900 transition-colors"
                aria-label="Toggle theme"
            >
                {theme === "light" ? (
                    <Moon size={20} className="text-gray-600 dark:text-gray-400" />
                ) : (
                    <Sun size={20} className="text-gray-400" />
                )}
            </button>
        </div>
    );
}
