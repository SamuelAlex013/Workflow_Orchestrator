# n8n Nodes: Zep Integration

[![n8n community node](https://img.shields.io/badge/n8n-community_node-brightgreen.svg)](https://n8n.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Supercharge your n8n workflows with long-term memory for your AI agents and assistants. This community node provides a complete integration with the powerful **Zep Cloud v3 API**, an open-source platform designed to give your AI a persistent memory and a rich understanding of its interactions.

As the official Zep nodes are now deprecated, this community-built node serves as a powerful, modern replacement, unlocking the full potential of Zep's latest features.

**Zep** is more than just a chat history log; it's a sophisticated memory layer that:
-   🧠 **Remembers and Summarizes:** Automatically creates summaries of conversations, allowing your AI to recall context from days, weeks, or months ago.
-   🕸️ **Builds Knowledge Graphs:** Extracts entities (people, products, places) and their relationships from conversations and documents, creating a knowledge graph that evolves over time.
-   🔍 **Enables Powerful Search:** Go beyond simple vector search with advanced, context-aware retrieval over conversation history and knowledge graphs.

This node is your key to building truly intelligent, personalized, and stateful AI applications directly within n8n.

## Table of Contents

-   [Key Features](#key-features)
-   [Installation Guide](#installation-guide)
    -   [n8n Cloud](#n8n-cloud)
    -   [n8n Self-Hosted (Docker)](#n8n-self-hosted-docker)
    -   [n8n Desktop](#n8n-desktop)
-   [Credentials Setup](#credentials-setup)
-   [Operations Reference (All Endpoints Explained)](#operations-reference-all-endpoints-explained)
    -   [👤 User](#-user)
    -   [💬 Thread](#-thread)
    -   [🕸️ Graph](#️-graph)
    -   [📍 Node](#-node)
    -   [↔️ Edge](#️-edge)
    -   [🎬 Episode](#-episode)
    -   [🏷️ Entity Type](#️-entity-type)
    -   [⏱️ Session](#️-session)
-   [Example Workflow: A Simple Memory-Powered Chatbot](#example-workflow-a-simple-memory-powered-chatbot)
-   [Compatibility](#compatibility)
-   [Contributing](#contributing)
-   [License](#license)

## Key Features

-   **Full Zep v3 API Coverage:** Complete control over Users, Threads, Graphs, Nodes, Edges, Episodes, and Sessions.
-   **Effortless User Management:** Create and manage users to associate memories and knowledge with specific individuals.
-   **Advanced Conversation Handling:** Add messages individually or in batches, and retrieve rich, summarized context for your AI prompts.
-   **Knowledge Graph Mastery:** Ingest unstructured text or structured data to automatically build a knowledge graph.
-   **Powerful Semantic Search:** Utilize advanced search and reranking capabilities to find the most relevant information in your AI's memory.


## Installation

### n8n Cloud
If you’re using n8n Cloud, installing community nodes is the simplest:

1.  From the n8n canvas, open the nodes panel by clicking the **+** button.
2.  Search for **Zep v3** in the community nodes section.
3.  Click **Install node** to add the Zep node to your instance.

> **Note:** On n8n Cloud, instance owners can choose to hide community nodes. If you don't see the node, please ensure the installation of community nodes is enabled in your Cloud Admin Panel.

### Self-Hosted n8n / n8n Desktop
To install the Zep community node from the n8n Editor UI:

1.  Open your n8n instance.
2.  Go to **Settings > Community Nodes**.
3.  Select **Install**.
4.  Enter the npm package name: `n8n-nodes-zep`.
5.  Agree to the risks of using community nodes and select **Install**.
6.  The node will be installed, and your instance will restart. It is now available to use in your workflows.

### Self-Hosted with Docker
For a permanent installation in a Docker environment, add the node as an environment variable:

1.  Stop your n8n container.
2.  Open your `docker-compose.yml` file (or the command you use to run n8n).
3.  In the `environment:` section for your n8n service, add the following line:
    ```yaml
    - N8N_CUSTOM_EXTENSIONS=n8n-nodes-zep
    ```
    *If you have other community nodes listed in `N8N_CUSTOM_EXTENSIONS`, add this one to the comma-separated list.*
4.  Save the file and restart your n8n container: `docker-compose up -d`.

## Credentials Setup

To connect to Zep, you need an API key.

1.  **Get a Zep API Key:**
    -   Sign up for a free account at [Zep Cloud](https://cloud.getzep.com/).
    -   From your project dashboard, generate a new API Key and copy it.

2.  **Add Credentials to n8n:**
    -   In n8n, go to the **Credentials** section from the left-hand menu.
    -   Click **Add credential**, search for `Zep API`, and select it.
    -   Paste your API key into the `API Key` field.
    -   Click **Save**.

You're all set! The Zep node will now be authenticated.

## Operations Reference (All Endpoints Explained)

This node gives you access to the entire Zep v3 API. Operations are grouped by resource type.

<details>
<summary><b>👤 User</b></summary>

Manages users to associate them with memories and knowledge graphs.

| Operation         | Description                                                      |
| ----------------- | ---------------------------------------------------------------- |
| **Add User**      | Creates a new user in Zep.                                       |
| **Delete User**   | Deletes a user by their ID.                                      |
| **Get User**      | Retrieves a user's details by their ID.                          |
| **Get User Node** | Gets the specific Knowledge Graph node associated with a user.   |
| **Get User Threads**| Lists all conversation threads for a specific user.              |
| **Get Users**     | Returns a list of all users in your project.                     |
| **Update User**   | Updates a user's information, such as email or metadata.         |

---

### Add User
Creates a new user.

| Parameter   | Description                              | Example Value                                       |
| ----------- | ---------------------------------------- | --------------------------------------------------- |
| **User ID** | A unique identifier for the user.        | `user-jane-doe-456`                                 |
| Email       | The user's email address.                | `jane.doe@example.com`                              |
| First Name  | The user's first name.                   | `Jane`                                              |
| Last Name   | The user's last name.                    | `Doe`                                               |
| Metadata    | A JSON object for storing extra data.    | `{"subscription_tier": "premium", "internal_id": 987}` |

### Get User / Delete User
Retrieves or deletes a user.

| Parameter   | Description                       | Example Value       |
| ----------- | --------------------------------- | ------------------- |
| **User ID** | The unique identifier of the user. | `user-jane-doe-456` |

</details>

<details>
<summary><b>💬 Thread</b></summary>

Manages conversational threads, which are ordered sequences of messages.

| Operation                           | Description                                                                     |
| ----------------------------------- | ------------------------------------------------------------------------------- |
| **Add Messages to a Thread**        | Appends one or more messages to a conversation thread.                          |
| **Add Messages to a Thread in Batch**| Efficiently adds a large number of messages in a single API call.                 |
| **Delete Thread**                   | Deletes an entire conversation thread.                                          |
| **Get Messages of a Thread**        | Retrieves the history of messages for a given thread.                           |
| **Get Threads**                     | Lists all conversation threads in your project, with pagination.                |
| **Get User Context**                | Extracts relevant summaries and facts from a thread to use in an LLM prompt.    |
| **Start a New Thread**              | Creates a new conversation thread and associates it with a user.                |

---

### Start a New Thread
Creates a new conversation thread.

| Parameter   | Description                                 | Example Value           |
| ----------- | ------------------------------------------- | ----------------------- |
| **Thread ID** | A unique identifier for the conversation.   | `convo-abc-123`         |
| **User ID**   | The ID of the user this thread belongs to.  | `user-jane-doe-456`     |

### Add Messages to a Thread
Adds messages to an existing conversation.

| Parameter    | Description                                                     | Example Value                                                                    |
| ------------ | --------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Thread ID**  | The identifier of the thread to add messages to.                | `convo-abc-123`                                                                  |
| **Messages**   | An array of message objects to add.                             | `[{"role": "user", "role_type": "user", "content": "Hello, can you help me?"}]`  |

### Get User Context
Retrieves a contextual summary of the conversation, perfect for providing history to an LLM.

| Parameter   | Description                                      | Example Value   |
| ----------- | ------------------------------------------------ | --------------- |
| **Thread ID** | The identifier of the thread to get context from. | `convo-abc-123` |
| Min Rating  | Filters facts by their relevance rating (0.0 to 1.0). | `0.7`           |
| Mode        | `summary` (default) or `basic` for lower latency.   | `summary`       |

</details>

<details>
<summary><b>🕸️ Graph</b></summary>

Manages temporal knowledge graphs, which store entities and their relationships.

| Operation               | Description                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------- |
| **Add Data**            | Adds an "episode" (a piece of text or JSON) to the graph for automatic fact extraction.    |
| **Add Data in Batch**   | Adds multiple episodes at once.                                                          |
| **Add Fact Triple**     | Manually creates a relationship (`edge`) between two entities (`nodes`).                   |
| **Clone Graph**         | Creates an exact copy of an existing graph.                                              |
| **Create Graph**        | Creates a new, empty knowledge graph.                                                    |
| **Delete Graph**        | Deletes a specified knowledge graph.                                                     |
| **Get Graph**           | Retrieves metadata for a specific graph.                                                 |
| **List All Graphs**     | Lists all graphs in your project.                                                        |
| **Search Graph**        | Performs a powerful semantic search over the graph's nodes, edges, or episodes.          |
| **Update Graph**        | Modifies the name or description of a graph.                                             |

---

### Create Graph
Initializes a new knowledge graph.

| Parameter     | Description                              | Example Value                     |
| ------------- | ---------------------------------------- | --------------------------------- |
| **Graph ID**    | A unique identifier for the graph.       | `product-knowledge-base`          |
| Graph Name    | A human-readable name for the graph.     | `Product Knowledge Base`          |
| Description   | A description of the graph's purpose.    | `Contains all product documentation` |

### Add Data
Adds unstructured data to the graph for Zep to process.

| Parameter          | Description                                           | Example Value                           |
| ------------------ | ----------------------------------------------------- | --------------------------------------- |
| **Data**           | The text or JSON data to add to the graph.            | `"The new QuantumLeap X1 model..."`   |
| **Data Type**      | The type of data being added (`text`, `json`, `message`). | `text`                                  |
| Graph ID           | The ID of the graph to add data to.                   | `product-knowledge-base`                |
| User ID            | Alternatively, the user's graph to add data to.       | `user-jane-doe-456`                     |

### Search Graph
Searches the knowledge graph for relevant information.

| Parameter           | Description                                                        | Example Value                                        |
| ------------------- | ------------------------------------------------------------------ | ---------------------------------------------------- |
| **Search Query**    | The natural language query to search for.                          | `QuantumLeap X1 release date and features`           |
| Graph ID / User ID  | The graph to search within.                                        | `product-knowledge-base`                             |
| Limit               | The maximum number of results to return.                           | `5`                                                  |
| Scope               | What to search for: `edges` (relationships), `nodes`, or `episodes`. | `episodes`                                           |
| Reranker            | Method to re-rank results for relevance (e.g., `rrf`, `mmr`).      | `rrf`                                                |
| Search Filters      | JSON object to filter results by metadata.                         | `{"node_labels": ["Product"]}`                       |

</details>

<details>
<summary><b>📍 Node</b></summary>

Manages individual entities (nodes) within a knowledge graph.

| Operation                    | Description                                         |
| ---------------------------- | --------------------------------------------------- |
| **Get Entity Edges for a Node** | Retrieves all relationships connected to a specific node. |
| **Get Episodes for a Node**  | Retrieves all data episodes where this node was mentioned. |
| **Get Graph Nodes**          | Lists all nodes within a specific graph.            |
| **Get Node**                 | Retrieves a single node by its UUID.                |
| **Get User Nodes**           | Lists all nodes within a specific user's graph.     |

</details>

<details>
<summary><b>↔️ Edge</b></summary>

Manages relationships (edges) between nodes in a knowledge graph.

| Operation        | Description                                  |
| ---------------- | -------------------------------------------- |
| **Get Edge**     | Retrieves a single edge by its UUID.         |
| **Get Graph Edges**| Lists all edges within a specific graph.     |
| **Get User Edges** | Lists all edges within a specific user's graph.|
| **Delete Edge**  | Deletes an edge by its UUID.                 |

</details>

<details>
<summary><b>🎬 Episode</b></summary>

Manages "episodes," which are the raw pieces of data ingested into the graph.

| Operation                                     | Description                                                                 |
| --------------------------------------------- | --------------------------------------------------------------------------- |
| **Delete Episode**                            | Deletes an episode by its UUID.                                             |
| **Get Episode**                               | Retrieves a single episode by its UUID.                                     |
| **Get Graph Episodes**                        | Lists all episodes within a specific graph.                                 |
| **Get User Episodes**                         | Lists all episodes within a specific user's graph.                          |
| **Return Any Nodes and Edges Mentioned in an Episode** | Extracts all entities and relationships identified within an episode. |

</details>

<details>
<summary><b>🏷️ Entity Type</b></summary>

Manages the schema for entity and edge types for more structured knowledge graph management.

| Operation         | Description                                       |
| ----------------- | ------------------------------------------------- |
| **Get Entity Types** | Retrieves the defined entity and edge types.    |
| **Set Entity Types** | Defines or updates the schema for entity and edge types. |

</details>

<details>
<summary><b>⏱️ Session</b></summary>

Manages short-term conversation sessions. This is distinct from long-term memory Threads.

| Operation             | Description                                          |
| --------------------- | ---------------------------------------------------- |
| **Add Session Messages** | Adds messages to a short-term session.               |
| **Create Session**      | Creates a new session associated with a user.        |
| **Get Session**         | Retrieves details about a specific session.          |
| **Get Session Messages**| Retrieves the message history for a session.         |
| **List Sessions**       | Lists all recent sessions.                           |

</details>

## Example Workflow: A Simple Memory-Powered Chatbot

This workflow demonstrates how to create a chatbot that remembers the conversation.

 <!-- Replace with a real image of the workflow -->

**Nodes & Logic:**

1.  **Webhook Node:**
    -   Receives a POST request with a `userId` and a `message`.
    -   Example payload: `{ "userId": "user-jane-doe-456", "message": "What was the last thing I asked about?" }`

2.  **Zep v3 Node (Add Message):**
    -   **Resource:** `Thread`
    -   **Operation:** `Add Messages to a Thread`
    -   **Thread ID:** Use an expression to create a consistent thread ID, e.g., `{{ $json.body.userId }}-main`. Zep automatically creates the thread on the first message.
    -   **Messages:**
        -   **Role:** `user`
        -   **Role Type:** `user`
        -   **Content:** `{{ $json.body.message }}`

3.  **Zep v3 Node (Get Context):**
    -   **Resource:** `Thread`
    -   **Operation:** `Get User Context`
    -   **Thread ID:** `{{ $json.body.userId }}-main` (same as above).
    -   This node will output a `context` field containing a summary and relevant facts.

4.  **OpenAI Node (or any LLM):**
    -   **Model:** `gpt-4-turbo`
    -   **Prompt:**
        ```
        You are a helpful assistant with a perfect memory of past conversations.

        Here is the relevant context from our previous discussions:
        ---
        {{ $json.context }}
        ---

        Based on that context, answer the user's latest question:
        {{ $('Zep v3').item.json.body.message }}
        ```

5.  **Webhook Response Node:**
    -   Returns the AI's generated response to the user.

This simple setup ensures your AI always has the necessary long-term context to provide intelligent, relevant, and personalized answers.

## Compatibility

-   **n8n Version:** `1.0.0` or higher.
-   **Zep API:** Zep Cloud v3 API.

## Contributing

This project was created by **MTM Suhail** to support the n8n community. Contributions, feature requests, and bug reports are highly welcome. Please open an issue or submit a pull request on the [GitHub repository](https://github.com/mtmsuhail/n8n-nodes-zep).
