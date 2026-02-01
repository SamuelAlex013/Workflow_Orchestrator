# n8n-nodes-wordpress-hash

This is an n8n community node. It lets you generate and verify WordPress-compatible password hashes in your n8n workflows.

WordPress password hashing (via the `wordpress-hash-node` library) provides hashing and verification compatible with WordPress user passwords. This is useful for migrations, integrations, and any workflow where you need to hash or validate passwords against WordPress.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

- Hash: Generate a WordPress-compatible hash from a plaintext password.
- Verify: Check a plaintext password against an existing WordPress hash and return a boolean result.

## Compatibility

- Uses n8n Nodes API v1.
- Targets Node.js >= 20.15.
- Should work with n8n versions that support community nodes and API v1.

## Usage

- Add the "Wordpress Hash" node to your workflow.
- Choose an operation:
  - Hash: Provide a plaintext password to receive a WordPress-compatible hash.
  - Verify: Provide a plaintext password and an existing WordPress hash to get a true/false result.
- The node uses the `wordpress-hash-node` library internally to match WordPress behavior as closely as possible.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [`wordpress-hash-node` on npm](https://www.npmjs.com/package/wordpress-hash-node)
- Repository: https://github.com/mongus/n8n-nodes-wordpress-hash
- Issues: https://github.com/mongus/n8n-nodes-wordpress-hash/issues

## Version history

- 1.0.0 — Initial release of the Wordpress Hash node (operations: hash, verify).
