import mongoose, { Document, Schema } from "mongoose";

export interface IMessage extends Document {
    _id: mongoose.Types.ObjectId;
    sessionId: mongoose.Types.ObjectId;  // References Session._id
    sender: "user" | "assistant";
    content: string;
    sources?: string[];                   // Only for assistant messages (RAG sources)
    confidence?: string;                  // "high" | "medium" | "low"
    model?: string;                       // Which LLM model generated the response
    createdAt: Date;
    updatedAt: Date;
}

const MessageSchema = new Schema<IMessage>(
    {
        sessionId: {
            type: Schema.Types.ObjectId,
            ref: "Session",
            required: true,
            index: true,
        },
        sender: {
            type: String,
            enum: ["user", "assistant"],
            required: true,
        },
        content: {
            type: String,
            required: true,
        },
        sources: {
            type: [String],
            default: [],
        },
        confidence: {
            type: String,
            default: null,
        },
        model: {
            type: String,
            default: null,
        },
    },
    {
        timestamps: true,
    }
);

// Index for fast ordered message retrieval within a session
MessageSchema.index({ sessionId: 1, createdAt: 1 });

export const Message =
    (mongoose.models.Message as mongoose.Model<IMessage>) ||
    mongoose.model<IMessage>("Message", MessageSchema);
