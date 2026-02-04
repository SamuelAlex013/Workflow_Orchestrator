"use client";

import { Moon, Sun } from "lucide-react";
import { useTheme } from "@/contexts/ThemeContext";

export function Header() {
    const { theme, toggleTheme } = useTheme();

    return (
        <div className="h-14 border-b border-slate-200 dark:border-slate-700/50 bg-white dark:bg-[#1E293B] flex items-center justify-between px-6">
            {/* Logo */}
            <div className="flex items-center gap-3">
                <h1 className="text-lg font-semibold text-gray-900 dark:text-white">
                    Workflow Orchestrator
                </h1>
            </div>

            {/* Right Side: Only Theme Toggle */}
            <div className="flex items-center">
                <button
                    onClick={toggleTheme}
                    className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-all duration-200"
                    aria-label="Toggle theme"
                >
                    {theme === "light" ? (
                        <Moon size={18} className="text-gray-600 dark:text-gray-400" />
                    ) : (
                        <Sun size={18} className="text-gray-400" />
                    )}
                </button>
            </div>
        </div>
    );
}
