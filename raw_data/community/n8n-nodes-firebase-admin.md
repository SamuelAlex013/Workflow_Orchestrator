# Firebase Node for n8n

![Firebase n8n Integration](https://img.shields.io/badge/Firebase-n8n-orange?style=flat-square&logo=firebase)

This node allows you to interact with Firebase Admin SDK in n8n to perform various operations with Firebase Authentication.

## Features

### Authentication Operations

1. **Verify ID Token** - Verify Firebase ID token
2. **Get User by UID** - Get user information by UID
3. **List All Users** - List all users in Firebase Auth
4. **Create User** - Create a new user
5. **Update User** - Update user information
6. **Delete User** - Delete a user

## Installation

1. Make sure you have Node.js version 20.15 or higher installed
2. Install dependencies: `npm install`
3. Build the project: `npm run build`

## Setting up credentials

### Method 1: Service Account JSON (Recommended)

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project
3. Go to Project Settings > Service Accounts
4. Click "Generate New Private Key"
5. Download the JSON file
6. In n8n, paste the contents of the JSON file in the "Service Account JSON" field

### Method 2: Individual fields

1. **Project ID** - Your Firebase project ID
2. **Private Key** - Private key from the service account
3. **Client Email** - Client email from the service account

## Usage

### Verify ID Token

Verifies a Firebase ID token and returns user information.

**Parameters:**
- `ID Token` - Firebase ID token to verify

**Returns:**
- User information (uid, email, displayName, etc.)

### Get User by UID

Gets user information by their UID.

**Parameters:**
- `User UID` - User UID

**Returns:**
- Complete user information

### List All Users

Gets a list of all users in Firebase Auth.

**Parameters:**
- `Max Results` - Maximum number of users to return (max 1000)
- `Next Page Token` - Token for pagination (optional)

**Returns:**
- List of users with pagination information

### Create User

Creates a new user in Firebase Auth.

**Parameters:**
- `Email` - User's email address
- `Password` - User's password
- `Display Name` - Display name
- `Phone Number` - Phone number
- `Email Verified` - Whether the email is verified
- `Disabled` - Whether the account is disabled

**Returns:**
- Information about the created user

### Update User

Updates information about an existing user.

**Parameters:**
- `User UID` - UID of the user to update
- `Email` - New email address
- `Display Name` - New display name
- `Phone Number` - New phone number
- `Email Verified` - Email verification status
- `Disabled` - Account status

**Returns:**
- Updated user information

### Delete User

Deletes a user from Firebase Auth.

**Parameters:**
- `User UID` - UID of the user to delete

**Returns:**
- Success message

## Usage examples

### Verify user token

```json
{
  "resource": "auth",
  "operation": "verifyIdToken",
  "idToken": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### Get list of users

```json
{
  "resource": "auth",
  "operation": "listUsers",
  "maxResults": 100
}
```

### Create new user

```json
{
  "resource": "auth",
  "operation": "createUser",
  "email": "user@example.com",
  "password": "securepassword123",
  "displayName": "John Doe",
  "emailVerified": false,
  "disabled": false
}
```

## Security

- Firebase credentials are stored in encrypted form
- Use service account with minimal required permissions
- Do not share private keys in plain text

## Support

If you encounter problems:
1. Check the correctness of Firebase credentials
2. Make sure the service account has permissions for Firebase Auth
3. Check n8n logs for additional error information

## License

MIT License
