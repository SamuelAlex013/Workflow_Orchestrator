import { redirect } from "next/navigation";

// Force dynamic rendering for Clerk auth
export const dynamic = "force-dynamic";

export default function HomePage() {
    redirect("/chat");
}
