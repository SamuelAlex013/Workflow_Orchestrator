import mongoose, { Document, Schema } from "mongoose";

export interface ISession extends Document {
    _id: mongoose.Types.ObjectId;
    userId: string;           // Clerk user ID — sessions are always user-scoped
    title: string;            // Auto-generated from the first user message (first 60 chars)
    mode: "general" | "workflow_planning";
    messageCount: number;     // Denormalized count for display without a join
    createdAt: Date;
    updatedAt: Date;
}

const SessionSchema = new Schema<ISession>(
    {
        userId: {
            type: String,
            required: true,
            index: true,         // Fast lookups by user
        },
        title: {
            type: String,
            required: true,
            default: "New Conversation",
            maxlength: 120,
        },
        mode: {
            type: String,
            enum: ["general", "workflow_planning"],
            default: "general",
        },
        messageCount: {
            type: Number,
            default: 0,
        },
    },
    {
        timestamps: true,        // Adds createdAt + updatedAt automatically
    }
);

// Compound index: list sessions sorted by most recently updated
SessionSchema.index({ userId: 1, updatedAt: -1 });

// Prevent model re-registration during Next.js hot reload
export const Session =
    (mongoose.models.Session as mongoose.Model<ISession>) ||
    mongoose.model<ISession>("Session", SessionSchema);
