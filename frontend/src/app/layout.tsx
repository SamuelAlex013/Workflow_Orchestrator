import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { ClerkProvider } from "@clerk/nextjs";
import { ThemeProvider } from "@/contexts/ThemeContext";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
    title: "Workflow Orchestrator - AI-Powered Automation Assistant",
    description: "Plan and create intelligent workflow automations with AI assistance",
};

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <ClerkProvider
            appearance={{
                variables: {
                    colorPrimary: "#6366f1", // indigo-500
                },
                elements: {
                    card: "shadow-2xl border border-slate-200 dark:border-slate-800",
                    headerTitle: "text-slate-900 dark:text-white",
                    headerSubtitle: "text-slate-600 dark:text-slate-400"
                }
            }}
            localization={{
                signIn: {
                    start: {
                        title: "Sign in to Workflow Orchestrator",
                    }
                },
                signUp: {
                    start: {
                        title: "Create Workflow Orchestrator Account",
                    }
                }
            }}
        >
            <html lang="en" suppressHydrationWarning>
                <body className={inter.className} suppressHydrationWarning>
                    <ThemeProvider>
                        {children}
                    </ThemeProvider>
                </body>
            </html>
        </ClerkProvider>
    );
}
