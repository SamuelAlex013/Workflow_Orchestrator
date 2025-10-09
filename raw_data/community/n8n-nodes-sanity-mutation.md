# n8n-nodes-sanity-mutation

This is an n8n community node. It lets you use [Sanity CMS](https://www.sanity.io/) in your n8n workflows.

Sanity CMS is a customizable solution that treats content as data to power your digital business. Sanity offers a suite of features to enable real-time collaboration on content.

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

## Operations

1. `SanitySchemaMapper` node: Takes a Sanity schema and input data, then transforms it into a valid Sanity document.
2. `SanityMutation` node: Create, Update, and Delete documents in Sanity.io

## Credentials

A [Sanity API Token](https://www.sanity.io/docs/content-lake/http-auth) is required to use the `SanityMutation` node.

## Compatibility

Tested with n8n Version: 1.99.1

## Usage

Usage guidance available at: https://realthreads.io/projects/n8n-sanity-nodes


## Resources

* [GitHub Repo](https://github.com/realthreads/n8n-sanity-mutations)
* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Sanity Docs](https://www.sanity.io/docs)


## Version history

* Version 0.1.6: Add credential test.

* Version 0.1.5: Initial working release with two nodes to: transform data into valid Sanity documents; create, edit and delete Sanity documents.

* Version 0.1.0: Initial release with two nodes to: transform data into valid Sanity documents; create, edit and delete Sanity documents.
