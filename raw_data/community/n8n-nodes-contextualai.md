# n8n-nodes-contextualai

This is an n8n community node. It lets you use Contextual AI in your n8n workflows.

Contextual AI provides enterprise-grade RAG (Retrieval-Augmented Generation) agents, advanced document parsing, intelligent querying, and document reranking capabilities for building sophisticated AI-powered applications.

[Contextual AI](https://contextual.ai) is a platform for building enterprise-grade AI applications with advanced RAG capabilities, while [n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Table of contents

- [Installation on self hosted instance](#installation-self-hosted)
- [Installation on n8n cloud](#installation-n8n-cloud)
- [Operations](#operations)
- [Credentials](#credentials)
- [Compatibility](#compatibility)
- [Usage](#usage)
- [Resources](#resources)
- [Troubleshooting](#troubleshooting)  

## Installation (self-hosted)

To install the Contextual AI community node directly from the n8n Editor UI:

1. Open your n8n instance.
2. Go to **Settings > Community Nodes**
3. Select **Install**.
4. Enter the npm package name: `n8n-nodes-contextualai` to install the latest version.
5. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes and select **Install**
6. The node is now available to use in your workflows.

## Installation (n8n Cloud)

If you're using n8n Cloud, installing community nodes is even simpler:

1. Go to the **Canvas** and open the **nodes panel**.
2. Search for **Contextual AI** in the community node registry.
3. Click **Install node** to add the Contextual AI node to your instance.

> On n8n cloud users can choose not to show verified community nodes. Instance owners can toggle this in the Cloud Admin Panel. To install the Contextual AI node, make sure the installation of verified community nodes is enabled.


## Operations

This node supports a comprehensive range of Contextual AI operations, organized by resource type:

### Agent
- **Create agent**: Create a new Contextual AI RAG agent with datastore and upload documents
  - Configure agent name, description, and datastore settings
  - Upload multiple documents via binary data
  - Support for various document formats (PDF, DOC/DOCX, PPT/PPTX)
  - Automatic document processing and indexing
- **List agents**: Retrieve a list of all agents in your Contextual AI account
  - View agent details and metadata
  - Check agent status and configuration
- **Delete agent**: Remove an agent from your Contextual AI account
  - Permanent deletion of agent and associated data
  - Requires agent ID for confirmation

### Datastore
- **Create datastore**: Create a new datastore for document storage
  - Configure datastore name and settings
  - Set up document storage and indexing
- **Ingest document**: Upload and process documents into a datastore
  - Support for multiple document formats (PDF, DOC/DOCX, PPT/PPTX, HTML)
  - Optional metadata attachment
  - Batch processing capabilities
- **Get document metadata**: Retrieve metadata for a specific document
  - Document information and processing status
  - Metadata and indexing details
- **List datastores**: Retrieve a list of all datastores in your account
  - View datastore details and configuration
  - Check datastore status and document counts

### Query
- **Query agent**: Query existing Contextual AI agents with intelligent retrieval
  - Natural language querying capabilities
  - Optional retrieval-only mode
  - Document readiness checking
  - Contextual response generation
  - Retrieval content inclusion

### Parser  
- **Parse document**: Parse documents using Contextual AI's advanced document parser
  - Support for PDF, DOC/DOCX, PPT/PPTX files
  - Configurable parsing modes (standard)
  - Figure caption extraction (concise/detailed)
  - Document hierarchy preservation
  - Page range selection
  - Returns job ID for status monitoring
- **Parse status**: Check the status of a document parsing job
  - Monitor parsing progress
  - Retrieve parsed results when completed
  - Track job status and file information
- **Parse result**: Get the results of a completed parse job
  - Retrieve parsed content in multiple formats (markdown-document, markdown-per-page, blocks-per-page)
  - Access document metadata and hierarchy information
  - Get structured content blocks with confidence levels and bounding boxes

### Reranker
- **Rerank documents**: Rank documents according to their relevance to a query
  - Instruction-following reranker technology
  - Custom instruction support
  - Metadata integration
  - Relevance scoring and ranking

### LMUnit
- **Run LMUnit**: Evaluate model responses using Contextual AI's scoring system
  - Automated response evaluation
  - Custom unit test criteria
  - Scoring from 1-5 scale
  - Quality assessment and validation

### AI Tools Integration

All Contextual AI node operations can be combined with n8n's AI tools to create powerful workflows.
For example, you can ingest documents into a datastore, create an agent from that information, and then query over the documents for grounded responses and citations.

## Credentials

This node requires a Contextual AI API key for authentication.

### Prerequisites
- Sign up for a free trial of Contextual AI account at [app.contextual.ai](https://app.contextual.ai)
- Obtain your API key from the Contextual AI dashboard

### Setup
1. In n8n, go to **Credentials**
2. Add a new **"Contextual AI API"** credential
3. Enter your API key in the **API Key** field
4. Optionally add a **Name** for easy identification
5. Click **Save** to store the credential

### Authentication Methods

The node supports API key authentication:
- **API Key**: Configure your Contextual AI API key in the n8n credentials section under `ContextualAiApi`
- **Security**: API keys are securely stored and encrypted in n8n's credential system

## Compatibility

This node has been tested with n8n version 1.57.0 and is compatible with:

- **n8n version**: 1.0.0 or later
- **Node.js version**: 20.15 or later
- **Contextual AI API**: Latest version

## Usage

### Getting Started

1. **Set up credentials**: Configure your Contextual AI API key in n8n credentials
2. **Create a workflow**: Start a new workflow in n8n
3. **Add the Contextual AI node**: Insert the Contextual AI node into your workflow
4. **Select an operation**: Choose the desired operation for your use case
5. **Execute the workflow**: Run the workflow to perform the Contextual AI operation

### Creating an Agent with Documents

1. Add the Contextual AI node to your workflow
2. Select **"Agent"** as the resource and **"Create agent"** as the operation
3. Configure your agent settings:
   - **Agent Name**: Give your agent a descriptive name
   - **Description**: Provide a brief description of the agent's purpose
   - **Datastore Name**: Specify the datastore name for document storage
4. Provide documents via binary data (supports multiple files)
5. Configure document processing options if needed
6. Execute to create the agent and upload documents

### Datastore Management

1. **Create a datastore**:
   - Select **"Datastore"** as the resource and **"Create datastore"** as the operation
   - Enter a datastore name
   - Execute to create the datastore and receive the datastore ID

2. **Upload documents**:
   - Select **"Ingest document"** as the operation
   - Provide the datastore ID and document files via binary data
   - Optionally add metadata as JSON
   - Execute to upload and process documents

3. **Using data connectors (Optional)**:
   > **Note**: To use source connectors for your datastore, you need to configure them in the [Contextual AI platform](https://app.contextual.ai) first, then use that datastore in your n8n workflow.
   
   - **Step 1**: Configure connectors in the [Contextual AI platform](https://app.contextual.ai)
     - Go to Datastores → Create → Select "Third-Party Connection"
     - Choose your data source (Google Drive, SharePoint)
     - Authorize and select specific folders to sync
     - Wait for initial sync to complete (status shows "Synced" with green checkmark)
   - **Step 2**: Use the connector datastore in your n8n workflow
     - Copy the datastore ID from the platform
     - Use this ID when creating agents or querying in n8n
     - The datastore will automatically stay in sync with your source data
   - **Benefits**: No manual document uploads, automatic permissions enforcement, real-time data updates

4. **Manage documents**:
   - Use **"List datastores"** to view all datastores
   - Use **"Get document metadata"** to retrieve specific document information

### Querying an Agent

1. Select **"Query"** as the resource and **"Query agent"** as the operation
2. Enter the **Agent ID** and your **Query**
3. Configure query options:
   - Enable **retrieval-only mode** for document search without generation
   - Include **retrieval content text** for context
   - Set **document readiness** checking
4. Execute to get the agent's response

### Document Reranking

1. Select **"Reranker"** as the resource and **"Rerank documents"** as the operation
2. Provide a **Query** and **comma-separated list of documents**
3. Configure reranking options:
   - Add **custom instructions** for ranking criteria
   - Include **metadata** for enhanced ranking
4. Execute to get ranked results with relevance scores

### Response Evaluation

1. Select **"LMUnit"** as the resource and **"Run LMUnit"** as the operation
2. Provide the required inputs:
   - **Original Query**: The question that was asked
   - **Model Response**: The response to evaluate
   - **Unit Test Criteria**: The criteria for evaluation
3. Execute to get a score from 1-5 on the unit test

### Document Parsing

1. Select **"Parser"** as the resource and **"Parse document"** as the operation
2. Provide a document file via binary data
3. Configure parsing options:
   - **Parse Mode**: Choose parsing mode (standard)
   - **Figure Caption Mode**: Choose caption extraction (concise/detailed)
   - **Enable Document Hierarchy**: Preserve document structure
   - **Page Range**: Specify pages to parse (e.g., "0-5")
4. Execute to submit the parse job and receive a job ID
5. Use **"Parse status"** operation with the job ID to monitor progress and retrieve results


### Advanced Workflow Examples

- **Document Processing Pipeline**: Parse documents → Create datastore → Ingest documents → Create agent → Query agent
- **Quality Assurance**: Query agent → Evaluate response with LMUnit
- **Content Optimization**: Rerank documents → Parse top results → Create refined agent
- **Batch Document Processing**: List datastores → Ingest multiple documents → Monitor processing status
- **Agent Management**: List agents → Delete unused agents → Create new agents with updated documents

## Resources

* [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Contextual AI Documentation](https://docs.contextual.ai)
* [Contextual AI API Reference](https://docs.contextual.ai/api-reference)

## Troubleshooting

### Common issues

1. **Authentication errors**
   - Verify your API key is correct and active
   - Check if your Contextual AI account has sufficient permissions
   - Ensure the API key hasn't expired

2. **Agent Not Found**
   - Verify the agent ID format is correct
   - Check if the agent exists in your Contextual AI account
   - Ensure you have access to the agent

3. **Document parsing failures**
   - Verify the document format is supported (PDF, DOC/DOCX, PPT/PPTX)
   - Check file size limits
   - Ensure the document isn't corrupted or password-protected

4. **Query operation failures**
   - Verify the agent ID is correct
   - Check if the agent is ready (documents processed)
   - Review query format and parameters

5. **Reranking errors**
   - Ensure documents are provided in the correct format
   - Check query and document content validity
   - Verify custom instructions are properly formatted

6. **Parse job failures**
   - Verify the job ID format is correct (should be a UUID)
   - Check if the parse job exists and hasn't expired
   - Ensure the original document was valid and supported

7. **Datastore operation failures**
   - Verify datastore ID format is correct (should be a UUID)
   - Check if the datastore exists in your account
   - Ensure you have proper permissions for the datastore

### Getting help

If you encounter issues:
1. Check the [Contextual AI API documentation](https://docs.contextual.ai/api-reference)
2. Review the [n8n Community Nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
3. Open an issue in the [GitHub repository](https://github.com/contextual-ai/n8n-nodes-contextualai)
