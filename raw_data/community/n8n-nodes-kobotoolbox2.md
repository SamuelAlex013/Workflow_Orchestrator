# n8n-nodes-kobotoolbox2

This is an n8n community node. It lets you use [KoboToolbox](https://www.kobotoolbox.org/) in your n8n workflows.

[![npm version](https://badge.fury.io/js/n8n-nodes-kobotoolbox2.svg)](https://badge.fury.io/js/n8n-nodes-kobotoolbox2)

[KoboToolbox](https://www.kobotoolbox.org/) is a leading open-source mobile survey solution designed for field use, and adapted to non-profits use.

This node is an alternative to the built-in KoboToolbox node provided by n8n, maintained by the original author. It is maintained here separately because the releasing times from n8n team to integrate new developments can be slow, so this version will typically be ahead of the one packaged within n8n core.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Release Notes

- __0.1.4__: Improved handling of survey media files:
  - Added support for getting/deleting survey media files by filename instead of file ID
  - Can now return media file contents when using __Get Many__ files
  - Can now overwrite an existing survey media file (by deleting before upload)
  - Added support for providing file content to upload as plain text
