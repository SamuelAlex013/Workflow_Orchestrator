import { SignUp } from "@clerk/nextjs";

export default function SignUpPage() {
    return (
        <div className="min-h-screen flex items-center justify-center bg-slate-50 dark:bg-[#0F172A]">
            <SignUp />
        </div>
    );
}
