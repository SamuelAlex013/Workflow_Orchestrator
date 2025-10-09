![Mallabe Logo](/docs/mallabe-logo.png)

# n8n-nodes-mallabe-images

This is an n8n community node for [Mallabe Images](https://www.mallabe.com/).

It allows you to manipulate images using different operations.

For more information, refer to the [Mallabe website](https://www.mallabe.com/).

Current supported operations:
- Resize Image
- Compress Image
- Get Image Metadata
- Crop Image
- Rotate Image
- Flip / Flop Image
- Greyscale Image
- Join 2 Images

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)

## Development
### Running Locally (Summary)
1. Install n8n globally using https://docs.n8n.io/integrations/creating-nodes/test/run-node-locally/
2. Run `nvm use` to use the correct node version in the node folder.
3. Run `pnpm install` in the node folder.
4. Run `pnpm link --global` to register as package.
5. Run `pnpm run build` whenever you make changes to the node.
6. Run `cd ~/.n8n`
7. Stop n8n if it was already running.
8. Run `pnpm link --global n8n-nodes-mallabe-images` in n8n `custom` folder.
9. Run `n8n start`

Note: if you like to watch the development instead of rebuilding every time, use `npm run dev`.
