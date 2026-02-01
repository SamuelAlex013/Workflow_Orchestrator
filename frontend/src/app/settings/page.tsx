"use client";

import { useUser } from "@clerk/nextjs";
import { useTheme } from "@/contexts/ThemeContext";
import { Moon, Sun, User, Mail } from "lucide-react";
import Link from "next/link";
import { cn } from "@/lib/utils";

export default function SettingsPage() {
    const { user } = useUser();
    const { theme, toggleTheme } = useTheme();

    return (
        <div className="min-h-screen bg-gray-50 dark:bg-gray-950">
            <div className="max-w-4xl mx-auto px-6 py-12">
                {/* Header */}
                <div className="mb-8">
                    <Link
                        href="/chat"
                        className="text-sm text-primary hover:underline mb-4 inline-block"
                    >
                        ← Back to Chat
                    </Link>
                    <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
                        Settings
                    </h1>
                    <p className="text-gray-600 dark:text-gray-400 mt-2">
                        Manage your account preferences and settings
                    </p>
                </div>

                {/* Settings Sections */}
                <div className="space-y-6">
                    {/* Account Information */}
                    <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
                        <h2 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">
                            Account Information
                        </h2>
                        <div className="space-y-4">
                            <div className="flex items-center gap-3">
                                <div className="w-10 h-10 rounded-full bg-gray-100 dark:bg-gray-800 flex items-center justify-center">
                                    <User size={20} className="text-gray-600 dark:text-gray-400" />
                                </div>
                                <div>
                                    <p className="text-sm text-gray-500 dark:text-gray-400">Name</p>
                                    <p className="font-medium text-gray-900 dark:text-white">
                                        {user?.fullName || "Not set"}
                                    </p>
                                </div>
                            </div>
                            <div className="flex items-center gap-3">
                                <div className="w-10 h-10 rounded-full bg-gray-100 dark:bg-gray-800 flex items-center justify-center">
                                    <Mail size={20} className="text-gray-600 dark:text-gray-400" />
                                </div>
                                <div>
                                    <p className="text-sm text-gray-500 dark:text-gray-400">Email</p>
                                    <p className="font-medium text-gray-900 dark:text-white">
                                        {user?.primaryEmailAddress?.emailAddress || "Not set"}
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Appearance */}
                    <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
                        <h2 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">
                            Appearance
                        </h2>
                        <div className="flex items-center justify-between">
                            <div>
                                <p className="font-medium text-gray-900 dark:text-white">Theme</p>
                                <p className="text-sm text-gray-500 dark:text-gray-400">
                                    Choose your preferred color scheme
                                </p>
                            </div>
                            <button
                                onClick={toggleTheme}
                                className={cn(
                                    "relative w-16 h-8 rounded-full transition-colors",
                                    theme === "dark" ? "bg-primary" : "bg-gray-300"
                                )}
                            >
                                <div
                                    className={cn(
                                        "absolute top-1 left-1 w-6 h-6 bg-white rounded-full transition-transform flex items-center justify-center",
                                        theme === "dark" && "translate-x-8"
                                    )}
                                >
                                    {theme === "light" ? (
                                        <Sun size={14} className="text-gray-600" />
                                    ) : (
                                        <Moon size={14} className="text-primary" />
                                    )}
                                </div>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
