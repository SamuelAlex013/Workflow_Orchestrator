![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-groner

This repository contains custom nodes for integrating n8n with the Groner API (Solar CRM). The Groner node provides comprehensive functionality to manage leads, projects, tasks, and communications within the Groner CRM system.

---

## 🚀 Main Node

- **Groner**: Primary node for integration with the Groner API, covering all major CRM operations including lead management, project tracking, task creation, and WhatsApp messaging.

## 📋 Available Resources and Operations

### 🔗 Available Resources

| Resource | Description |
|----------|-------------|
| **Contact** | Contact/lead management |
| **Deal** | Deal/project management |
| **Note** | Note/occurrence addition |
| **Tag** | Tag management |
| **Task** | Task creation and search |
| **WhatsApp** | WhatsApp message sending |

### 📊 Operations by Resource

#### **Deal (Deal/Project)**
| Operation | Description | HTTP Method |
|-----------|-------------|-------------|
| **Create** | Creates a new deal (lead/project) in Groner | POST |
| **Search** | Searches deals with advanced filters and pagination | GET |
| **Edit by Property** | Edits specific properties of a deal | PUT |
| **Get Quote** | Gets quotes for a specific deal | GET |
| **Move** | Moves a deal to a different stage | POST |

#### **Contact (Contact)**
| Operation | Description | HTTP Method |
|-----------|-------------|-------------|
| **Edit** | Edits contact information | PUT |
| **Edit by Property** | Edits specific properties of a contact | PUT |

#### **Task (Task)**
| Operation | Description | HTTP Method |
|-----------|-------------|-------------|
| **Create** | Creates a new task | POST |
| **Search** | Searches tasks with filters | GET |

#### **Note (Note)**
| Operation | Description | HTTP Method |
|-----------|-------------|-------------|
| **Add** | Adds a note/occurrence to a deal | POST |

#### **Tag (Tag)**
| Operation | Description | HTTP Method |
|-----------|-------------|-------------|
| **Add** | Adds tags to a deal | POST |

#### **WhatsApp**
| Operation | Description | HTTP Method |
|-----------|-------------|-------------|
| **Send** | Sends WhatsApp message | POST |

---

## 🔧 Prerequisites

Before installing and using this package, ensure you have the following installed on your development machine:

### Required Software
- **[Git](https://git-scm.com/downloads)** - Version control system
- **[Node.js](https://nodejs.org/)** - Version 18.10 or higher
- **[pnpm](https://pnpm.io/)** - Package manager (Version 9.1 or higher)

### n8n Installation
Install n8n globally using pnpm:
```bash
pnpm install n8n -g
```

### System Requirements
- **Node.js**: >=18.10
- **pnpm**: >=9.1
- **n8n-workflow**: Compatible version

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/gronerbr/n8n-nodes-groner.git
cd n8n-nodes-groner
```

### 2. Install Dependencies
```bash
pnpm install
```

### 3. Build the Project
```bash
pnpm build
```
This command will:
- Compile TypeScript files
- Copy custom icons to the distribution folder
- Prepare the package for use

### 4. Development Mode (Optional)
For development with automatic recompilation:
```bash
pnpm dev
```

---

## 🔐 Credentials Configuration

### Setting Up Groner API Credentials

1. **Access n8n Credentials**: In your n8n instance, navigate to Settings → Credentials
2. **Add New Credential**: Click "Add Credential" and select **Groner API**
3. **Configure Credentials**:
   - **Tenant**: Your Groner subdomain (e.g., `mycompany`)
   - **API Key**: Your Groner API authentication key

### Credential Details

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| **Tenant** | String | Yes | Your Groner subdomain identifier | `mycompany` |
| **API Key** | Password | Yes | Your Groner API authentication token | `groner_api_key_123...` |

### API Endpoint Structure
The node automatically constructs API endpoints using your tenant:
```
https://{tenant}.api.groner.app/api/{endpoint}
```

---

## 🎯 How to Use the Groner Node

### Basic Workflow Setup

1. **Add the Node**: Drag and drop the **Groner** node into your n8n workflow
2. **Select Resource**: Choose the desired resource (Deal, Contact, Task, etc.)
3. **Select Operation**: Choose the desired operation from the "Operation" dropdown
4. **Configure Parameters**: Fill in required and optional fields based on the selected operation
5. **Execute**: Run the workflow to process the operation

### Output Format
- **Success**: Returns API response data as JSON
- **Search Operations**: Each returned item becomes an individual n8n item
- **Error Handling**: Errors are displayed in the node execution panel

---

## 📖 Detailed Operation Guide

### 1. Create Deal

Creates a new lead or project in Groner with comprehensive tracking capabilities.

#### Required Fields
- **Name** (`nome`): Full name of the contact
- **Email** (`email`): Contact email address
- **Phone** (`telefone`): Contact phone number
- **Origin Name or ID** (`codOrigem`): Lead origin (loadOptions)

#### Optional Fields
- **Account Value** (`valorConta`): Estimated project value
- **City** (`cidade`): Contact's city
- **Document** (`documento`): CPF or CNPJ number
- **Person Type** (`tipoPessoa`): PF (Individual) or PJ (Company)
- **State** (`uf`): Brazilian state abbreviation
- **Responsible Name or ID** (`responsavelId`): Responsible salesperson (loadOptions)
- **Responsible Email** (`emailResponsavel`): Salesperson email
- **Note** (`nota`): Initial notes about the lead
- **Campaign** (`campanha`): Marketing campaign identifier
- **Advertisement** (`anuncio`): Ad campaign reference
- **Ad Set** (`conjuntoAnuncios`): Ad group identifier
- **Lead Tracking Code** (`codigoLeadTracking`): Tracking code for analytics
- **Trade Name** (`nomeFantasia`): Company trade name (for PJ)
- **Segment** (`segmento`): Business segment classification
- **Deal Type Name or ID** (`tipoProjetoId`): Type of solar project (loadOptions)
- **URL** (`url`): Custom endpoint URL (optional)

#### Example Usage
```json
{
  "nome": "John Doe",
  "email": "john.doe@example.com",
  "telefone": "+5511999999999",
  "codOrigem": "1",
  "cidade": "São Paulo",
  "documento": "123.456.789-00",
  "tipoPessoa": "F",
  "valorConta": 25000,
  "nota": "Interested in residential solar installation"
}
```

### 2. Search Deals

Searches for existing deals with advanced filtering and pagination.

#### Filter Parameters
- **Page Size** (`pageSize`): Items per page (default: 20)
- **Search** (`query`): Text search across deal data
- **Criterio** (`criterio`): Search criteria
- **Filters**:
  - **Deal Type ID** (`dealTypeId`): Filter by project type (loadOptions)
  - **Stage ID** (`stageId`): Filter by sales pipeline stage (loadOptions)
  - **Status ID** (`statusId`): Filter by status (loadOptions)
  - **Responsible Seller ID** (`responsibleSellerId`): Filter by responsible seller (loadOptions)
  - **Responsible Technician ID** (`responsibleTechnicianId`): Filter by responsible technician (loadOptions)
  - **Pre Seller ID** (`preSellerId`): Filter by pre-seller (loadOptions)
- **Additional Fields**:
  - **Lead ID** (`leadId`): Filter by specific lead
  - **Stores IDs** (`storesIds`): Filter by store locations (multiOptions)
  - **Tags IDs** (`tagsIds`): Filter by specific tags (multiOptions)
  - **Origins IDs** (`originsIds`): Filter by origins (multiOptions)
  - **Status History IDs** (`statusHistoryIds`, `nStatusHistoryIds`): Filter by status history (multiOptions)
  - **Order By** (`orderBy`): Sort criteria
  - **Initial Qualification** (`initialQualification`): Initial qualification (0-10)
  - **Final Qualification** (`finalQualification`): Final qualification (0-10)
  - **Indicator** (`indicator`): Performance indicator
  - **Contact Owner ID** (`contactOwnerId`): Filter by contact owner
  - **Campaign** (`campaign`): Filter by campaign
  - **Advertisement** (`advertisement`): Filter by advertisement
  - **Ad Set** (`adSet`): Filter by ad set
- **Location**:
  - **City** (`city`): Filter by city
  - **State** (`state`): Filter by state
- **Financial**:
  - **Initial Power** (`initialPower`): Initial power in kW
  - **Final Power** (`finalPower`): Final power in kW
  - **Initial Value** (`initialValue`): Initial project value
  - **Final Value** (`finalValue`): Final project value
  - **Initial Consumption** (`initialConsumption`): Initial consumption in kWh
  - **Final Consumption** (`finalConsumption`): Final consumption in kWh
- **Dates**:
  - **Start Date** (`startDate`): Start date
  - **End Date** (`endDate`): End date
  - **Initial Closing Forecast Date** (`initialClosingForecastDate`): Initial closing forecast date
  - **Final Closing Forecast Date** (`finalClosingForecastDate`): Final closing forecast date
  - **Initial Proposal Date** (`initialProposalDate`): Initial proposal date
  - **Final Proposal Date** (`finalProposalDate`): Final proposal date
  - **Initial Sale Date** (`initialSaleDate`): Initial sale date
  - **Final Sale Date** (`finalSaleDate`): Final sale date
  - **Initial Loss Date** (`initialLossDate`): Initial loss date
  - **Final Loss Date** (`finalLossDate`): Final loss date

#### Example Usage
```json
{
  "pageSize": 50,
  "query": "solar installation",
  "filters": {
    "stageId": "1",
    "statusId": "2"
  },
  "financial": {
    "initialValue": 10000,
    "finalValue": 50000
  }
}
```

### 3. Add Tags

Adds organizational labels to existing deals.

#### Required Fields
- **Deal ID** (`dealId`): Deal ID
- **Tag IDs** (`tagIds`): Array of tag IDs

#### Example Usage
```json
{
  "dealId": "12345",
  "tagIds": ["1", "2", "3"]
}
```

### 4. Add Note

Adds notes or occurrences to track deal interactions.

#### Required Fields
- **Deal ID** (`dealId`): Deal ID
- **Occurrence** (`ocorrencia`): Note content

#### Optional Fields
- **Mentions** (`marcacoes`): Optional user mentions

#### Example Usage
```json
{
  "dealId": "12345",
  "ocorrencia": "Customer requested quote for 10kW system",
  "marcacoes": "@sales_team"
}
```

### 5. Create Task

Creates tasks linked to deals with assignment capabilities.

#### Required Fields
- **Title** (`titulo`): Task title
- **Type ID** (`tipoId`): Task type identifier (loadOptions)
- **Status ID** (`statusId`): Task status (loadOptions)
- **Project ID** (`projetoId`): Associated deal ID
- **Users IDs** (`usuariosIds`): Assigned user IDs (multiOptions)

#### Optional Fields
- **Description** (`descricao`): Task description
- **Start Date** (`dataInicial`): Task start date (YYYY-MM-DD)
- **Delivery Date** (`dataEntrega`): Task delivery date (YYYY-MM-DD)

#### Example Usage
```json
{
  "titulo": "Follow up call",
  "descricao": "Call customer to discuss proposal",
  "tipoId": "1",
  "statusId": "1",
  "projetoId": 12345,
  "usuariosIds": ["user1", "user2"],
  "dataInicial": "2024-01-15",
  "dataEntrega": "2024-01-20"
}
```

### 6. Search Tasks

Searches for tasks with comprehensive filtering options.

#### Filter Parameters
- **Page Size** (`pageSize`): Items per page (default: 20)
- **Search** (`query`): Text search
- **Additional Fields**:
  - **Lead ID** (`leadId`): Filter by associated lead
  - **Project ID** (`projetoId`): Filter by associated project
  - **Type ID** (`tipoId`): Filter by task type (loadOptions)
  - **Status ID** (`statusId`): Filter by task status (loadOptions)
  - **User ID** (`usuarioId`): Filter by assigned user (loadOptions)
  - **Stores IDs** (`lojasIds`): Filter by store locations (multiOptions)
  - **Order By** (`ordenarPor`): Sort criteria
  - **Start Date** (`dataInicial`): Filter by start date (YYYY-MM-DD)
  - **End Date** (`dataFinal`): Filter by end date (YYYY-MM-DD)
  - **Page Number** (`pageNumber`): Page number

#### Example Usage
```json
{
  "projetoId": 12345,
  "statusId": "1",
  "pageSize": 20,
  "ordenarPor": "dataCriacao"
}
```

### 7. Edit Contact by Property

Updates specific properties of existing contacts.

#### Required Fields
- **Contact ID** (`contactId`): Contact/Lead ID (number)
- **Property** (`propriedade`): Property name to update (loadOptions)
- **Value** (`valor`): New property value

#### Example Usage
```json
{
  "contactId": 12345,
  "propriedade": "email",
  "valor": "new.email@example.com"
}
```

### 8. Edit Deal by Property

Updates specific properties of existing deals.

#### Required Fields
- **Deal ID** (`dealId`): Deal ID (number)
- **Property** (`propriedade`): Property name to update (loadOptions)
- **Value** (`valor`): New property value

#### Example Usage
```json
{
  "dealId": 12345,
  "propriedade": "valorConta",
  "valor": "30000"
}
```

### 9. Send WhatsApp Message

Sends WhatsApp messages through Groner's integrated messaging system.

#### Required Fields
- **Message** (`mensagem`): Message content

#### Optional Fields
- **Lead ID** (`leadId`): Target lead ID (number)
- **Phone** (`celular`): Direct phone number
- **Image URL** (`urlImagem`): Image attachment URL
- **Audio URL** (`urlAudio`): Audio attachment URL
- **Video URL** (`urlVideo`): Video attachment URL
- **Document URL** (`urlDocumento`): Document attachment URL
- **Send to Pre-Seller** (`preVendedor`): Whether to send to Pre-Seller (boolean)
- **Send to Seller** (`vendedor`): Whether to send to Seller (boolean)
- **Send to Technician** (`tecnico`): Whether to send to Technician (boolean)
- **Send to Lead** (`lead`): Whether to send to Lead (boolean)

#### Example Usage
```json
{
  "leadId": 12345,
  "mensagem": "Hello! Here's your solar installation quote.",
  "urlImagem": "https://example.com/quote.pdf",
  "vendedor": true
}
```

### 10. Move Deal

Changes the status/stage of a deal in the sales pipeline.

#### Required Fields
- **Deal ID** (`dealId`): Deal ID
- **Status ID** (`statusId`): New status identifier (loadOptions)

#### Optional Fields
- **Validate Status Available** (`validaStatusDisponivel`): Whether to validate if the status is available (boolean)

#### Example Usage
```json
{
  "dealId": "12345",
  "statusId": "2",
  "validaStatusDisponivel": true
}
```

### 11. Get Deal Quote

Retrieves quotes associated with a specific deal.

#### Required Fields
- **Project ID** (`projetoId`): Deal/Project ID

#### Example Usage
```json
{
  "projetoId": "12345"
}
```

---

## 🔄 Workflow Examples

### Example 1: Process Deals with Content.List

This example shows how to use Content.List to process multiple deals:

```
[Groner: Search Deals] → [Content.List] → [Groner: Edit Deal] → [Result]
```

**Content.List Configuration:**
```
Input Data: {{ $json.data }}
Output Field Name: deal
```

**Edit Deal Configuration:**
```
Resource: Deal
Operation: Edit by Property
Deal ID: {{ $json.deal.id }}
Property: valorConta
Value: {{ $json.deal.valorConta * 1.1 }}
```

### Example 2: Complete Follow-up Workflow

```
[Groner: Search Deals] → [IF] → [Groner: Add Note] → [Groner: Send WhatsApp]
```

**IF Condition:**
```
{{ $json.status === "Em Negociação" }}
```

---

## 🔧 Development Scripts

| Script | Description |
|--------|-------------|
| `pnpm build` | Compiles TypeScript and copies icons |
| `pnpm dev` | Runs TypeScript compiler in watch mode |
| `pnpm lint` | Checks for linting issues |
| `pnpm lintfix` | Automatically fixes linting issues |
| `pnpm format` | Formats code using Prettier |
| `pnpm prepublishOnly` | Builds and lints before publishing |

---

## 📁 Project Structure

```
n8n-nodes-groner/
├── credentials/
│   └── GronerApi.credentials.ts    # API authentication
├── nodes/
│   └── Groner/
│       ├── loadOptions/            # Dynamic options
│       │   ├── getStatuses.ts      # Status options
│       │   ├── getOrigins.ts       # Origin options
│       │   ├── getResponsibles.ts  # Responsible user options
│       │   ├── getDealTypes.ts     # Deal type options
│       │   ├── getTags.ts          # Tag options
│       │   ├── getStores.ts        # Store options
│       │   ├── getEtapas.ts        # Stage options
│       │   ├── getTaskTypes.ts     # Task type options
│       │   ├── getTaskStatuses.ts  # Task status options
│       │   ├── getContactProperties.ts # Contact property options
│       │   └── getDealProperties.ts    # Deal property options
│       ├── Groner.node.ts          # Main node file
│       └── logogroner.svg          # Custom icon
├── package.json                    # Project configuration
├── tsconfig.json                   # TypeScript configuration
└── gulpfile.js                     # Build configuration
```

---

## ⚠️ Important Notes

### API Response Handling
- **Search Operations**: Each item returned by the API becomes an individual n8n item for easy processing
- **Error Handling**: API errors are displayed in the node execution panel with detailed error messages
- **Authentication**: Uses Bearer token authentication with your API key

### Load Options
The node provides dynamic loading of options for various fields:
- **Statuses**: Available deal statuses
- **Origins**: Lead origin sources
- **Responsibles**: Available users/responsible persons
- **Deal Types**: Types of projects/deals
- **Tags**: Available tags/labels
- **Stores**: Store locations
- **Etapas**: Sales pipeline stages
- **Task Types**: Types of tasks
- **Task Statuses**: Task status options
- **Contact Properties**: Available contact properties
- **Deal Properties**: Available deal properties

### Custom Icon
- The node displays the Groner logo if the `logogroner.svg` file is present in the node directory
- The icon is automatically copied during the build process

### Data Validation
- Empty fields are automatically removed from API requests
- Required fields are validated before sending requests
- Date formats should follow YYYY-MM-DD standard
- Arrays are automatically converted to comma-separated strings for API compatibility

### Rate Limiting
- Be aware of Groner API rate limits
- Implement appropriate delays between requests in high-volume workflows

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Reporting Issues
- Use the GitHub issue tracker
- Provide detailed error messages and steps to reproduce
- Include your n8n version and node configuration

### Submitting Pull Requests
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run `pnpm lint` and `pnpm build`
5. Submit a pull request with detailed description

### Development Guidelines
- Follow TypeScript best practices
- Maintain consistent code formatting
- Add appropriate error handling
- Include field validation where necessary

---

## 📄 License

This project is licensed under the [MIT License](LICENSE.md).

---

## 📞 Support

For support and questions:
- **Email**: contato@gronercrm.com.br
- **GitHub Issues**: [Create an issue](https://github.com/gronerbr/n8n-nodes-groner/issues)
- **Documentation**: This README and inline code comments

---

## 🌐 Language Versions

- **[English Version](README.md)** (Current)
- **[Portuguese Version](README_PT.md)**

---

## 🔄 Version History

- **v0.1.18**: Current version with comprehensive CRM operations and updated field structure
- **v0.1.17**: Added WhatsApp messaging capabilities
- **v0.1.16**: Enhanced search and filtering options
- **v0.1.15**: Improved error handling and validation
- **v0.1.14**: Initial release with basic operations

For detailed changelog, see the [GitHub releases](https://github.com/gronerbr/n8n-nodes-groner/releases).
