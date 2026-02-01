# n8n-nodes-octavehq

This is an n8n community node. It lets you use Octave in your n8n workflows.

Octave is the AI-powered messaging brain for B2B go-to-market teams, helping you articulate your product's value, synthesize customer interaction data, and deploy consistent, effective messaging across all your execution channels. In a world of rapid product innovation, Octave ensures your go-to-market strategy is always on message and impactful.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Resources](#resources)
[Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

The Octave node supports the following operations, categorized by resource:

**Resource: Agent**
*   **List Agents**: List all agents
    *   Corresponds to `GET /api/v2/agents/list`
*   **Build Workspace**: Generate and build a Workspace
    *   Corresponds to `POST /api/v2/agents/workspace/build`
*   **Call Prep**: Generate call prep content including discovery questions, call scripts, and objection handling
    *   Corresponds to `POST /api/v2/agents/call-prep/run`
*   **Enrich Company**: Enrich a company
    *   Corresponds to `POST /api/v2/agents/enrich-company/run`
*   **Enrich Person**: Enrich a Person
    *   Corresponds to `POST /api/v2/agents/enrich-person/run`
*   **Generate Content**: Generate content for a person
    *   Corresponds to `POST /api/v2/agents/generate-content/run`
*   **Run Sequence**: Generate Emails for a person
    *   Corresponds to `POST /api/v2/agents/sequence/run`
*   **Run Prospector**: Find relevant people at a company or lookalike companies
    *   Corresponds to `POST /api/v2/agents/prospector/run`
*   **Qualify Company**: Determine if a company is qualified for a given Product and/or Segment
    *   Corresponds to `POST /api/v2/agents/qualify-company/run`
*   **Qualify Person**: Determine if a person is qualified for a given Product, Persona, and/or Segment
    *   Corresponds to `POST /api/v2/agents/qualify-person/run`

**Resource: Async**
*   **Run Agent Asynchronously**: Triggers an agent to run in the background.
    *   Corresponds to `POST /api/v2/async/agent/run`

**Resource: Competitor**
*   **List Competitors**: Retrieves a list of competitors with optional filtering.
    *   Corresponds to `GET /api/v2/competitor/list`
*   **Get Competitor**: Retrieves a specific competitor by its OId.
    *   Corresponds to `GET /api/v2/competitor/get`
*   **Create Competitor**: Creates a new competitor.
    *   Corresponds to `POST /api/v2/competitor/create`
*   **Update Competitor**: Updates an existing competitor.
    *   Corresponds to `PUT /api/v2/competitor/update`
*   **Generate Competitors**: Generate competitors from source materials using AI.
    *   Corresponds to `POST /api/v2/competitor/generate`

**Resource: Experiment**
*   **Create Experiment**: Creates a new agent experiment for A/B testing different agents.
    *   Corresponds to `POST /api/v2/agents/experiment/create`

**Resource: Persona**
*   **List Personas**: Retrieves a list of personas.
    *   Corresponds to `GET /api/v2/persona/list`
*   **Get Persona**: Retrieves a specific persona by its OId.
    *   Corresponds to `GET /api/v2/persona/get`
*   **Create Persona**: Creates a new persona.
    *   Corresponds to `POST /api/v2/persona/create`
*   **Update Persona**: Updates an existing persona.
    *   Corresponds to `PUT /api/v2/persona/update`
*   **Generate Personas**: Generate personas from source materials using AI.
    *   Corresponds to `POST /api/v2/persona/generate`

**Resource: Playbook**
*   **List Playbooks**: Retrieves a list of playbooks.
    *   Corresponds to `GET /api/v2/playbook/list`
*   **Get Playbook**: Retrieves a specific playbook by its OId.
    *   Corresponds to `GET /api/v2/playbook/get`
*   **Create Playbook**: Creates a new playbook.
    *   Corresponds to `POST /api/v2/playbook/create`
*   **Update Playbook**: Updates an existing playbook.
    *   Corresponds to `PUT /api/v2/playbook/update`

**Resource: Product**
*   **List Products**: Retrieves a list of products.
    *   Corresponds to `GET /api/v2/product/list`
*   **Get Product**: Retrieves a specific product by its OId.
    *   Corresponds to `GET /api/v2/product/get`
*   **Create Product**: Creates a new product.
    *   Corresponds to `POST /api/v2/product/create`
*   **Update Product**: Updates an existing product.
    *   Corresponds to `PUT /api/v2/product/update`
*   **Generate Products**: Generate products from source materials using AI.
    *   Corresponds to `POST /api/v2/product/generate`

**Resource: Proof Point**
*   **List Proof Points**: Retrieves a list of proof points with optional filtering.
    *   Corresponds to `GET /api/v2/proof-point/list`
*   **Get Proof Point**: Retrieves a specific proof point by its OId.
    *   Corresponds to `GET /api/v2/proof-point/get`
*   **Create Proof Point**: Creates a new proof point.
    *   Corresponds to `POST /api/v2/proof-point/create`
*   **Update Proof Point**: Updates an existing proof point.
    *   Corresponds to `PUT /api/v2/proof-point/update`
*   **Generate Proof Points**: Generate proof points from source materials using AI.
    *   Corresponds to `POST /api/v2/proof-point/generate`

**Resource: Reference**
*   **List References**: Retrieves a list of references.
    *   Corresponds to `GET /api/v2/reference/list`
*   **Get Reference**: Retrieves a specific reference by its OId.
    *   Corresponds to `GET /api/v2/reference/get`
*   **Create Reference**: Creates a new reference.
    *   Corresponds to `POST /api/v2/reference/create`
*   **Update Reference**: Updates an existing reference.
    *   Corresponds to `PUT /api/v2/reference/update`
*   **Generate References**: Generate references from source materials using AI.
    *   Corresponds to `POST /api/v2/reference/generate`

**Resource: Segment**
*   **List Segments**: Retrieves a list of segments with optional filtering.
    *   Corresponds to `GET /api/v2/segment/list`
*   **Get Segment**: Retrieves a specific segment by its OId.
    *   Corresponds to `GET /api/v2/segment/get`
*   **Create Segment**: Creates a new segment.
    *   Corresponds to `POST /api/v2/segment/create`
*   **Update Segment**: Updates an existing segment.
    *   Corresponds to `PUT /api/v2/segment/update`
*   **Generate Segments**: Generate segments from source materials using AI.
    *   Corresponds to `POST /api/v2/segment/generate`

**Resource: Use Case**
*   **List Use Cases**: Retrieves a list of use cases.
    *   Corresponds to `GET /api/v2/use-case/list`
*   **Get Use Case**: Retrieves a specific use case by its OId.
    *   Corresponds to `GET /api/v2/use-case/get`
*   **Create Use Case**: Creates a new use case.
    *   Corresponds to `POST /api/v2/use-case/create`
*   **Update Use Case**: Updates an existing use case.
    *   Corresponds to `PUT /api/v2/use-case/update`
*   **Generate Use Cases**: Generate use cases from source materials using AI.
    *   Corresponds to `POST /api/v2/use-case/generate`

## Credentials

Get your API key from the Octave settings page. We recommend naming the credentials with the Workspace that the API key is associated with.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Library Overview](https://youtu.be/UyU1tDuRE58)
* [Playbooks Overview](https://youtu.be/SINDvLIfRa8)
* [Agents Overview](https://www.youtube.com/watch?v=oExCRibGjAU)
* [Octave + Clay Overview](https://www.youtube.com/watch?v=JjYLBddEn7A)


## Version history
* 0.1.1 - Octave <> N8N. Let the games begin!
* 1.0.1 - Add `x-request-source` header to indicate request came from n8n
* 1.0.2 - Add Credentials test + make Octave node usable by AI
* 1.1.0 - Added Competitor, Segment, and Experiment resources; Added Call Prep agent; Removed Personalize Template agent; Improved modular architecture
* 1.1.1 - Uses IHttpRequestOptions instead of deprecated IRequestOptions
* 1.1.2 - Uses httpRequestWithAuthentication instead of httpRequest to be more secure and maintainable
* 1.2.0 - Removed List API Keys endpoint
* 1.2.1 - Rebuild to remove deprecated API files from build
* 1.3.0 - Major expansion: Added full CRUD support (create, update, generate) for all resources; Added new Proof Point resource; Enhanced UX with native collection inputs for generate operations; Improved agent field ordering with LinkedIn Profile prioritization; Enhanced runtime context handling for sequences
* 1.3.1 - Fixed UI issue in generate operations where "Add Source" button was not displaying Type and Value fields properly
* 1.3.2 - Update Playbook types
