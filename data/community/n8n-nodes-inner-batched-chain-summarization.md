# n8n-nodes-inner-batched-chain-summarization

This is an n8n community node that provides intelligent batched chain summarization for processing large documents efficiently with built-in rate limiting and pause functionality.

The Batched Chain Summarization node transforms text into concise summaries using multiple strategies (map-reduce, refine, stuff) with intelligent batching to handle large documents while respecting API rate limits through configurable delays between batches.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Configuration](#configuration)
[Usage](#usage)
[Compatibility](#compatibility)
[Resources](#resources)
[Version History](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

```bash
npm install n8n-nodes-inner-batched-chain-summarization
```

## Operations

The node supports three powerful summarization strategies:

### 🗺️ Map-Reduce (Recommended)
**Best for**: Large documents with many chunks
- **Process**: Summarizes each document/chunk individually in parallel batches, then combines all summaries
- **Batching**: Full batching support with configurable delays between batches
- **Scalability**: High - handles large document sets efficiently
- **API Calls**: Most calls (one per document + one combine)

### 🔄 Refine
**Best for**: Documents where order and context matter
- **Process**: Iteratively refines summary by processing each subsequent document against the existing summary
- **Batching**: Partial batching support with delays between refinement batches
- **Scalability**: Medium - good for contextual content
- **API Calls**: Moderate (one per document)

### 📦 Stuff
**Best for**: Small documents that fit within model context limits
- **Process**: Combines all documents into a single prompt for one LLM call
- **Batching**: No batching (single call)
- **Scalability**: Low - limited by context window
- **API Calls**: Minimal (only one)

## Configuration

### Data Input Modes
- **Use Node Input (JSON)**: Process JSON data from the previous node
- **Use Node Input (Binary)**: Process binary files from the previous node
- **Use Document Loader**: Use a dedicated document loader sub-node with advanced options

### Chunking Strategies
- **Simple**: Built-in recursive character text splitter with configurable size and overlap
- **Advanced**: Use an external text splitter sub-node for complex requirements
- **None**: Process documents without chunking (document loader mode only)

### Batching & Rate Limiting
- **Batch Size**: Number of documents to process simultaneously (default: 5, range: 1-1000)
- **Delay Between Batches**: Milliseconds to wait between batches (default: 0, max: 10 minutes)
- **Input Validation**: Automatic bounds checking prevents infinite loops and invalid configurations

### Custom Prompts
Full customization support for all summarization methods:
- **Map-Reduce**: Individual summary prompt + combine prompt
- **Refine**: Initial prompt + refinement prompt
- **Stuff**: Single summarization prompt

## Usage

### Basic Workflow
1. **Connect your data source** (previous node, binary files, or document loader)
2. **Choose summarization method** based on your document size and requirements
3. **Configure batching** to respect your API provider's rate limits
4. **Set chunking strategy** if processing large documents
5. **Customize prompts** if needed for specific summarization requirements

### Rate Limiting Best Practices

Start with conservative settings and adjust based on your API provider:

```
Batch Size: 2-3 documents
Delay: 1000-2000ms between batches
```

The pause functionality helps prevent rate limit violations during processing.

### Example Configurations

**For Large Document Sets:**
- Method: Map-Reduce
- Batch Size: 5
- Delay: 1000ms
- Chunking: Simple (1000 chars, 200 overlap)

**For Narrative Content:**
- Method: Refine
- Batch Size: 3
- Delay: 500ms
- Chunking: Advanced (with custom splitter)

**For Quick Processing:**
- Method: Stuff
- No batching required
- Ensure documents fit in context window

### Error Handling

Enable "Continue on Fail" in node settings to handle:
- API rate limit errors gracefully
- Individual document processing failures
- Network timeout issues

## Compatibility

- **Minimum n8n version**: 1.0.0
- **Node.js version**: ≥20.15.0
- **Tested with**: n8n 1.82.0+

### Dependencies
- **LangChain**: ^0.3.34 (document processing and LLM integration)
- **LangChain Core**: ^0.3.76 (base functionality)
- **LangChain Text Splitters**: ^0.1.0 (chunking support)

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [LangChain Documentation](https://js.langchain.com/)
- [Node Source Code](https://github.com/nichmorgan/n8n-nodes-inner-batched-chain-summarization)
- [Comprehensive Documentation](CLAUDE.md) - Detailed technical implementation guide

## Version History

### 0.1.0 (Current)
- **Initial Release**: Complete batched chain summarization implementation
- **Features**: Three summarization methods (map-reduce, refine, stuff)
- **Batching**: Intelligent batching with configurable delays and rate limiting
- **Testing**: Comprehensive test suite with 111+ tests covering all functionality
- **Performance**: Optimized for large document processing with pause functionality
- **Validation**: Input validation prevents infinite loops and invalid configurations
- **Architecture**: Shared constants system prevents circular dependencies

### Upcoming Features
- Enhanced document format support
- Advanced prompt template management
- Integration with more LangChain document loaders
- Performance monitoring and metrics

---

**Author**: Morgan C. Nicholson (nich.dev@pm.me)
**License**: MIT
**Repository**: [GitHub](https://github.com/nichmorgan/n8n-nodes-inner-batched-chain-summarization)