# Environment Setup Guide

## Step 1: Copy this file
```bash
cp .env.example .env.local
```

## Step 2: Add Your Credentials

Open `.env.local` and replace the placeholder values with your actual credentials:

### Clerk Authentication Keys
1. Go to [https://dashboard.clerk.com/](https://dashboard.clerk.com/)
2. Select your "AI Workflow Orchestrator" application
3. Navigate to **API Keys** in the sidebar
4. Copy your keys:

```env
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_...
CLERK_SECRET_KEY=sk_test_...
```

### PostgreSQL Database URL
From your Neon dashboard, copy the connection string:

```env
DATABASE_URL=postgresql://username:password@ep-...neon.tech/dbname?sslmode=require
```

## Step 3: Initialize the Database

After setting up your `.env.local`:

```bash
# Generate Prisma Client
npx prisma generate

# Create database tables
npx prisma db push
```

## Step 4: Run the Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## Troubleshooting

### If dependencies aren't installed:
```bash
npm install
```

### If Prisma client isn't generated:
```bash
npx prisma generate
```

### If authentication isn't working:
- Verify Clerk keys are correct
- Check that Clerk middleware is properly configured
- Ensure you're using the correct environment (development)
