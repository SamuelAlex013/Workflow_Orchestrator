# n8n-nodes-roundrobin

This is a custom node for [n8n](https://n8n.io/) that allows you to store and retrieve messages in a round-robin fashion, particularly useful for LLM conversation loops with multiple personas.

## Features

- **Store messages** from different roles/personas in a stateful way during workflow execution
- **Enhanced persona profiles** with tone, expertise areas, colors, and system prompts
- **Round counter** tracks conversation turns and allows setting limits
- **Reliable storage** using binary data attachments for persistence
- **LLM platform integrations** with formatting for OpenAI, Anthropic Claude, and Google Gemini
- **System prompt management** for guiding AI behavior
- **Retrieve messages** in various formats (array, object by role, or conversation history for LLMs)
- **Simplify outputs** to create clean, minimal data structures for AI models
- **LLM-ready defaults** pre-configured for ChatGPT-style conversations
- **Clear stored messages** when needed

## Installation

### Local Installation (Development)

1. Clone this repository:
```bash
git clone https://github.com/JamesFincher/n8n-nodes-roundrobin.git
```

2. Navigate to the project directory:
```bash
cd n8n-nodes-roundrobin
```

3. Install dependencies:
```bash
npm install
```

4. Build the project:
```bash
npm run build
```

5. Link the package to your n8n installation:
```bash
npm link
```

6. In your n8n installation directory, link this package:
```bash
cd YOUR_N8N_INSTALLATION_DIRECTORY
npm link n8n-nodes-roundrobin
```

### Global Installation (Production)

To install the node globally, run:

```bash
npm install -g n8n-nodes-roundrobin@0.9.2
```

### Docker Installation

If you're using Docker to run n8n, you can include this custom node by:

1. Creating a custom Dockerfile:
```dockerfile
FROM n8nio/n8n

RUN npm install -g n8n-nodes-roundrobin@0.9.2
```

2. Building your custom image:
```bash
docker build -t n8n-with-roundrobin .
```

3. Running n8n with your custom image:
```bash
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  n8n-with-roundrobin
```

## Usage

### Basic Workflow Example

1. **Initial Setup**: Start by configuring the Round Robin node in "Store" mode.
   - Set the number of spots (default: 3 for User, Assistant, System)
   - Define the roles for each spot with enhanced persona details
   - Configure colors, tones, expertise areas, and system prompts

2. **Storing Messages**: For each message in your workflow:
   - Configure the Round Robin node to "Store" mode
   - Specify which role's spot to store the message (e.g., spot index 0 for "User")
   - Set the input field name that contains the message (default: "output")

3. **Retrieving Messages**: When you need to retrieve the conversation:
   - Configure the Round Robin node to "Retrieve" mode
   - Choose the output format (array, object, or conversation history)
   - Select the target LLM platform (OpenAI, Claude, etc.)
   - Configure system prompt options
   - Enable "Simplify Output" for clean, minimal data

### LLM Conversation Loop Example

Here's a typical workflow for managing multi-persona conversations with LLMs:

1. **Initialize** with the Round Robin in "Clear" mode to start fresh
2. **Store Initial Message** from User (spot index 0)
3. **Loop**:
   - Retrieve the conversation history (format: conversationHistory, platform: openai)
   - Send to LLM for Assistant response
   - Store the Assistant response (spot index 1)
   - Retrieve updated conversation history
   - Process or display the results
   - Store the next user input (spot index 0)
   - Continue the loop

## Node Reference

### Store Mode
- **Number of Spots**: Define how many distinct roles/personas you have (default: 3)
- **Roles**: Configure enhanced persona details:
  - **Name**: Name of the role/persona
  - **Description**: Description of the role/persona
  - **Color**: Visual color indicator for the role
  - **Tone**: Tone of voice (friendly, professional, technical, etc.)
  - **Expertise Areas**: Comma-separated list of expertise domains
  - **System Prompt Template**: Role-specific system instructions
  - **Enabled**: Whether this role should be included in conversations
- **Input Message Field**: Field name containing the message to store (default: "output")
- **Spot Index**: Which spot to store the message in (0-based index)

### Retrieve Mode
- **Output Format**: 
  - `array`: Returns all messages as an array
  - `object`: Groups messages by role name
  - `conversationHistory`: Formats for LLM input (default)
- **LLM Platform**: Format specifically for different AI platforms
  - **OpenAI (ChatGPT)**: Standard OpenAI format with user/assistant/system roles
  - **Anthropic (Claude)**: Claude-specific format with Human/Assistant markers
  - **Google (Gemini)**: Google's conversation format
  - **Generic**: Generic format compatible with most LLMs
- **System Prompt Options**:
  - **Include System Prompt**: Whether to include system instructions
  - **System Prompt Position**: Place at start or end of conversation
- **Simplify Output**: Returns clean, minimal data structures (default: true)
- **Maximum Messages**: Limit the number of messages returned (0 = all)

### Clear Mode
Resets all stored messages while preserving role configurations.

## Important Notes

- Data is stored in workflow memory and will be lost if:
  - The n8n instance is restarted
  - The workflow is updated and redeployed

## Version History

### v0.9.2 - UI Improvements & Round Counter Optimization
- Improved round counter implementation with better error handling
- Enhanced user interface with more intuitive parameter organization
- Added round count information to all output formats
- Further improved storage reliability across workflow executions

### v0.9.1 - Storage Improvements & Round Counter
- Added conversation round counter to track and limit conversation turns
- Made binary storage the default for better persistence across executions
- Improved UI with better organization, hints, and notices
- Enhanced role configuration interface

### v0.8.9 - Code Quality & Project Structure Improvements
- Fixed TypeScript configuration for better development experience
- Added ESLint for code quality assurance
- Improved project structure following n8n community node standards
- Enhanced gitignore patterns for cleaner development
- Fixed type inference issues in storage management

### v0.8.0 - Storage System Refactoring
- Complete refactoring of the storage system for maximum reliability
- Added proper static data handling with namespace isolation for multiple nodes
- Split monolithic code into modular functions for better maintainability
- Improved type safety and error handling throughout the codebase
- Removed redundant serialization for better performance

### v0.7.1 - Critical Data Persistence Fix
- Fixed critical issue with data persistence between node executions
- Improved static data storage by using unique node identifiers
- Fixed type handling for expertise fields
- Optimized data structures to ensure reliable storage

### v0.7.0 - Phase 2: Enhanced Persona System & LLM Integration
- Added rich persona profiles with tone, expertise, and color
- Implemented platform-specific formatting for OpenAI, Claude, and Gemini
- Added system prompt management with positioning options
- Enhanced filtering of messages by role enablement

### v0.6.1 - Storage Reliability Fix
- Fixed critical issue with data persistence between workflow executions
- Implemented robust serialization to ensure messages and roles are properly stored
- Added more thorough type checking and initialization of static data
- Improved error handling for serialization/deserialization

### v0.5.0 - Phase 1 Release
- Fixed storage implementation for reliable persistence
- Added "Simplify Output" option for cleaner data
- Implemented better defaults for LLM use cases
- Improved error handling and debugging
- Added helpful notices and documentation

## License

[MIT](LICENSE)

## Author

James Fincher 