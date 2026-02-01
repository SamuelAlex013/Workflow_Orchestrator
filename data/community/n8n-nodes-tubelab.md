# n8n-nodes-tubelab

This is an n8n community node. It lets you get enhanced YouTube data - including 400K+ trending channels, 4M+ outliers and scan niches in real-time with [TubeLab](https://tubelab.ai).

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Usage](#usage)
[Resources](#resources)
[Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-tubelab` in **Enter npm package name**.
4. Agree to the risks of using community nodes: select **I understand the risks of installing unverified code from a public source.**
5. Select **Install**.

After installing the node, you can use it like any other node. n8n displays the node in search results in the **Nodes** panel.

## Operations

It supports these TubeLab operations:

- **Search Outliers**: Search for videos directly from the TubeLab Outliers library with AI enhanced data and 30+ filters. Updated in real-time, 24/7.
- **Search Similar Outliers**: Search for YouTube outliers with related content to another outlier(s)
- **Search Channels**: Search for channels directly from the YouTube Niche Finder with AI enhanced data and 30+ filters. Updated in real-time, 24/7.
- **Search Similar Channels**: Search for YouTube channels with related content to another channel
- **Start a Scan**: Start a TubeLab scan to search for fresh outliers and channels on any given topic
- **Get a Scan**: Get the status of a scan and used inputs

## Credentials

To use this node, you will need to authenticate with [TubeLab's API](https://tubelab.net/docs/api).

1. Sign up for a [TubeLab](https://tubelab.net/) account
2. Go to the [Developers Dashboard](https://tubelab.net/developers) and create an API key
3. Create new credential in n8n
   - Use TubeLab's node
   - Under Credential to connect with, click Create New Credential
   - Paste API Key

## Compatibility

This node was developed & tested with the `1.112.5` version.

## Usage

Please refer to [TubeLab's Automation documentation](https://tubelab.net/docs/api/automation) with example templates on how to use this node.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [TubeLab's API Documentation](https://tubelab.net/docs/api)
- [Sign up for a TubeLab API key](https://tubelab.net)
- Contact support if you have any issues: [https://tubelab.net/support](https://tubelab.net/support)

## Version history

- 0.3.3 - Fix Start Scan `findBy`input
- 0.3.2 - Add "publishedAtFrom" to Outliers Filters
- 0.3.0 - Fix Webhooks Trigger
- 0.2.0 - Fix API base URL
- 0.1.1 - Fix package.json metadata details
- 0.1.0 - Initial release
