# n8n-nodes-yourtextguru

This is an n8n community node. It lets you use YourTextGuru in your n8n workflows.

This API enables developers to integrate SEO optimization tools into their applications, allowing for content analysis, keyword research, and more.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)   
[Compatibility](#compatibility)  
[Resources](#resources)  
[Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

Base URL : https://yourtext.guru/api/v2/

1. Status Endpoints
Endpoints for monitoring API availability and usage.
________________________________________
GET /status
Description:
Check the current operational status of the API.
Parameters:
None
________________________________________
GET /consumption/openai
Description:
Retrieve information about OpenAI-related usage and consumption.
Parameters:
•	lastId (integer) – Retrieve consumption entries after this ID (for pagination or incremental updates).

2. Project Endpoints
Endpoints for managing SEO projects, including creation, retrieval, and deletion.
________________________________________
GET /projects
Description:
Retrieve a list of all projects associated with the authenticated user.
Parameters:
None
________________________________________
POST /projects
Description:
Create a new project.
Parameters:
•	name (string) – Name of the project.
•	host (string) – Associated domain or host (e.g., example.com).
________________________________________
GET /projects/{projectId}
Description:
Retrieve detailed information about a specific project.
Parameters:
•	projectId (integer) – ID of the project to retrieve.
________________________________________
POST /projects/{projectId}
Description:
Update the name or host of an existing project.
Parameters:
•	projectId (integer) – ID of the project to update.
•	name (string) – New name for the project.
•	host (string) – New host or domain for the project.
________________________________________
DELETE /projects/{projectId}
Description:
Delete a specific project by its ID.
Parameters:
•	projectId (integer) – ID of the project to delete.

3. Group Endpoints
Endpoints for organizing guides into groups and generating topical meshes within a project.
________________________________________
GET /projects/{projectId}/groups
Description:
Retrieve all groups within a specific project.
Parameters:
•	projectId (integer) – ID of the project.
________________________________________
POST /projects/{projectId}/groups
Description:
Create a new group within a project.
Parameters:
•	projectId (integer) – ID of the project.
•	name (string) – Name of the new group.
________________________________________
GET /projects/{projectId}/groups/{groupId}
Description:
Retrieve details of a specific group.
Parameters:
•	projectId (integer) – ID of the project.
•	groupId (integer) – ID of the group.
________________________________________
POST /projects/{projectId}/groups/{groupId}
Description:
Update the name of a specific group.
Parameters:
•	projectId (integer) – ID of the project.
•	groupId (integer) – ID of the group.
•	name (string) – New name for the group.
________________________________________
DELETE /projects/{projectId}/groups/{groupId}
Description:
Delete a specific group from a project.
Parameters:
•	projectId (integer) – ID of the project.
•	groupId (integer) – ID of the group.
________________________________________
POST /projects/{projectId}/groups/{groupId}/guides/add
Description:
Add a list of guide to a group.
Parameters:
•	projectId (integer) – ID of the project.
•	groupId (integer) – ID of the group.
•	guideId (integer) – ID of the guide to add.
________________________________________
POST /projects/{projectId}/groups/{groupId}/guides/remove
Description:
Remove guides from a group.
Parameters:
•	projectId (integer) – ID of the project.
•	groupId (integer) – ID of the group.
•	guideId (integer) – ID of the guide to remove.
________________________________________
GET /projects/{projectId}/groups/{groupId}/topicalMesh
Description:
Retrieve the topical mesh associated with a group.
Parameters:
•	projectId (integer) – ID of the project.
•	groupId (integer) – ID of the group.
________________________________________
POST /projects/{projectId}/groups/{groupId}/topicalMesh
Description:
Generate a topical mesh for a group.
Parameters:
•	projectId (integer) – ID of the project.
•	groupId (integer) – ID of the group.
________________________________________
GET /projects/{projectId}/groups/{groupId}/topicalMesh/wordcloud
Description:
Retrieve a word cloud visualization of the group's topical mesh.
Parameters:
•	projectId (integer) – ID of the project.
•	groupId (integer) – ID of the group.
________________________________________
GET /projects/{projectId}/groups/{groupId}/topicalMesh/paa
Description:
Retrieve "People Also Ask" questions related to the group's topical mesh.
Parameters:
•	projectId (integer) – ID of the project.
•	groupId (integer) – ID of the group.

4. Guide Endpoints
Endpoints related to the creation, retrieval, and analysis of SEO guides.
________________________________________
GET /guides
Description:
Retrieve a list of guides, optionally filtered by project, group, or other attributes.
Parameters:
•	projectId (integer) – ID of the associated project.
•	lastId (integer) – Retrieve guides after this ID (for pagination).
•	lang (string) – Language code (e.g., " en_GB", " fr_FR").
•	apiOnly (integer) – If set to 1, only API-generated guides are returned.
•	groupId (integer) – ID of the associated group.
•	status (string) – Filter by guide status.
________________________________________
POST /guides
Description:
Create a new SEO guide based on a query (keyword or phrase).
Parameters:
•	query (string) – Target keyword or phrase.
•	lang (string) – Language code for the guide.
•	projectId (integer) – ID of the project to associate the guide with.
•	type (string) – Type of guide (, "google" or "bing").
•	groupId (integer) – group ID to associate the guide with.
________________________________________
GET /guides/{guideId}
Description:
Retrieve detailed information about a specific guide.
Parameters:
•	guideId (integer) – ID of the guide to retrieve.
________________________________________
DELETE /guides/{guideId}
Description:
Delete a specific guide by its ID.
Parameters:
•	guideId (integer) – ID of the guide to delete.
________________________________________
GET /guides/{guideId}/paa
Description:
Retrieve "People Also Ask" questions related to the guide's query.
Parameters:
•	guideId (integer) – ID of the guide.
________________________________________
GET /guides/{guideId}/related
Description:
Retrieve keywords and topics related to the guide's query.
Parameters:
•	guideId (integer) – ID of the guide.
________________________________________
POST /guides/{guideId}/check
Description:
Check the SEO quality of a given text against the guide.
Parameters:
•	guideId (integer) – ID of the guide.
•	text (string) – The content to analyze.
________________________________________
GET /guides/{guideId}/serp
Description:
Retrieve SERP (Search Engine Results Page) data related to the guide’s keyword.
Parameters:
•	guideId (integer) – ID of the guide.
________________________________________
GET /guides/{guideId}/brief
Description:
Get the current brief associated with the guide.
Parameters:
•	guideId (integer) – ID of the guide.
________________________________________
POST /guides/{guideId}/brief
Description:
Generate or update the brief for the guide.
Parameters:
•	guideId (integer) – ID of the guide.
________________________________________
GET /guides/{guideId}/brief/analyze
Description:
Retrieve the result of the latest brief analysis.
Parameters:
•	guideId (integer) – ID of the guide.
________________________________________
POST /guides/{guideId}/brief/analyze
Description:
Submit a brief for SEO analysis.
Parameters:
•	guideId (integer) – ID of the guide.
•	requestBody (string) – Text content to analyze.
________________________________________
GET /guides/{guideId}/brief/analyze/{analyzeId}
Description:
Retrieve a specific analysis result by its ID.
Parameters:
•	guideId (integer) – ID of the guide.
•	analyzeId (integer) – ID of the analysis to retrieve.

5. Seo Txl Endpoints
Endpoints for generating and manipulating SEO-optimized text (TXL) based on guide data.
________________________________________
POST /guides/{guideId}/seotxl/auto
Description:
Automatically generate SEO content based on the guide and input text.
Parameters:
•	guide (integer) – ID of the guide.
•	text (string) – Input text to base the generation on.
________________________________________
POST /guides/{guideId}/seotxl/outline
Description:
Generate a structured outline for SEO content.
Parameters:
•	guide (integer) – ID of the guide.
•	text (string) – Input topic or content to guide the outline.
________________________________________
POST /guides/{guideId}/seotxl/questions
Description:
Generate a list of relevant questions based on the guide’s topic.
Parameters:
•	guide (integer) – ID of the guide.
________________________________________
POST /guides/{guideId}/seotxl/rephrase
Description:
Rephrase a given text to improve clarity or SEO performance.
Parameters:
•	guide (integer) – ID of the guide.
•	text (string) – The text to rephrase.
________________________________________
POST /guides/{guideId}/seotxl/create
Description:
Generate custom SEO text with configurable temperature and word limit.
Parameters:
•	guide (integer) – ID of the guide.
•	text (string) – Input prompt or content base.
•	temperature (integer) – Controls creativity (higher = more creative).
•	maxWords (integer) – Maximum number of words in the output.


## Credentials

To get your API key, please refer to [this page](https://yourtext.guru/en/pricing) for pricing and details.
All API requests require authentication. You must include your API key in the request headers:

```
Authorization: Bearer YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your actual API key.

## Compatibility

Tested on n8n Version: 1.100.1

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* For more detailed information, refer to the [official API documentation](https://yourtext.guru/api/v2/documentation)
  If you encounter issues or have questions, please contact the YourText.Guru support team through their support portal.


## Version history

version: 0.1.0


