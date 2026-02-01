# n8n-nodes-dav

This is an n8n community node. It lets you use WebDAV, CalDAV, and CardDAV protocols in your n8n workflows.

WebDAV, CalDAV, and CardDAV are standard protocols for accessing and managing files, calendars, and address books on remote servers. These nodes enable seamless integration with DAV-compliant servers for comprehensive data synchronization and management.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Manual Installation

1. Clone the repository:
```bash
git clone https://github.com/x40x1/n8n-nodes-dav.git
cd n8n-nodes-dav
```

2. Install dependencies:
```bash
npm install
```

3. Build the project:
```bash
npm run build
```

## Operations

### WebDAV Node
- **Download File**: Retrieve files from the DAV server
- **Upload File**: Upload files to the DAV server
- **Get Properties**: List directory contents and file properties
- **Create Directory**: Create new directories
- **Delete Resource**: Remove files or directories
- **Move Resource**: Move files/directories to new locations
- **Copy Resource**: Copy files/directories

### CalDAV Node
- **Get Calendars**: List available calendars
- **Get Events**: Retrieve calendar events with optional time filtering
- **Create Event**: Add new calendar events
- **Update Event**: Modify existing events
- **Delete Event**: Remove calendar events

### CardDAV Node
- **Get Address Books**: List available address books
- **Get Contacts**: Retrieve contacts with optional filtering
- **Create Contact**: Add new contacts
- **Update Contact**: Modify existing contacts
- **Delete Contact**: Remove contacts

## Credentials

The nodes require authentication with your DAV server. You need to create a "DAV API" credential in n8n.

### Prerequisites
- Access to a DAV-compliant server (Nextcloud, OwnCloud, Apache/mod_dav, etc.)
- Valid username and password for the DAV server

### Authentication Methods
- **Basic Authentication**: Username and password authentication
- **Server Configuration**: Base URL of your DAV server

### Setup Steps
1. In n8n, go to **Settings > Credentials**
2. Create a new **"DAV API"** credential
3. Enter your DAV server details:
   - **Base URL**: Your DAV server URL (e.g., `https://dav.example.com`)
   - **Username**: Your DAV server username
   - **Password**: Your DAV server password

## Compatibility

- **Minimum n8n version**: 1.0.0
- **Tested with**: n8n 1.0.x and 1.1.x
- **Node.js**: >= 18.0.0 (recommended: 20.x)
- **DAV Server Compatibility**:
  - Nextcloud (full WebDAV/CalDAV/CardDAV support)
  - OwnCloud (standard DAV protocol support)
  - Apache/mod_dav (basic WebDAV functionality)
  - SabreDAV (PHP-based DAV server library)
  - Other RFC-compliant DAV servers

## Usage

### Basic Setup
1. Install the nodes following the installation guide
2. Configure your DAV credentials
3. Add a DAV node to your workflow
4. Select the appropriate resource (File/Calendar/Address Book)
5. Choose your desired operation
6. Configure the operation parameters

### Advanced Features

#### Expression Support
All nodes support n8n expressions for dynamic values:
- File paths: `{{$json.filename}}`
- Calendar paths: `{{$node["Previous Node"].json.calendarPath}}`
- Contact filters: `{{$json.searchTerm}}`

#### Workflow Integration Examples

**File Processing Workflow:**
```javascript
// WebDAV + File Processing nodes
const fileContent = item.json.fileContent;
const processedContent = fileContent.toString().toUpperCase();
item.json.processedFile = processedContent;
```

**Calendar Data Integration:**
```javascript
// CalDAV + Calendar nodes
const icalData = item.json.calendarData;
// Parse iCalendar format for n8n calendar nodes
item.json.events = parseICalendar(icalData);
```

**Contact Synchronization:**
```javascript
// CardDAV + CRM/Contact nodes
const vcardData = item.json.contactData;
// Transform vCard to structured contact format
item.json.contact = {
  name: extractVCardField(vcardData, 'FN'),
  email: extractVCardField(vcardData, 'EMAIL'),
  phone: extractVCardField(vcardData, 'TEL')
};
```

### Development

#### Building
```bash
npm run build
```

#### Linting
```bash
npm run lint
npm run lintfix  # Auto-fix issues
```

#### Testing
Test the nodes locally using n8n desktop or your n8n instance.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [WebDAV RFC 4918](https://tools.ietf.org/html/rfc4918)
* [CalDAV RFC 4791](https://tools.ietf.org/html/rfc4791)
* [CardDAV RFC 6352](https://tools.ietf.org/html/rfc6352)
* [Nextcloud DAV documentation](https://docs.nextcloud.com/server/latest/developer_manual/client_apis/WebDAV/index.html)

## Version history

### 0.1.0
- Initial release
- WebDAV node with 7 operations (Download, Upload, Get Properties, Create Directory, Delete, Move, Copy)
- CalDAV node with 5 operations (Get Calendars, Get Events, Create Event, Update Event, Delete Event)
- CardDAV node with 5 operations (Get Address Books, Get Contacts, Create Contact, Update Contact, Delete Contact)
- Shared DAV API credentials
- Full RFC compliance for DAV protocols
- Expression support for dynamic values
- Comprehensive error handling and workflow integration
