![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-event-pattern

This package provides two n8n nodes that implement the "Event Listener" pattern: an event emitter (`Event Emitter`) and an event-listening trigger (`Event Listener Trigger`).

## Installation

1) Via the n8n UI

- If your n8n instance (cloud or self-hosted) supports installing community packages from the editor, search for `n8n-nodes-event-pattern` in the integrations/community section and install it directly from the UI.

2) Via npm (manual installation on the n8n environment)

- Install from the npm registry (once the package is published):

```bash
npm install n8n-nodes-event-pattern
```

After installation, restart your n8n instance so the nodes appear in the editor.

## Usage

- Event Emitter
  - Purpose: publish an event with a JSON payload.
  - Main fields:
    - Channel: select the channel (e.g. Redis) configured in n8n credentials.
    - Event name: the event type/name (string used to route the message).
    - Event Payload: JSON object to send.
  - Behavior: when executed, the node publishes the payload to the topic associated with the event name.

- Event Listener Trigger
  - Purpose: listen for events and trigger the workflow when a message arrives.
  - Main fields:
    - Channel: select the same channel used by the emitter.
    - Event name: the event name to listen for (must match the emitter).
  - Behavior: the trigger waits for messages on the event topic and, when a message arrives, starts the workflow with the received payload.

## Notes

- Make sure the channel credentials (for example, Redis connection details) are configured in the n8n credentials panel.
- Restart n8n after installing the nodes so they become available in the editor.
