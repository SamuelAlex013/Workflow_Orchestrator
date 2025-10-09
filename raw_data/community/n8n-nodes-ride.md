![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-ride

This is an n8n community node. It lets you use [Ride with GPS](https://ridewithgps.com) in your n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

### Ride with GPS

[Ride with GPS](https://ridewithgps.com) is a comprehensive cycling platform that allows users to plan routes, track rides, organize events, and share their cycling adventures with a community of riders. The platform offers GPS tracking, route planning tools, performance analytics, and social features for cyclists of all levels.

This custom node enables you to integrate and leverage your Ride with GPS data within n8n workflows, allowing you to automate data processing, analysis, and integration with other services and platforms.

## Use Cases

Automatically process Ride with GPS data in n8n, connect with other nodes, and enable analysis, recording, and content generation.

🚴‍♀️ **Finish your ride and instantly auto-post beautiful summaries with route maps to Instagram, Twitter, and Strava!** No more manual uploads.

🥾 **Hiking data flows automatically to your Notion database and then shares highlights on Facebook!** Elevation data and scenic waypoints included.

🏍️ **Motorcycle adventures auto-backup to cloud storage and generate travel journals!** Preserve every memorable journey forever.

🚗 **Family road trips automatically create daily logs and email them to grandparents!** Real-time journey sharing made effortless.

✍️ **City exploration tracks become blog drafts automatically!** Extract visited spots and route maps for instant content creation.

---

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This node supports the following resources and operations:

### User

- **Get Current**: Retrieve information about the currently authenticated user

### Events

- **Get Event**: Retrieve details of a specific event by ID (including associated routes and organizer info)
- **Get Events**: Retrieve a paginated list of events owned by the authenticated user

### Routes

- **Get Route**: Retrieve details of a specific route by ID (including track points, course points, and points of interest)
- **Get Routes**: Retrieve a paginated list of routes owned by the authenticated user

### Trips

- **Get Trip**: Retrieve details of a specific trip by ID (including track points and comprehensive trip statistics)
  - **Data Processing Options**:
    - **Sanitize Track Points**: Remove GPS noise and speed outliers using statistical analysis for cleaner data
    - **Normalize Track Points**: Optimize data size by consolidating stationary points and reducing redundancy (typical 30-70% size reduction)
  - **Multiple Output Formats**: Choose from the following formats (multiple selections allowed):
    - **Raw Data**: Original Ride with GPS data in JSON format with complete trip information and statistics
    - **GeoJSON**: RFC 7946 compliant format converted from Raw Data, optimized for n8n workflow processing and geographic data analysis
    - **KML**: Keyhole Markup Language format for Google Earth and GPS applications
    - **GPX**: GPS Exchange Format compatible with most GPS devices and mapping software
    - **Investigation Points**: Collection of key waypoints for comprehensive route analysis, designed for querying external APIs (e.g., reverse geocoding for location names)
    - **Image**: Static map visualization using Google Maps Static API (requires API key)
- **Get Trips**: Retrieve a paginated list of trips owned by the authenticated user

### Sync

- **Sync**: Retrieve changes to routes and/or trips since a specific datetime (specialized for data synchronization)

## Credentials

To use this node, you need to authenticate with Ride with GPS using your service account credentials.

### Prerequisites

1. Sign up for a [Ride with GPS account](https://ridewithgps.com)

### Authentication Setup

1. In n8n, create new credentials of type "Ride API"
2. Enter your Ride with GPS service account email address and password
3. **Optional**: Enter your Google Maps API key for static map image generation
   - This is only required if you want to use the Image output format for trips
   - You can use all other features without a Google Maps API key
4. Configure the base URL (defaults to `https://ridewithgps.com`)

### Google Maps API Setup (Optional)

To use the static map image generation feature:

1. Get a Google Maps API key from the [Google Cloud Console](https://console.cloud.google.com/)
2. Enable the "Maps Static API" for your project
3. Add the API key to your Ride API credentials in n8n
4. **Note**: This is completely optional - all other node features work without it

## Compatibility

- **Minimum n8n version**: 1.0.0
- **Node.js version**: 20.15 or higher
- **Tested with**: n8n v1.x

## Usage

### Basic Examples

**Get Current User Information:**

- Select Resource: User
- The node will automatically fetch the current user's profile information

**List Your Routes:**

- Select Resource: Routes
- Select Operation: Get Routes
- Optionally specify a page number for pagination

**Get Specific Route Details:**

- Select Resource: Routes
- Select Operation: Get Route
- Enter the Route ID

**Get Trip with Multiple Output Formats:**

- Select Resource: Trips
- Select Operation: Get Trip
- Enter the Trip ID
- Select Output Formats: Choose any combination of the following:
  - **Raw Data**: Original Ride with GPS data in complete JSON format
  - **GeoJSON**: Standardized geographic format, ideal for n8n workflow processing
  - **KML**: Compatible with Google Earth and GPS applications
  - **GPX**: Universal GPS format for devices and mapping software
  - **Investigation Points**: Key waypoints for external API queries (reverse geocoding, location analysis)
  - **Image**: Visual map representation with route and markers (requires Google Maps API key)

![Static Map Example](docs/StaticMap.png)
_Example of generated static map showing trip route with start (S) and end (E) markers_

**Sync Changes:**

- Select Resource: Sync
- Enter a "Since Datetime" in ISO8601 format (e.g., `2024-01-01T00:00:00Z`)
- Select Asset Types (Routes, Trips, or both)
- This is useful for maintaining synchronized copies of user data

### Pagination

Most list operations support pagination through the "Page Number" parameter. The response will include metadata about pagination, including total record count and links to additional pages.

### Data Synchronization

The Sync operation is particularly useful for:

- Initial full synchronization (use `1970-01-01T00:00:00Z` as since datetime)
- Incremental updates (use the timestamp from previous sync)
- Maintaining backup copies of user's route and trip libraries

## Changelog

For detailed version history and release notes, see [CHANGELOG.md](CHANGELOG.md).

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [Ride with GPS API Documentation](https://ridewithgps.com/api)
- [Ride with GPS Platform](https://ridewithgps.com)

## License

This project is licensed under the MIT License.
