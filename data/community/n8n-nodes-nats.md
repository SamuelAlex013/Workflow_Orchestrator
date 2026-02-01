![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# NATS node

nodes to communicate with the message broker [nats](nats.io).

## Features

Common:
- Header support
- Shared tcp connection in each workflow instance
- Payload in text,json or binary format

NATS credentials:
- Connect with different authenticators
- Set most of [nats.js](https://github.com/nats-io/nats.node) connection options

NATS node:
- Publish to a subject
- Send request to a nats service and receive one or more responses

NATS Jetstream node:
- Publish to a Nats JetStream

NATS Jetstream trigger:
- Receive message from a NATS via consumer. Currently supports both durable consumers (pre-created) and ephemeral consumers.
    - Durable consumer: Provide the existing consumer name. This consumer is created and managed outside of n8n.
	- Ephemeral consumer: Enable “Auto-create Ephemeral Consumer” and optionally set a “Filter Subject”. The node will create a pull consumer on demand (and clean it up when stopped). The consumer name is only required for durable consumers.

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
