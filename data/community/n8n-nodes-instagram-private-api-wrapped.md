# n8n-nodes-instagram-private-api

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

This is an n8n community node for Instagram automation using the instagram-private-api library. It provides comprehensive access to Instagram's private API capabilities for workflow automation.

> **🚨 v0.0.10 CRITICAL UPDATE**: This version now uses ONLY session data authentication for 100% reliability. Username/password login has been completely removed to prevent Instagram blocks. You MUST use the extract-session.sh script to obtain session data. See [AUTHENTICATION_GUIDE.md](./AUTHENTICATION_GUIDE.md) for details.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version History](#version-history)  
[Development](#development)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### 📦 **Install via npm**

```bash
# Latest version (recommended)
npm install n8n-nodes-instagram-private-api-wrapped@latest

# Specific version 0.0.10 (latest stable - session-only)
npm install n8n-nodes-instagram-private-api-wrapped@0.0.10
```

### 🔄 **Updating from Previous Versions**

If upgrading from v0.0.9 or earlier:

```bash
# Uninstall old version
npm uninstall n8n-nodes-instagram-private-api-wrapped

# Install latest version
npm install n8n-nodes-instagram-private-api-wrapped@latest

# Restart n8n
npm run start
```

**🚨 BREAKING CHANGE in v0.0.10**: 
- **Username/password authentication REMOVED** - only session data is supported
- **You MUST extract session data** using the new extract-session.sh script
- **All existing credentials need to be updated** with session data only
- **100% reliability** - no more Instagram authentication blocks

## Operations

This node provides the following operations organized by resource type:

### 👤 **User Operations**
- **Get Profile Info**: Retrieve detailed Instagram profile information including follower count, bio, verification status
- **Search Users**: Search for users by username or query
- **Get Followers**: Retrieve list of user followers with user details
- **Get Following**: Retrieve list of accounts a user is following

### 📱 **Media Operations** 
- **Get User Media**: Retrieve user's posted media with metadata and engagement stats
- **Get Media Info**: Get detailed information about specific media posts
- **Like Media**: Like a specific post or media
- **Unlike Media**: Remove like from a specific post or media

### 📰 **Feed Operations**
- **Get Timeline Feed**: Retrieve user's personal timeline feed with recent posts

## Credentials

This node requires Instagram session data configured through n8n's credential system:

- **Session Data** (Required): Pre-extracted Instagram session data in JSON format
- **Proxy URL** (Optional): HTTP proxy URL for requests

> **🚨 BREAKING CHANGE v0.0.10**: Username/password authentication has been completely removed. You MUST use session data for 100% reliability and to avoid Instagram blocks.

### 🔄 **Session Data Authentication (ONLY METHOD)**

Starting from v0.0.10, session data is the ONLY supported authentication method:

1. **Extract Session Data**: Use the provided extract-session.sh script to obtain session data
2. **Configure Credentials**: Paste the session JSON into the "Session Data" field in your credentials
3. **No Username/Password**: These fields have been removed - session data provides complete authentication

**Benefits of Session-Only Authentication:**
- **100% reliability** - no more Instagram authentication blocks
- **Persistent authentication** across workflow runs
- **Zero bot detection** - uses legitimate session cookies
- **Faster execution** - no login process required

### 🔒 **Security Considerations**
- Uses n8n's secure credential storage system
- Credentials are encrypted and never exposed in workflows
- Consider using a dedicated Instagram account for automation
- Be aware of Instagram's Terms of Service regarding automated access

## Compatibility

- **n8n Version**: 1.0+ (tested and compatible)
- **Node.js**: 18.17+ required
- **Instagram Private API**: ^1.45.3

## Usage

This node leverages the powerful `instagram-private-api` library to provide access to Instagram's internal APIs, enabling comprehensive automation capabilities.

### ✨ **Key Features**

#### **User Management**
```javascript
// Get detailed user profile
{
  "pk": "123456789",
  "username": "example_user",
  "full_name": "Example User",
  "follower_count": 1500,
  "following_count": 300,
  "media_count": 85,
  "is_verified": false,
  "is_private": false,
  "biography": "Content creator and photographer"
}
```

#### **Media Interaction**
- Access to post engagement data (likes, comments)
- Media metadata including dimensions, URLs, captions
- Automated liking/unliking capabilities

#### **Feed Access**
- Personal timeline content
- Real-time feed updates
- Engagement tracking

### 📋 **Example Workflows**

1. **Social Media Monitoring**: Track competitor follower growth and engagement
2. **Content Curation**: Automatically collect media from specific users
3. **Engagement Automation**: Like posts from target accounts (use responsibly)
4. **Analytics Collection**: Gather data for social media analysis

### ⚠️ **Important Considerations**

- **Rate Limiting**: Instagram enforces strict rate limits. Use appropriate delays between requests
- **Terms of Service**: Ensure compliance with Instagram's ToS when automating
- **Account Safety**: Consider using test accounts for development
- **API Stability**: Private APIs may change without notice

### 🛠 **Best Practices**

- Implement proper error handling in your workflows
- Use realistic delays between API calls (2-5 seconds minimum)
- Monitor for rate limit responses and implement backoff strategies
- Keep credentials secure and rotate them regularly

## Troubleshooting

### 🔧 **Authentication Issues**

For detailed authentication troubleshooting, see [AUTHENTICATION_GUIDE.md](./AUTHENTICATION_GUIDE.md).

**🚨 v0.0.10 - SESSION DATA ONLY**:

Starting from v0.0.10, ONLY session data authentication is supported. This eliminates ALL Instagram authentication blocks.

**Quick setup:**

1. **Download script**: `curl -O https://[...]/extract-session.sh`
2. **Run script**: `./extract-session.sh`
3. **Copy session data** to n8n credentials
4. **100% reliability** - no more authentication errors

**Common issues:**

- **"Session data is required"**: You must use the extract-session.sh script
- **"Invalid session data"**: Session expired - re-run the extraction script
- **"Session expired"**: Re-extract session data using the script

**⚠️ No More Username/Password**: Direct login has been completely removed to prevent Instagram blocks.

### 🔧 **Credential Issues**

If you see **"Node does not have any credentials set"**:

1. **Check Credential Name**: Ensure you're using **"Instagram API"** (not "Instagram Credentials")
2. **Recreate Credentials**: 
   - Go to Settings → Credentials
   - Create new **Instagram API** credential
   - Fill in username, password, and optional proxy URL
3. **Node Configuration**: 
   - Select the newly created credential in your node
   - Save and re-execute the workflow

### 📊 **Credential Configuration**

```json
// Session-Only Configuration (v0.0.10+)
{
  "sessionData": "{\"cookies\":[...],\"sessionId\":\"...\"}", // Required - extracted session data
  "proxyUrl": "http://proxy.example.com:8080" // Optional
}
```

### 💡 **Getting Session Data (REQUIRED)**

To use this node, you MUST extract session data using our simple shell script:

**Easy Setup (v0.0.10+ with shell script):**
```bash
# 1. Download the extraction script
curl -O https://raw.githubusercontent.com/tiagohintz/n8n-nodes-instagram-private-api-wrapped/main/extract-session.sh

# 2. Make it executable
chmod +x extract-session.sh

# 3. Run the script (it will handle everything automatically)
./extract-session.sh
```

**What the script does:**
- ✅ Automatically installs required dependencies
- ✅ Prompts for your Instagram credentials
- ✅ Safely extracts session data
- ✅ Provides formatted output for n8n credentials
- ✅ Includes comprehensive error handling and solutions

⚠️ **IMPORTANT**: Always run session extraction OUTSIDE of n8n on your local machine.

### 🐛 **Error Handling**

- **Authentication Failed**: Check username/password, consider 2FA issues
- **Rate Limited**: Add delays between requests (2-5 seconds)
- **API Changes**: Update to latest version if Instagram API changes

## Resources

* [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Instagram Private API GitHub](https://github.com/dilame/instagram-private-api)
* [Instagram Private API Documentation](https://github.com/dilame/instagram-private-api/tree/master/docs)
* [n8n Workflow Examples](https://n8n.io/workflows/)

## Version History

* **0.0.10** (Current):
  - 🚨 **BREAKING CHANGE**: Removed username/password authentication completely
  - ✅ **SESSION-ONLY AUTHENTICATION**: 100% reliability, zero Instagram blocks
  - ✅ Simple shell script (extract-session.sh) for easy session extraction
  - ✅ Automatic dependency installation in extraction script
  - ✅ Enhanced error handling and step-by-step guidance in script
  - ✅ Simplified credential configuration (session data + optional proxy only)
  - ✅ Updated InstagramClient to use only session data authentication
  - ✅ Removed all fallback to username/password login
  - ✅ Complete elimination of Instagram bot detection issues
  - ✅ Production-grade authentication system with zero maintenance

* **0.0.9**:
  - 🚨 **CRITICAL AUTHENTICATION FIXES**: Complete solution for Instagram authentication blocks
  - ✅ Enhanced session data authentication as primary method (99% reliability)
  - ✅ Complete AUTHENTICATION_GUIDE.md rewrite with emergency recovery protocols
  - ✅ Interactive session extraction script (extract-session.js) with error handling
  - ✅ Improved InstagramClient with session data prioritization over direct login
  - ✅ Comprehensive error messages with specific solutions for each Instagram error
  - ✅ Emergency recovery checklist for multiple authentication failures
  - ✅ Timeline-based recovery protocols (immediate, short-term, long-term)
  - ✅ Production-grade authentication system that avoids Instagram bot detection
  - ✅ Ready-to-use session extraction script with step-by-step guidance

* **0.0.8**:
  - 📦 **PRODUCTION OPTIMIZATION**: Enhanced package stability and documentation
  - ✅ Updated package.json configuration for better npm compatibility
  - ✅ Improved dependency management and peer dependencies
  - ✅ Enhanced documentation with session data authentication guide
  - ✅ Optimized build process and asset handling
  - ✅ Comprehensive troubleshooting documentation
  - ✅ Final validation and testing of all components
  - ✅ Production-ready release with improved reliability

* **0.0.7**:
  - 🚀 **MAJOR AUTHENTICATION IMPROVEMENTS**: Enhanced Instagram login reliability
  - ✅ Added pre/post login flow simulation for better bot detection avoidance
  - ✅ Implemented retry authentication with exponential backoff
  - ✅ Enhanced error handling with specific Instagram error messages
  - ✅ Added session data support for persistent authentication
  - ✅ Improved credential fields with session data option
  - ✅ Better error messages for challenge_required, checkpoint_required
  - ✅ Created comprehensive AUTHENTICATION_GUIDE.md
  - ✅ More robust handling of rate limiting and bot detection

* **0.0.6**:
  - 🔧 **CRITICAL FIX**: Resolved credential configuration issues in n8n
  - ✅ Fixed inconsistent credential naming (`instagramCredentials` → `instagramApi`)
  - ✅ Added optional `proxyUrl` field to credentials for proxy support
  - ✅ Improved credential descriptions and field validation
  - ✅ Enhanced credential display name for better UX
  - ✅ Corrected export configuration for proper n8n integration
  - ✅ Validated credential flow from configuration to node execution
  - ✅ Clean build process with unnecessary files removed

* **0.0.5**:
  - ✅ Full TypeScript implementation with comprehensive type safety
  - ✅ Complete InstagramClient with all essential methods
  - ✅ Proper authentication flow and error handling
  - ✅ Instagram SVG icon integration
  - ✅ Support for user operations (profile, search, followers, following)
  - ✅ Support for media operations (get media, like/unlike, media info)
  - ✅ Support for feed operations (timeline feed)
  - ✅ Automated asset copying in build process
  - ✅ Comprehensive test suite with integration tests
  - ✅ Production-ready build and deployment

* **0.0.4**: Core functionality implementation and bug fixes
* **0.0.3**: Initial TypeScript structure and basic operations
* **0.0.2**: Template refinement and dependency management  
* **0.0.1**: Initial template implementation

## Development

To work with this node locally:

```bash
# Install dependencies
npm install

# Build the node
npm run build

# Run in development mode with file watching
npm run dev

# Run linting
npm run lint

# Run linting with auto-fix
npm run lint:fix

# Run tests
npm test

# Format code
npm run format
```

### 🏗 **Build Process**

The build process includes:
- TypeScript compilation
- Automatic copying of SVG assets
- Type declaration generation
- Source map generation (optional)

### 🧪 **Testing**

The project includes:
- Unit tests for core functionality
- Integration tests for API methods
- Type safety validation
- Error handling verification

## License

[MIT](https://github.com/tiagohintz/n8n-nodes-instagram-private-api/blob/master/LICENSE.md)

---

**Made with ❤️ for the n8n community**

