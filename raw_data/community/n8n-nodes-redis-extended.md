# n8n-nodes-redis-extended

This is an n8n community node. It lets you use **Redis** with extended operations in your n8n workflows.

**Redis Extended** is an enhanced Redis integration that provides additional hash operations (HGET, HDEL, HKEYS) beyond the basic Redis functionality, allowing for more granular control over Redis hash data structures.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Use the package name: `@iaconnecto/n8n-nodes-redis-extended`

## Operations

This node provides comprehensive Redis operations including specialized hash operations:

### Core Operations

- **Delete**: Delete a key from Redis
- **Get**: Get the value of a key from Redis (supports automatic type detection for string, hash, list, sets)
- **Set**: Set the value of a key in Redis
- **Increment**: Atomically increment a key by 1 (creates the key if it doesn't exist)
- **Info**: Get generic information about the Redis instance
- **Keys**: Get all keys matching a pattern with optional value retrieval
- **Publish**: Publish message to Redis channel
- **Push**: Push data to a Redis list (supports head/tail operations)
- **Pop**: Pop data from a Redis list (supports head/tail operations)

### Hash Operations (Extended)

- **Hash Get (HGET)**: Get the value of a specific field in a hash
- **Hash Delete (HDEL)**: Delete one or more fields from a hash (supports comma-separated field names)
- **Hash Keys (HKEYS)**: Get all field names in a hash

### Advanced Features

- **Dot notation support**: Use dot notation for nested property assignment (e.g., `data.user.name`)
- **Multiple data types**: Automatic handling of strings, hashes, lists, and sets
- **TTL support**: Set expiration times for keys
- **JSON parsing**: Automatic JSON parsing for complex data structures
- **Batch operations**: Support for multiple field operations in hash commands

## Credentials

To use this node, you need to configure Redis credentials with the following fields:

- **Host**: Redis server hostname (default: `localhost`)
- **Port**: Redis server port (default: `6379`)
- **Password**: Redis authentication password (if required)
- **User**: Redis username (leave blank for password-only auth)
- **Database Number**: Redis database number (default: `0`)
- **SSL**: Enable SSL/TLS connection (default: `false`)

### Setting up Redis credentials:

1. In n8n, go to **Credentials** → **New**
2. Search for "Redis" and select it
3. Fill in your Redis connection details
4. Test the connection
5. Save the credentials

## Compatibility

- **Minimum n8n version**: 0.198.0+
- **Node.js**: >=20.15
- **Redis**: Compatible with Redis 5.0+ and Redis Stack
- **Tested with**: n8n v1.0+

### Known compatibility:

- ✅ Redis Cloud
- ✅ AWS ElastiCache
- ✅ Azure Cache for Redis
- ✅ Self-hosted Redis instances
- ✅ Redis Stack (with JSON and Search modules)

## Usage

### Basic Key Operations

Use **Get**, **Set**, and **Delete** operations for simple key-value operations.

### Hash Operations (Advanced)

The hash operations provide granular control over Redis hash data structures:

**Hash Get Example:**

- Use when you need only a specific field from a large hash
- More efficient than getting the entire hash with `HGETALL`

**Hash Delete Example:**

- Delete specific fields without affecting other hash data
- Supports multiple fields: `field1,field2,field3`

**Hash Keys Example:**

- Get a list of all available fields in a hash
- Useful for dynamic field processing

### Performance Tips

- Use **Hash Get** instead of **Get** with hash type when you only need specific fields
- Use **Keys** operation with patterns to efficiently filter large keysets
- Enable TTL for temporary data to prevent memory bloat

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Redis Official Documentation](https://redis.io/docs/)
- [Redis Hash Commands Reference](https://redis.io/commands/?group=hash)
- [n8n Redis Integration Guide](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.redis/)
