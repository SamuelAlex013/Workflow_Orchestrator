# Global Variables n8n Node

> Inspired by `n8n-nodes-globals`
>
> https://github.com/umanamente/n8n-nodes-globals
>
> _At the time of creation of `n8n-nodes-global-variables`, `n8n-nodes-globals` didn't support JSON variables._  
> _And even still I enjoy being able to organize my variables into multiple named variables._  
> _Personal preference!_

<img src="screenshots/workflow-canvas.png" width="500" />

# Install `n8n-nodes-global-variables`

> Requires self-hosted n8n

<img src="screenshots/install.png" width="500" />

# How it works

## 1. Create a `Global Variables` credential

> Note: you can have as many of these as you want to organize your variables.

<img src="screenshots/search-credential.png" width="500" />

## 2. Add some variables with names and values

> The credential stores up to 10 named variables with values.
>
> _Note: I found that up to 50 work, but it slows down loading of the credential UI. Fork the code if you want up to 50._
>
> If you want to organize your variables into more than 10 named variables, you can create multiple credentials.

<img src="screenshots/v0.0.5/named-credential-with-values.png" width="650" />

## 3. Add a `Global Variables` node in your workflow

> Choose the credential you created in step 1.

<img src="screenshots/search-nodes.png" width="500" />

<img src="screenshots/workflow-canvas.png" width="500" />

<img src="screenshots/v0.0.5/open-node-create-credential-dropdown.png" width="500" />

<img src="screenshots/v0.0.5/populated-node.png" width="500" />

## That's it!

Wherever the node is used, its variables will be available in the workflow after the node is executed in `$json`.

<img src="screenshots/one-key-table.png" width="500" />

### `$json.vars.X`

If you choose `Put All Variables in One Key` in the node options, all variables will be available under the `$json.<the name you chose>` key.

<img src="screenshots/v0.0.5/schema-output.png" width="500" />

<img src="screenshots/v0.0.5/json-output.png" width="500" />

### `$json.X`

If you disable `Put All Variables in One Key` in the node options, each variable will be available under its own key in `$json`.

<img src="screenshots/not-one-key-table.png" width="500" />

<img src="screenshots/not-one-key-json.png" width="500" />

## Does not overwrite existing variables

If you have existing variables in your workflow, the `Global Variables` node will not overwrite them.

It will only add the variables that are defined in the credential.

<img src="screenshots/workflow-canvas-with-edit-fields.png" width="500" />

<img src="screenshots/show-existing-value.png" width="500" />

## Expressions

Expressions such as `{{ $json.foo }}` work as expected!

So long as `$json.foo` is available before the `Global Variables` node is executed.

# Attribution

This node is inspired by the `n8n-nodes-globals` node by [Umanamente](https://github.com/umanamente).
>
> https://github.com/umanamente/n8n-nodes-globals
>
> License MIT
