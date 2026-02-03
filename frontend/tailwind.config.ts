import type { Config } from "tailwindcss";

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
    plugins: [],
    darkMode: "class",
} satisfies Config;
