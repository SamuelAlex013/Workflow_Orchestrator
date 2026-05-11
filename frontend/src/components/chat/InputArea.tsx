"use client";

import { useState, FormEvent, KeyboardEvent, useRef, useEffect } from "react";
import { Send, ChevronDown, Zap, Network, Wrench } from "lucide-react";
import { cn } from "@/lib/utils";

type Mode = "general" | "workflow_planning" | "advanced_automation";

const MODE_OPTIONS = [
    {
        id: "general",
        label: "n8n",
        shortLabel: "n8n",
        icon: Network,
    },
    {
        id: "workflow_planning",
        label: "Zapier",
        shortLabel: "Zapier",
        icon: Zap,
    },
    {
        id: "advanced_automation",
        label: "Make",
        shortLabel: "Make",
        icon: Wrench,
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

    // Close dropdowns when clicking outside
    useEffect(() => {
        const handleClickOutside = (event: MouseEvent) => {
            if (modeDropdownRef.current && !modeDropdownRef.current.contains(event.target as Node)) {
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

    const handleModeSelect = (mode: string) => {
        setSelectedMode(mode as Mode);
        // Remove @ from input if present
        if (input.endsWith("@")) {
            setInput(input.slice(0, -1));
        }
        setShowModeDropdown(false);
    };

    const selectedModeOption = MODE_OPTIONS.find(m => m.id === selectedMode) || MODE_OPTIONS[0];
    const SelectedModeIcon = selectedModeOption.icon;

    return (
        <div className="bg-transparent px-4 py-4 md:px-6 w-full">
            <form onSubmit={handleSubmit} className="w-full">
                {/* Unified Input Bar: Mode Selector + Input + Send Button */}
                <div className="relative flex items-stretch gap-2 w-full" ref={modeDropdownRef}>
                    {/* Mode Selector (Left of Input) */}
                    <div className="relative flex-shrink-0 flex">
                        <button
                            type="button"
                            onClick={() => setShowModeDropdown(!showModeDropdown)}
                            className={cn(
                                "flex items-center justify-center gap-1.5 px-3 rounded-xl self-stretch sm:min-w-[130px]",
                                "bg-white/80 dark:bg-slate-800/80 backdrop-blur-sm",
                                "border border-slate-200/80 dark:border-slate-600/80",
                                "hover:bg-white dark:hover:bg-slate-800 hover:border-slate-300 dark:hover:border-slate-500",
                                "transition-all text-sm font-medium text-gray-700 dark:text-gray-300"
                            )}
                        >
                            <span className="hidden sm:flex flex-col items-center gap-0 whitespace-nowrap text-center">
                                {SelectedModeIcon && (
                                    <SelectedModeIcon size={16} className="flex-shrink-0 text-indigo-600 dark:text-sky-400" />
                                )}
                                <span className="text-sm leading-none mt-0.5">{selectedModeOption.shortLabel || selectedModeOption.label}</span>
                            </span>
                            <ChevronDown size={14} className={cn(
                                "transition-transform",
                                showModeDropdown && "rotate-180"
                            )} />
                        </button>

                        {/* Mode Dropdown */}
                        {showModeDropdown && (
                            <div className="absolute bottom-full left-0 mb-2 w-full bg-white dark:bg-gray-900 rounded-xl shadow-2xl border border-gray-200 dark:border-gray-700 overflow-hidden z-50">
                                <div className="px-3 py-2 bg-gray-50 dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
                                    <p className="text-xs font-medium text-gray-500 dark:text-gray-400">
                                        Select Mode
                                    </p>
                                </div>
                                {MODE_OPTIONS.map((mode) => {
                                    const Icon = mode.icon;
                                    return (
                                    <button
                                        key={mode.id}
                                        type="button"
                                        onClick={() => handleModeSelect(mode.id)}
                                        className={cn(
                                            "w-full text-left px-4 py-3 hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors border-b border-gray-100 dark:border-gray-800 last:border-b-0",
                                            selectedMode === mode.id && "bg-indigo-50 dark:bg-sky-950/20 border-l-2 border-indigo-500 dark:border-sky-500"
                                        )}
                                    >
                                        <div className="flex items-center justify-center">
                                            <div className="flex flex-col items-center gap-1">
                                                {Icon && (
                                                    <Icon size={18} className="text-indigo-600 dark:text-sky-400" />
                                                )}
                                                <span className="font-medium text-sm text-gray-900 dark:text-white text-center">
                                                    {mode.label}
                                                </span>
                                            </div>
                                        </div>
                                    </button>
                                    );
                                })}
                            </div>
                        )}
                    </div>

                    {/* Text Input */}
                    <div className="flex-1 relative flex">
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
                                "w-full resize-none rounded-xl px-4 py-3.5",
                                "bg-white/80 dark:bg-slate-800/80 backdrop-blur-sm",
                                "border border-slate-200/80 dark:border-slate-600/80",
                                "focus:bg-white dark:focus:bg-slate-800",
                                "focus:border-indigo-400 dark:focus:border-sky-400 focus:outline-none focus:ring-2 focus:ring-indigo-100 dark:focus:ring-sky-900/30",
                                "text-slate-900 dark:text-slate-100 placeholder:text-slate-400 dark:placeholder:text-slate-500",
                                "transition-all duration-200",
                                "disabled:opacity-50 disabled:cursor-not-allowed",
                                "max-h-40 overflow-y-auto text-[15px] leading-relaxed"
                            )}
                            style={{
                                height: "auto",
                                minHeight: "48px",
                            }}
                            onInput={(e) => {
                                const target = e.target as HTMLTextAreaElement;
                                target.style.height = "auto";
                                target.style.height = Math.min(target.scrollHeight, 160) + "px";
                            }}
                        />
                    </div>

                    {/* Send Button */}
                    <button
                        type="submit"
                        disabled={!input.trim() || disabled}
                        className={cn(
                            "flex-shrink-0 w-12 rounded-xl self-stretch min-h-[48px]",
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
            </form>
        </div>
    );
}
