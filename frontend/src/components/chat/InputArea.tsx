"use client";

import { useState, FormEvent, KeyboardEvent, useRef, useEffect } from "react";
import { Send, ChevronDown, Lock } from "lucide-react";
import { cn } from "@/lib/utils";

type Mode = "general" | "workflow_planning" | "advanced_automation";

const MODE_OPTIONS = [
    {
        id: "general",
        label: "General Automation",
        icon: "💬",
        description: "General information, FAQs, and explanations about n8n automation"
    },
    {
        id: "workflow_planning",
        label: "Workflow Planning",
        icon: "📋",
        description: "Planning, structuring, and discussing n8n workflows conceptually"
    },
    {
        id: "advanced_automation",
        label: "Advanced Automation",
        icon: "🔒",
        locked: true,
        description: "Workflow visualization and creation - Authorized users only"
    },
];

interface InputAreaProps {
    onSendMessage: (content: string, mode?: Mode) => void;
    disabled?: boolean;
}

export function InputArea({ onSendMessage, disabled = false }: InputAreaProps) {
    const [input, setInput] = useState("");
    const [showModeDropdown, setShowModeDropdown] = useState(false);
    const [selectedMode, setSelectedMode] = useState<Mode>("general");
    const [cursorPosition, setCursorPosition] = useState(0);
    const textareaRef = useRef<HTMLTextAreaElement>(null);
    const modeDropdownRef = useRef<HTMLDivElement>(null);
    const modeSelectorRef = useRef<HTMLDivElement>(null);

    // Close dropdowns when clicking outside
    useEffect(() => {
        const handleClickOutside = (event: MouseEvent) => {
            if (modeDropdownRef.current && !modeDropdownRef.current.contains(event.target as Node)) {
                setShowModeDropdown(false);
            }
            if (modeSelectorRef.current && !modeSelectorRef.current.contains(event.target as Node)) {
                setShowModeDropdown(false);
            }
        };

        document.addEventListener("mousedown", handleClickOutside);
        return () => document.removeEventListener("mousedown", handleClickOutside);
    }, []);

    // Detect @ symbol for mode switcher
    useEffect(() => {
        const lastChar = input.charAt(cursorPosition - 1);
        if (lastChar === "@" && cursorPosition === input.length) {
            setShowModeDropdown(true);
        }
    }, [input, cursorPosition]);

    const handleSubmit = (e: FormEvent) => {
        e.preventDefault();
        if (input.trim() && !disabled) {
            onSendMessage(input.trim(), selectedMode);
            setInput("");
        }
    };

    const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSubmit(e);
        }
    };

    const handleModeSelect = (mode: string, locked?: boolean) => {
        if (locked) {
            alert("🔒 Advanced Automation is a premium feature available only to authorized users.");
            setShowModeDropdown(false);
            return;
        }

        setSelectedMode(mode as Mode);
        // Remove @ from input if present
        if (input.endsWith("@")) {
            setInput(input.slice(0, -1));
        }
        setShowModeDropdown(false);
    };

    const selectedModeOption = MODE_OPTIONS.find(m => m.id === selectedMode) || MODE_OPTIONS[0];

    return (
        <div className="border-t border-slate-200 dark:border-slate-700/50 bg-white dark:bg-[#1E293B] p-6">
            <form onSubmit={handleSubmit} className="max-w-4xl mx-auto">
                <div className="flex flex-col gap-3">
                    {/* Mode Selector (replaces Model Selector) */}
                    <div className="relative" ref={modeSelectorRef}>
                        <button
                            type="button"
                            onClick={() => setShowModeDropdown(!showModeDropdown)}
                            className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors text-sm font-medium text-gray-700 dark:text-gray-300"
                        >
                            <span>{selectedModeOption.icon}</span>
                            {selectedModeOption.label}
                            <ChevronDown size={14} />
                        </button>

                        {showModeDropdown && (
                            <div className="absolute bottom-full left-0 mb-2 w-80 bg-white dark:bg-gray-900 rounded-xl shadow-2xl border border-gray-200 dark:border-gray-700 overflow-hidden z-50">
                                <div className="px-3 py-2 bg-gray-50 dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
                                    <p className="text-xs font-medium text-gray-500 dark:text-gray-400">
                                        Select Mode
                                    </p>
                                </div>
                                {MODE_OPTIONS.map((mode) => (
                                    <button
                                        key={mode.id}
                                        type="button"
                                        onClick={() => handleModeSelect(mode.id, mode.locked)}
                                        className={cn(
                                            "w-full text-left px-4 py-3 hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors border-b border-gray-100 dark:border-gray-800 last:border-b-0",
                                            mode.locked && "bg-gray-50/50 dark:bg-gray-800/50",
                                            selectedMode === mode.id && "bg-indigo-50 dark:bg-sky-950/20 border-l-2 border-indigo-500 dark:border-sky-500"
                                        )}
                                    >
                                        <div className="flex items-start justify-between gap-3">
                                            <div className="flex items-start gap-2 flex-1">
                                                <span className="text-lg mt-0.5">{mode.icon}</span>
                                                <div className="flex-1">
                                                    <div className="flex items-center gap-2">
                                                        <span className="font-medium text-sm text-gray-900 dark:text-white">
                                                            {mode.label}
                                                        </span>
                                                        {mode.locked && (
                                                            <Lock size={12} className="text-gray-400" />
                                                        )}
                                                    </div>
                                                    <p className="text-xs text-gray-500 dark:text-gray-400 mt-0.5">
                                                        {mode.description}
                                                    </p>
                                                </div>
                                            </div>
                                            {mode.locked && (
                                                <span className="px-2 py-0.5 text-xs font-medium bg-gray-200 dark:bg-gray-700 text-gray-600 dark:text-gray-300 rounded">
                                                    Locked
                                                </span>
                                            )}
                                        </div>
                                    </button>
                                ))}
                            </div>
                        )}
                    </div>

                    {/* Input Area with @mention */}
                    <div className="relative flex items-end gap-3">
                        <div className="flex-1 relative" ref={modeDropdownRef}>
                            <textarea
                                ref={textareaRef}
                                value={input}
                                onChange={(e) => {
                                    setInput(e.target.value);
                                    setCursorPosition(e.target.selectionStart);
                                }}
                                onKeyDown={handleKeyDown}
                                placeholder="Type @ to switch modes or start typing..."
                                disabled={disabled}
                                rows={1}
                                className={cn(
                                    "w-full resize-none rounded-3xl px-5 py-4 pr-12",
                                    "bg-white dark:bg-[#1E293B]",
                                    "border border-slate-200 dark:border-slate-600",
                                    "focus:border-indigo-400 dark:focus:border-sky-400 focus:outline-none focus:ring-2 focus:ring-indigo-100 dark:focus:ring-sky-900/30",
                                    "text-slate-900 dark:text-slate-100 placeholder:text-slate-400 dark:placeholder:text-slate-500",
                                    "transition-all duration-200",
                                    "disabled:opacity-50 disabled:cursor-not-allowed",
                                    "max-h-40 overflow-y-auto text-[15px] leading-relaxed"
                                )}
                                style={{
                                    height: "auto",
                                    minHeight: "60px",
                                }}
                                onInput={(e) => {
                                    const target = e.target as HTMLTextAreaElement;
                                    target.style.height = "auto";
                                    target.style.height = Math.min(target.scrollHeight, 160) + "px";
                                }}
                            />
                        </div>

                        <button
                            type="submit"
                            disabled={!input.trim() || disabled}
                            className={cn(
                                "flex-shrink-0 w-12 h-12 rounded-2xl",
                                "bg-indigo-500 hover:bg-indigo-600 dark:bg-sky-500 dark:hover:bg-sky-400",
                                "disabled:bg-slate-300 dark:disabled:bg-slate-700",
                                "disabled:cursor-not-allowed",
                                "flex items-center justify-center",
                                "transition-all duration-200",
                                "hover:scale-105 active:scale-95",
                                "shadow-lg shadow-indigo-500/25 dark:shadow-sky-500/25 disabled:shadow-none"
                            )}
                        >
                            <Send size={18} className="text-white" />
                        </button>
                    </div>
                </div>
            </form>
        </div>
    );
}
