import type { Config } from "tailwindcss";
import typography from "@tailwindcss/typography";

export default {
    content: [
        "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
        "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
        "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
    ],
    theme: {
        extend: {
            colors: {
                background: "var(--background)",
                foreground: "var(--foreground)",
                surface: "var(--surface)",
                // Deep Sea Tech / Modern Minimalist color system
                primary: {
                    DEFAULT: "var(--primary)",
                    hover: "var(--primary-hover)",
                    light: "var(--primary-light)",
                },
                accent: {
                    DEFAULT: "var(--accent)",
                    hover: "var(--accent-hover)",
                },
                success: {
                    DEFAULT: "var(--success)",
                    hover: "var(--success-hover)",
                },
                error: {
                    DEFAULT: "var(--error)",
                    hover: "var(--error-hover)",
                },
                info: {
                    DEFAULT: "var(--info)",
                },
            },
            keyframes: {
                "fade-in": {
                    "0%": { opacity: "0" },
                    "100%": { opacity: "1" },
                },
                "slide-in-from-bottom-4": {
                    "0%": { transform: "translateY(1rem)" },
                    "100%": { transform: "translateY(0)" },
                },
            },
            animation: {
                "in": "fade-in 0.3s ease-out",
            },
        },
    },
    plugins: [typography],
    darkMode: "class",
} satisfies Config;
