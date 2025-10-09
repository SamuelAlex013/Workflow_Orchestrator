# n8n-nodes-autocalls

This is an n8n community node. It lets you use Autocalls in your n8n workflows.

Autocalls is an AI-powered calling platform that enables you to automate phone calls using intelligent virtual assistants.

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

This package provides the Autocalls node with a unified interface for both actions and triggers:

### Autocalls Node

When you add the **Autocalls** node to your workflow, n8n will present you with a submenu to choose between:

#### Actions (Regular Node)
- **Call**: Make phone calls using AI assistants
  - **Make**: Initiate phone calls using AI assistants
    - Select an assistant from your Autocalls account (outbound assistants only)
    - Specify the phone number to call
    - Add variables with name/value pairs to customize the conversation

- **Assistant**: Manage assistants
  - **Get Assistants**: Retrieve assistants from your Autocalls account
    - Fetches all assistants from your account
    - Returns each assistant as a separate item with details like name, ID, status, etc.
    - Regular action that can be used in any workflow

#### Triggers (Trigger Node)
- **Call**: Monitor phone call events
  - **Call Ended**: Receive notifications when phone calls end
    - Select an assistant to monitor
    - Receives call details including duration, status, and transcript
    - Gets extracted variables from the conversation
    - Provides input variables that were used
    - Real-time webhook notifications

## Credentials

To use this node, you need to set up Autocalls API credentials:

1. Sign up for an account at [Autocalls](https://app.autocalls.ai/)
2. Generate an API key from your account settings
3. In n8n, create new credentials of type "Autocalls API"
4. Enter your API key

The credentials are automatically validated when you save them.

## Compatibility

- Minimum n8n version: 0.36.1
- Tested with n8n version: 1.0.0+

## Usage

### Adding the Autocalls Node

1. Add the **Autocalls** node to your workflow
2. n8n will present you with a submenu to choose between **Action** and **Trigger**
3. Select the type you need:
   - **Action**: For making phone calls (requires input connection)
   - **Trigger**: For receiving events or fetching data (no input connection needed)

### Using Actions

#### Making Phone Calls

1. Choose **Action** from the submenu
2. Select **Resource**: Call, **Operation**: Make
3. Choose an outbound assistant from the dropdown (assistants are loaded from your Autocalls account)
4. Enter the phone number to call
5. Add variables using the name/value interface to personalize the conversation (e.g., Name: "customer_name", Value: "John")

#### Getting Assistants

1. Choose **Action** from the submenu
2. Select **Resource**: Assistant, **Operation**: Get Assistants
3. The action will fetch all assistants from your account
4. Each assistant will be returned as a separate item with details like name, ID, status, etc.
5. Can be used like any regular action in your workflows

### Using Triggers

The **Autocalls Call Ended Trigger** receives webhook notifications when phone calls are completed. This trigger provides real-time data about call outcomes, extracted variables, and conversation transcripts.

#### What Data You Receive

When a call ends, the trigger receives a webhook with the following information:

- **Call Details**: ID, duration, status
- **Phone Numbers**: Customer and assistant phone numbers
- **Extracted Variables**: AI-extracted data from the conversation
- **Input Variables**: Variables passed to the assistant before the call
- **Transcript**: Full conversation transcript
- **Recording URL**: Link to call recording (if enabled)
- **Timestamps**: When the call started and ended
- **Lead Information**: Lead and campaign details (for campaign calls)

#### Setting Up the Trigger

1. Choose **Trigger** from the submenu
2. Select an assistant to monitor from the dropdown
3. The trigger will automatically generate a webhook URL
4. **Important**: You must manually register this webhook URL in your Autocalls assistant settings
5. Go to your assistant settings in Autocalls dashboard
6. Add the webhook URL ,enable webhook status and save the configuration

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Autocalls Documentation](https://docs.autocalls.ai/)
* [Autocalls API Reference](https://docs.autocalls.ai/api-reference/)
* [Autocalls Platform](https://app.autocalls.ai/)
