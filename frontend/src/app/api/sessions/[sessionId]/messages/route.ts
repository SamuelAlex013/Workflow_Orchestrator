/**
 * GET  /api/sessions/[sessionId]/messages  — Load message history for a session
 * POST /api/sessions/[sessionId]/messages  — Save a message (user or assistant)
 */

import { NextRequest, NextResponse } from "next/server";
import { auth } from "@clerk/nextjs/server";
import { connectToDatabase } from "@/lib/mongodb";
import { Session } from "@/lib/models/Session";
import { Message } from "@/lib/models/Message";
import mongoose from "mongoose";

type RouteContext = { params: Promise<{ sessionId: string }> };

// ─── GET: load messages ───────────────────────────────────────────────────────
export async function GET(_req: NextRequest, context: RouteContext) {
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

        // Verify this session belongs to the user
        const session = await Session.findOne({ _id: sessionId, userId });
        if (!session) {
            return NextResponse.json({ error: "Session not found" }, { status: 404 });
        }

        const messages = await Message.find({ sessionId: session._id })
            .sort({ createdAt: 1 })   // Chronological order
            .lean();

        const serialized = messages.map((m) => ({
            id: (m._id as object).toString(),
            sender: m.sender,
            content: m.content,
            sources: m.sources ?? [],
            confidence: m.confidence ?? null,
            model: m.model ?? null,
            createdAt: m.createdAt,
        }));

        return NextResponse.json({ messages: serialized });
    } catch (err) {
        console.error("[GET /api/sessions/[sessionId]/messages] Error:", err);
        return NextResponse.json(
            { error: "Internal server error" },
            { status: 500 }
        );
    }
}

// ─── POST: save a message ────────────────────────────────────────────────────
export async function POST(req: NextRequest, context: RouteContext) {
    try {
        const { userId } = await auth();
        if (!userId) {
            return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
        }

        const { sessionId } = await context.params;

        if (!mongoose.Types.ObjectId.isValid(sessionId)) {
            return NextResponse.json({ error: "Invalid session ID" }, { status: 400 });
        }

        const body = await req.json();
        const { sender, content, sources, confidence, model } = body;

        if (!sender || !content) {
            return NextResponse.json(
                { error: "sender and content are required" },
                { status: 400 }
            );
        }

        await connectToDatabase();

        // Verify ownership
        const session = await Session.findOne({ _id: sessionId, userId });
        if (!session) {
            return NextResponse.json({ error: "Session not found" }, { status: 404 });
        }

        // Save the message
        const message = await Message.create({
            sessionId: session._id,
            sender,
            content,
            sources: sources ?? [],
            confidence: confidence ?? null,
            model: model ?? null,
        });

        // Update session: bump updatedAt and messageCount
        await Session.updateOne(
            { _id: session._id },
            { $inc: { messageCount: 1 }, updatedAt: new Date() }
        );

        return NextResponse.json(
            { messageId: message._id.toString() },
            { status: 201 }
        );
    } catch (err) {
        console.error("[POST /api/sessions/[sessionId]/messages] Error:", err);
        return NextResponse.json(
            { error: "Internal server error" },
            { status: 500 }
        );
    }
}
