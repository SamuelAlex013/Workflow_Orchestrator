"use client";

import { useState, FormEvent, KeyboardEvent, useRef, useEffect } from "react";
import { Send, ChevronDown, Sparkles, Lock } from "lucide-react";
import { cn } from "@/lib/utils";

type Mode = "general" | "workflow_planning" | "advanced_automation";

interface Model {
    id: string;
    name: string;
    description: string;
    disabled?: boolean;
    comingSoon?: boolean;
}

const MODELS: Model[] = [
    {
        id: "orchestrator-v1",
        name: "Orchestrator v1.0",
        description: "Best for workflow automation guidance",
        disabled: false,
    },
    {
        id: "orchestrator-advanced",
        name: "Advanced Orchestrator",
        description: "Enhanced capabilities",
        disabled: true,
        comingSoon: true,
    },
    {
        id: "workflow-builder",
        name: "Workflow Creation (n8n Visual Builder)",
        description: "Direct n8n workflow creation",
        disabled: true,
        comingSoon: true,
    },
];

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
    const [selectedModel, setSelectedModel] = useState(MODELS[0]);
    const [showModelDropdown, setShowModelDropdown] = useState(false);
    const [showModeDropdown, setShowModeDropdown] = useState(false);
    const [selectedMode, setSelectedMode] = useState<Mode>("general");
    const [cursorPosition, setCursorPosition] = useState(0);
    const textareaRef = useRef<HTMLTextAreaElement>(null);
    const modelDropdownRef = useRef<HTMLDivElement>(null);
    const modeDropdownRef = useRef<HTMLDivElement>(null);

    // Close dropdowns when clicking outside
    useEffect(() => {
        const handleClickOutside = (event: MouseEvent) => {
            if (modelDropdownRef.current && !modelDropdownRef.current.contains(event.target as Node)) {
                setShowModelDropdown(false);
            }
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
            setSelectedMode("general");
        }
    };

    const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSubmit(e);
        }
    };

    const handleModeSelect = (mode: Mode, locked?: boolean) => {
        if (locked) {
            // Show locked feature notice
            alert("🔒 Advanced Automation is a premium feature available only to authorized users.");
            setShowModeDropdown(false);
            return;
        }

        setSelectedMode(mode as Mode);
        // Remove @ from input
        setInput(input.slice(0, -1));
        setShowModeDropdown(false);
    };

    return (
        <div className="border-t border-gray-200/50 dark:border-gray-800/50 bg-white/80 dark:bg-gray-950/80 backdrop-blur-sm p-6">
            <form onSubmit={handleSubmit} className="max-w-4xl mx-auto">
                <div className="flex flex-col gap-3">
                    {/* Model Selector */}
                    <div className="relative" ref={modelDropdownRef}>
                        <button
                            type="button"
                            onClick={() => setShowModelDropdown(!showModelDropdown)}
                            className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors text-sm font-medium text-gray-700 dark:text-gray-300"
                        >
                            <Sparkles size={14} className="text-purple-500" />
                            {selectedModel.name}
                            <ChevronDown size={14} />
                        </button>

                        {showModelDropdown && (
                            <div className="absolute bottom-full left-0 mb-2 w-80 bg-white dark:bg-gray-900 rounded-xl shadow-2xl border border-gray-200 dark:border-gray-700 overflow-hidden z-50">
                                {MODELS.map((model) => (
                                    <button
                                        key={model.id}
                                        type="button"
                                        onClick={() => {
                                            if (!model.disabled) {
                                                setSelectedModel(model);
                                                setShowModelDropdown(false);
                                            }
                                        }}
                                        disabled={model.disabled}
                                        className={cn(
                                            "w-full text-left px-4 py-3 hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors border-b border-gray-100 dark:border-gray-800 last:border-b-0",
                                            model.disabled && "opacity-50 cursor-not-allowed",
                                            selectedModel.id === model.id && "bg-purple-50 dark:bg-purple-950/20"
                                        )}
                                    >
                                        <div className="flex items-start justify-between">
                                            <div className="flex-1">
                                                <div className="font-medium text-gray-900 dark:text-white text-sm">
                                                    {model.name}
                                                </div>
                                                <div className="text-xs text-gray-500 dark:text-gray-400 mt-0.5">
                                                    {model.description}
                                                </div>
                                            </div>
                                            {model.comingSoon && (
                                                <span className="ml-2 px-2 py-0.5 text-xs font-medium bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300 rounded">
                                                    Coming Soon
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
                                    "bg-gray-50 dark:bg-gray-900/50",
                                    "border border-gray-200 dark:border-gray-700",
                                    "focus:border-purple-400 dark:focus:border-purple-600 focus:outline-none focus:ring-2 focus:ring-purple-100 dark:focus:ring-purple-900/30",
                                    "text-gray-900 dark:text-white placeholder:text-gray-400 dark:placeholder:text-gray-500",
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

                            {/* @Mention Dropdown */}
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
                                            onClick={() => handleModeSelect(mode.id as Mode, mode.locked)}
                                            className={cn(
                                                "w-full text-left px-4 py-3 hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors border-b border-gray-100 dark:border-gray-800 last:border-b-0",
                                                mode.locked && "bg-gray-50/50 dark:bg-gray-800/50"
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

                        <button
                            type="submit"
                            disabled={!input.trim() || disabled}
                            className={cn(
                                "flex-shrink-0 w-12 h-12 rounded-2xl",
                                "bg-gradient-to-r from-purple-500 to-purple-600 hover:from-purple-600 hover:to-purple-700",
                                "disabled:from-gray-300 disabled:to-gray-300 dark:disabled:from-gray-700 dark:disabled:to-gray-700",
                                "disabled:cursor-not-allowed",
                                "flex items-center justify-center",
                                "transition-all duration-200",
                                "hover:scale-105 active:scale-95",
                                "shadow-lg shadow-purple-500/30 disabled:shadow-none"
                            )}
                        >
                            <Send size={18} className="text-white" />
                        </button>
                    </div>

                    {/* Mode Indicator */}
                    {selectedMode !== "general" && (
                        <div className="flex items-center gap-2 text-xs text-gray-500 dark:text-gray-400 pl-1">
                            <span className="font-medium">
                                Mode: {MODE_OPTIONS.find(m => m.id === selectedMode)?.label}
                            </span>
                            <button
                                type="button"
                                onClick={() => setSelectedMode("general")}
                                className="text-purple-500 hover:text-purple-600 underline"
                            >
                                Reset
                            </button>
                        </div>
                    )}
                </div>
            </form>
        </div>
    );
}
