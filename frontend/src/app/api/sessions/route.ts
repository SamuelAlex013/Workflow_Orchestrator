/**
 * GET  /api/sessions  — List all sessions for the logged-in user (newest first)
 * POST /api/sessions  — Create a new session, returns { sessionId }
 */

import { NextRequest, NextResponse } from "next/server";
import { auth } from "@clerk/nextjs/server";
import { connectToDatabase } from "@/lib/mongodb";
import { Session } from "@/lib/models/Session";

// ─── GET: list sessions ──────────────────────────────────────────────────────
export async function GET() {
    try {
        const { userId } = await auth();
        if (!userId) {
            return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
        }

        await connectToDatabase();

        const sessions = await Session.find({ userId })
            .sort({ updatedAt: -1 })   // Most recent first
            .select("_id title mode messageCount createdAt updatedAt")
            .lean();

        // Serialize _id to string for the frontend
        const serialized = sessions.map((s) => ({
            id: (s._id as object).toString(),
            title: s.title,
            mode: s.mode,
            messageCount: s.messageCount,
            updatedAt: s.updatedAt,
            createdAt: s.createdAt,
        }));

        return NextResponse.json({ sessions: serialized });
    } catch (err) {
        console.error("[GET /api/sessions] Error:", err);
        return NextResponse.json(
            { error: "Internal server error" },
            { status: 500 }
        );
    }
}

// ─── POST: create session ────────────────────────────────────────────────────
export async function POST(req: NextRequest) {
    try {
        const { userId } = await auth();
        if (!userId) {
            return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
        }

        const body = await req.json();
        const { title = "New Conversation", mode = "general" } = body;

        await connectToDatabase();

        const session = await Session.create({
            userId,
            title: title.slice(0, 120),   // enforce max length
            mode,
            messageCount: 0,
        });

        return NextResponse.json(
            { sessionId: session._id.toString() },
            { status: 201 }
        );
    } catch (err) {
        console.error("[POST /api/sessions] Error:", err);
        return NextResponse.json(
            { error: "Internal server error" },
            { status: 500 }
        );
    }
}
