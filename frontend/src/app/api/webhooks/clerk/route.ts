import { Webhook } from 'svix';
import { headers } from 'next/headers';
import { WebhookEvent } from '@clerk/nextjs/server';
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

export async function POST(req: Request) {
    // Get the headers
    const headerPayload = await headers();
    const svix_id = headerPayload.get('svix-id');
    const svix_timestamp = headerPayload.get('svix-timestamp');
    const svix_signature = headerPayload.get('svix-signature');

    // If there are no headers, error out
    if (!svix_id || !svix_timestamp || !svix_signature) {
        return new Response('Error: Missing svix headers', {
            status: 400,
        });
    }

    // Get the body
    const payload = await req.json();
    const body = JSON.stringify(payload);

    // Create a new Svix instance with your webhook secret
    const wh = new Webhook(process.env.CLERK_WEBHOOK_SECRET || '');

    let evt: WebhookEvent;

    // Verify the payload with the headers
    try {
        evt = wh.verify(body, {
            'svix-id': svix_id,
            'svix-timestamp': svix_timestamp,
            'svix-signature': svix_signature,
        }) as WebhookEvent;
    } catch (err) {
        console.error('Error verifying webhook:', err);
        return new Response('Error: Verification failed', {
            status: 400,
        });
    }

    // Handle the webhook
    const eventType = evt.type;

    if (eventType === 'user.created') {
        const { id, email_addresses, first_name, last_name } = evt.data;

        try {
            // Create user in database
            await prisma.user.create({
                data: {
                    clerkId: id,
                    email: email_addresses[0]?.email_address || '',
                    name: first_name && last_name
                        ? `${first_name} ${last_name}`
                        : first_name || last_name || null,
                    themePreference: 'light',
                },
            });

            console.log(`✅ User created: ${id}`);
        } catch (error) {
            console.error('Error creating user in database:', error);
            return new Response('Error: Failed to create user', {
                status: 500,
            });
        }
    }

    if (eventType === 'user.updated') {
        const { id, email_addresses, first_name, last_name } = evt.data;

        try {
            // Update user in database
            await prisma.user.update({
                where: { clerkId: id },
                data: {
                    email: email_addresses[0]?.email_address || '',
                    name: first_name && last_name
                        ? `${first_name} ${last_name}`
                        : first_name || last_name || null,
                },
            });

            console.log(`✅ User updated: ${id}`);
        } catch (error) {
            console.error('Error updating user in database:', error);
            return new Response('Error: Failed to update user', {
                status: 500,
            });
        }
    }

    if (eventType === 'user.deleted') {
        const { id } = evt.data;

        try {
            // Delete user from database
            await prisma.user.delete({
                where: { clerkId: id },
            });

            console.log(`✅ User deleted: ${id}`);
        } catch (error) {
            console.error('Error deleting user from database:', error);
            return new Response('Error: Failed to delete user', {
                status: 500,
            });
        }
    }

    return new Response('Webhook received', { status: 200 });
}
