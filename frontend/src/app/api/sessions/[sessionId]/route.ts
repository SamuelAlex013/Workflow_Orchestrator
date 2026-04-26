/**
 * DELETE /api/sessions/[sessionId]  — Delete a session and all its messages
 * PATCH  /api/sessions/[sessionId]  — Update session title
 */

import { NextRequest, NextResponse } from "next/server";
import { auth } from "@clerk/nextjs/server";
import { connectToDatabase } from "@/lib/mongodb";
import { Session } from "@/lib/models/Session";
import { Message } from "@/lib/models/Message";
import mongoose from "mongoose";

type RouteContext = { params: Promise<{ sessionId: string }> };

// ─── DELETE: delete session + all messages ───────────────────────────────────
export async function DELETE(_req: NextRequest, context: RouteContext) {
    try {
        const { userId } = await auth();
        if (!userId) {
            return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
        }

        const { sessionId } = await context.params;

        if (!mongoose.Types.ObjectId.isValid(sessionId)) {
            return NextResponse.json({ error: "Invalid session ID" }, { status: 400 });
        }

        await connectToDatabase();

        // Verify ownership before deleting
        const session = await Session.findOne({ _id: sessionId, userId });
        if (!session) {
            return NextResponse.json({ error: "Session not found" }, { status: 404 });
        }

        // Delete messages first, then the session
        await Message.deleteMany({ sessionId: session._id });
        await Session.deleteOne({ _id: session._id });

        return NextResponse.json({ success: true });
    } catch (err) {
        console.error("[DELETE /api/sessions/[sessionId]] Error:", err);
        return NextResponse.json(
            { error: "Internal server error" },
            { status: 500 }
        );
    }
}

// ─── PATCH: rename session title ─────────────────────────────────────────────
export async function PATCH(req: NextRequest, context: RouteContext) {
    try {
        const { userId } = await auth();
        if (!userId) {
            return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
        }

        const { sessionId } = await context.params;
        const { title } = await req.json();

        if (!mongoose.Types.ObjectId.isValid(sessionId)) {
            return NextResponse.json({ error: "Invalid session ID" }, { status: 400 });
        }

        await connectToDatabase();

        const session = await Session.findOneAndUpdate(
            { _id: sessionId, userId },
            { title: String(title).slice(0, 120) },
            { new: true }
        );

        if (!session) {
            return NextResponse.json({ error: "Session not found" }, { status: 404 });
        }

        return NextResponse.json({ success: true, title: session.title });
    } catch (err) {
        console.error("[PATCH /api/sessions/[sessionId]] Error:", err);
        return NextResponse.json(
            { error: "Internal server error" },
            { status: 500 }
        );
    }
}
