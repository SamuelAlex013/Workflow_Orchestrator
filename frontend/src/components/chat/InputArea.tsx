"use client";

import { useState, FormEvent, KeyboardEvent } from "react";
import { Send } from "lucide-react";
import { cn } from "@/lib/utils";

interface InputAreaProps {
    onSendMessage: (content: string) => void;
    disabled?: boolean;
}

export function InputArea({ onSendMessage, disabled = false }: InputAreaProps) {
    const [input, setInput] = useState("");

    const handleSubmit = (e: FormEvent) => {
        e.preventDefault();
        if (input.trim() && !disabled) {
            onSendMessage(input.trim());
            setInput("");
        }
    };

    const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSubmit(e);
        }
    };

    return (
        <div className="border-t border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950 p-4">
            <form onSubmit={handleSubmit} className="max-w-4xl mx-auto">
                <div className="relative flex items-end gap-2">
                    <div className="flex-1 relative">
                        <textarea
                            value={input}
                            onChange={(e) => setInput(e.target.value)}
                            onKeyDown={handleKeyDown}
                            placeholder="Type your message..."
                            disabled={disabled}
                            rows={1}
                            className={cn(
                                "w-full resize-none rounded-full px-6 py-4 pr-12",
                                "bg-gray-100 dark:bg-gray-900",
                                "border-2 border-transparent",
                                "focus:border-primary focus:outline-none",
                                "text-gray-900 dark:text-white placeholder:text-gray-500",
                                "transition-all duration-200",
                                "disabled:opacity-50 disabled:cursor-not-allowed",
                                "hover:bg-gray-200 dark:hover:bg-gray-800 focus:bg-white dark:focus:bg-gray-900",
                                "max-h-32 overflow-y-auto"
                            )}
                            style={{
                                height: "auto",
                                minHeight: "56px",
                            }}
                            onInput={(e) => {
                                const target = e.target as HTMLTextAreaElement;
                                target.style.height = "auto";
                                target.style.height = target.scrollHeight + "px";
                            }}
                        />
                    </div>

                    <button
                        type="submit"
                        disabled={!input.trim() || disabled}
                        className={cn(
                            "flex-shrink-0 w-14 h-14 rounded-full",
                            "bg-primary hover:bg-primary-hover",
                            "disabled:bg-gray-300 dark:disabled:bg-gray-700",
                            "disabled:cursor-not-allowed",
                            "flex items-center justify-center",
                            "transition-all duration-200",
                            "hover:scale-105 active:scale-95",
                            "shadow-lg disabled:shadow-none"
                        )}
                    >
                        <Send size={20} className="text-white" />
                    </button>
                </div>
            </form>
        </div>
    );
}
