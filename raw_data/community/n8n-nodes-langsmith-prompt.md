![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-langsmith-prompt

This is an n8n community node. It lets you use LangSmith prompt templates in your n8n workflows.

LangSmith is a platform for debugging, testing, evaluating, and monitoring LLM applications, allowing you to manage prompts and track their performance.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

- **Fill Prompt Template**: Fetches a prompt template from LangSmith by name and substitutes parameter values into the template's variable placeholders.

## Credentials

You need a LangSmith API key to use this node.

1. Sign up for an account at [LangSmith](https://smith.langchain.com/)
2. Generate an API key in your account settings
3. Use this API key in the LangSmith API credentials in n8n

## Compatibility

This node has been tested with n8n version 1.0.0 and later.

## Usage

1. Add the LangSmith Prompt node to your workflow
2. Configure the LangSmith API credentials with your API key
3. Enter the Prompt Name of the prompt template you want to fetch from LangSmith
4. Add Input Parameters to substitute in the template:
   - Click "Add Parameter" to add key-value pairs
   - For each parameter, provide:
     - Name: The parameter name as it appears in the template (e.g., if template contains {question}, use "question")
     - Value: The value to substitute for that parameter

### Example: Template Variable Substitution

If your LangSmith prompt template is:

```text
This is your question: "{Question}"
```

And you add a parameter with:

- Name: Question
- Value: What is artificial intelligence?

The filled template output will be:

```text
This is your question: "What is artificial intelligence?"
```

### Working with Multiple Parameters

If your template has multiple variables like:

```text
Hello {Name}, your question about {Topic} is: "{Question}"
```

Add three parameters:

- Name: Name, Value: John
- Name: Topic, Value: Machine Learning
- Name: Question, Value: How do neural networks work?

### Node Output

The node outputs an object with the prompt name as key and the filled prompt content as value:

```json
{
  "my-template": "This is your question: \"What is artificial intelligence?\""
}
```

You can reference this output in subsequent nodes using expressions such as:

```javascript
{{$node["LangSmith Prompt"].json["my-template"]}}
```

Where "my-template" is the name of your prompt.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [LangSmith documentation](https://docs.smith.langchain.com/)
- [LangSmith API reference](https://docs.smith.langchain.com/reference/)

## License

[MIT](LICENSE.md)
