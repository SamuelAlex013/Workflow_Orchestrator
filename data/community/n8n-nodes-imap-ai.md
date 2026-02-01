# n8n IMAP Node

An n8n community node for IMAP email operations with advanced search and management functions.

## Installation

```bash
npm install n8n-nodes-imap-ai
```

Alternatively via n8n Community Nodes GUI: `n8n-nodes-imap-ai`

## Features

### Email Operations

**List Emails**
- Lists emails in a mailbox folder
- Configurable limit
- Sorted by UID (newest first)

**Get Email**
- Retrieves a single email with full content
- Supports text and HTML content
- Parses email headers and metadata

**Search Emails**
- Two modes: Simple Search and Advanced Search
- Server-side IMAP SEARCH for performance
- Combinable search criteria in Advanced mode

**Move Email**
- Moves emails between mailbox folders
- Uses IMAP MOVE command

**Mark Email**
- Marks emails as read or unread
- Changes IMAP flags accordingly

**Delete Email**
- Marks emails for deletion
- Uses IMAP STORE with \Deleted flag

**Download Attachment**
- Downloads email attachments
- Supports various attachment types

### Mailbox Operations

**List Mailboxes**
- Lists all available IMAP folders
- Supports hierarchical folder structures

**Create Mailbox**
- Creates new IMAP folders
- Validates folder names

### Draft Operations

**Create Draft**
- Creates email drafts
- Supports text and HTML format
- Configurable recipients, subject and content

## Email Search

### Simple Search Mode

Provides predefined filters:
- All Emails
- Unread Emails  
- Read Emails
- Today's Emails
- This Week's Emails

Optional with text search that simultaneously searches Subject, From and Body.

### Advanced Search Mode

Combinable criteria:

**Content Filters:**
- From (Sender): Email address or name
- To (Recipient): Target email address
- Subject Contains: Text in subject
- Body Contains: Text in email content

**Status Filters:**
- Read Status: Any/Unread Only/Read Only
- Flagged: Include flagged emails
- Has Attachments: Filter by attachment presence

**Date Filters:**
- Quick Date: Today/Yesterday/This Week/Last Week/This Month/Last Month
- Custom Date Range: From/To dates
- Date combinations for precise time windows

**Size Filters:**
- Size threshold with larger/smaller options
- Configurable in KB for bandwidth management

## Configuration

### IMAP Credentials

Required fields:
- **Host**: IMAP server address
- **Port**: Server port (usually 993 for SSL)
- **User**: Email address
- **Password**: Email password or app password
- **Secure**: Enable SSL/TLS (recommended)

### Common IMAP Settings

**Gmail:**
- Host: imap.gmail.com
- Port: 993
- Secure: Yes
- Note: Requires App Password with 2FA enabled

**Outlook/Hotmail:**
- Host: outlook.office365.com
- Port: 993
- Secure: Yes

## Usage Examples

### Basic Email Listing

```javascript
{
  "operation": "listEmails",
  "mailbox": "INBOX",
  "limit": 20
}
```

### Simple Email Search

```javascript
// Simple Mode: Quick filter with text search
{
  "operation": "searchEmails",
  "searchMode": "simple", 
  "quickFilter": "today",
  "simpleSearchText": "invoice"
}
```

### Advanced Email Search

```javascript
// Advanced Mode: Multiple combined criteria
{
  "operation": "searchEmails",
  "searchMode": "advanced",
  "advancedCriteria": {
    "from": "billing@company.com",
    "subject": "payment", 
    "readStatus": "unread",
    "quickDate": "thisWeek",
    "hasAttachments": "yes"
  }
}
```

### Email Management

```javascript
// Get email
{
  "operation": "getEmail",
  "mailbox": "INBOX",
  "emailUid": "12345"
}

// Move email  
{
  "operation": "moveEmail",
  "mailbox": "INBOX",
  "emailUid": "12345", 
  "targetMailbox": "Archive"
}
```

## Compatibility

**Tested IMAP Servers:**
- Gmail (imap.gmail.com)
- Outlook/Exchange
- Standard IMAP-compliant servers

**Requirements:**
- n8n Version >= 0.190.0
- Node.js >= 16
- IMAP server with SSL/TLS support

## Known Limitations

- OAuth2 authentication not yet implemented
- Attachment search uses Content-Type workaround (IMAP standard limitation)
- Large email attachments can be memory-intensive

## Development

### Adding New Operations

1. Create operation class in `operations/`
2. Implement `IImapOperation` interface  
3. Register in `operationRegistry.ts`
4. Define UI parameters in `ImapNodeProperties.ts`

### Build & Test

```bash
npm run build
npm test
```

## Changelog

**v2.3.9**
- Fixed missing draftFolder parameter for Create Draft operation
- Added resourceLocator for draft folder selection

**v2.3.0**
- New Multi-Criteria Search UI
- Simple vs Advanced Search modes
- Extended Date/Size/Attachment filters

**v2.2.4** 
- Promise.race() timeout fix for IMAP logout
- Improved connection stability

**v2.2.0**
- Modular architecture refactoring
- Operations Registry pattern
- Improved error handling

## Support

- GitHub Issues: [Repository Issues](https://github.com/terschawebIT/terschaweb-nodes-imap/issues)
- Email: support@terschaweb.de

## License

MIT License

