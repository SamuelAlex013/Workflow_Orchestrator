# n8n-nodes-smartleadai

This is an n8n community node that lets you use [Smartlead.ai](https://smartlead.ai) in your n8n workflows.

Smartlead.ai is a platform for sending cold emails at scale, with features for campaign management, lead tracking, and analytics.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](https://www.google.com/search?q=%23installation)
[Operations](https://www.google.com/search?q=%23operations)
[Credentials](https://www.google.com/search?q=%23credentials)
[Compatibility](https://www.google.com/search?q=%23compatibility)
[Resources](https://www.google.com/search?q=%23resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

1.  Go to **Settings \> Community Nodes**.
2.  Select **Install**.
3.  Enter `n8n-nodes-smarteadapi` in **Enter npm package name**.
4.  Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5.  Select **Install**.

After installing the node, you can use it like any other node. n8n displays the node in search results in the **Nodes** panel.

## Operations

This node supports a wide range of operations for managing your Smartlead.ai account:

  * **Campaign Management**

      * Create a new campaign
      * List all campaigns
      * Get a campaign by ID
      * Delete a campaign
      * Update a campaign's schedule
      * Update a campaign's general settings
      * Update a campaign's status (Start/Pause/Stop)
      * Fetch a campaign's sequence data
      * Save a campaign sequence
      * List all email accounts in a campaign
      * Add an email account to a campaign
      * Remove an email account from a campaign

  * **Lead Management**

      * Add leads to a campaign
      * List all leads in a campaign
      * Update a lead's information
      * Delete a lead from a campaign
      * Pause a lead in a campaign
      * Resume a lead in a campaign
      * Unsubscribe a lead from a campaign
      * Update a lead’s category
      * Fetch a lead by email address
      * Fetch all available lead categories
      * Fetch all campaigns a lead belongs to
      * Unsubscribe a lead from all campaigns
      * Add a lead or domain to the global block list

  * **Email Account Management**

      * Fetch all email accounts
      * Create a new email account
      * Fetch an email account by ID
      * Update an email account
      * Add/Update warmup settings for an email account
      * Fetch warmup stats for an email account
      * Reconnect failed email accounts

  * **Statistics & Analytics**

      * Fetch detailed statistics for a campaign
      * Fetch top-level analytics for a campaign
      * Fetch campaign statistics within a date range
      * Export all leads from a campaign as a CSV file

  * **Master Inbox & Messaging**

      * Fetch the message history for a lead in a campaign
      * Reply to a lead from the Master Inbox

  * **Webhooks**

      * Fetch all webhooks for a campaign
      * Add or update a webhook for a campaign
      * Delete a webhook from a campaign

  * **Client Management**

      * Fetch all clients
      * Add a new client to the system

## Credentials

To use this node, you need a Smartlead.ai API key.

1.  Log in to your [Smartlead.ai account](https://app.smartlead.ai/).
2.  Navigate to the **Settings** section.
3.  Click on **Activate API** to get your API key.
4.  Enter this key into the Smartlead API credentials in n8n.

## Compatibility

  - Minimum n8n version: **1.0.0**

## Resources

  * [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
  * [Smartlead.ai API Documentation](https://help.smartlead.ai/API-Documentation-a0d223bdd3154a77b3735497aad9419f)

## License

[MIT](https://www.google.com/search?q=https://github.com/Chris-Terminator/n8n-nodes-smarteadapi/blob/master/LICENSE.md)
