# n8n-nodes-upload-post

This is an n8n community node package for [Upload Post](https://www.upload-post.com/). It allows you to automate uploading photos, videos, and text posts to various social media platforms supported by the Upload Post API.

[n8n](https://n8n.io/) is a fair-code licensed workflow automation tool.

## Installation

Follow the [n8n community node installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) to install this node.

1.  Go to **Settings > Community Nodes**.
2.  Select **Install**.
3.  Enter `n8n-nodes-upload-post` in **Enter npm package name**.
4.  Agree to the [risks of using community nodes](https://docs.n8n.io/integrations/community-nodes/risks/).
5.  Select **Install**.

After installing the node, you can use it in your n8n workflows.

## Credentials

To use this node, you need to configure the Upload Post API credentials:

1.  Create an API key from your [Upload Post dashboard](https://www.upload-post.com/).
2.  In n8n, go to **Credentials > New**.
3.  Search for **Upload Post API** and select it.
4.  Enter a **Credential Name**.
5.  Paste your Upload Post API key into the **API Key** field.
6.  Select **Save**.

## Operations

The node provides the following operations grouped for clarity:

### Upload Actions
- **Upload Photo(s)**: Upload one or more photos to supported platforms.
  - Supports file uploads and photo URLs.
  - Common parameters: User Identifier, Platform(s), Title, Description (optional), Photos (Files or URLs), Scheduled Date (optional).
  - Title/Description overrides per platform: set `[platform]_title` and `[platform]_description` to override the generic fields (e.g., `instagram_title`, `youtube_description`).
  - Platform-specific parameters are available for LinkedIn, Facebook, TikTok, Instagram, and Pinterest.
  - Pinterest: requires selecting a Board via the dynamic selector (see Selectors below).
- **Upload Video**: Upload a single video to supported platforms.
  - Supports file uploads and video URLs.
  - Common parameters: User Identifier, Platform(s), Title, Description (optional), Video (File or URL), Scheduled Date (optional).
  - Title/Description overrides per platform supported as arriba.
  - YouTube: supports custom thumbnail via URL or binary (YouTube Thumbnail).
  - Platform-specific parameters are available for LinkedIn, Facebook, TikTok, Instagram, YouTube, Threads, X (Twitter), and Pinterest.
  - Pinterest: requires selecting a Board via the dynamic selector (see Selectors below).
- **Upload Text**: Upload a text-based post to supported platforms.
  - Common parameters: User Identifier, Platform(s), Title (used as content for most platforms), Scheduled Date (optional).
  - Facebook: supports `Facebook Link` to attach a URL with link preview.
  - Platform-specific parameters are available for LinkedIn, Facebook, Threads, and X (Twitter).

### Status & History Actions
- **Get Upload Status**: Check the status/result of an async upload by `request_id`.
  - Parameters: Request ID.
- **Get Upload History**: List past uploads.
  - Parameters: Page (default 1), Limit (default 20). Limit can be 20, 50, or 100.
- **Get Analytics**: Retrieve aggregated analytics for uploads.
  - Optional filters: From Date, To Date, User Filter, Platforms.

### Scheduled Posts
- **List Scheduled Posts**: Lists future scheduled jobs.
- **Cancel Scheduled Post**: Cancels a scheduled job by its Job ID.
- **Edit Scheduled Post**: Updates a scheduled job (e.g., new scheduled date/time).
  - Tip: You can schedule any Upload action by providing the `Scheduled Date` during upload.

### Platform Selectors (Dynamic)
- Facebook Pages: pick the Page from a dynamic list, or enter an ID via expression. Backed by the API endpoint documented at https://docs.upload-post.com/api/get-facebook-pages
- LinkedIn Pages: pick the Organization Page from a dynamic list, or enter an ID via expression. Backed by the API endpoint documented at https://docs.upload-post.com/api/get-linkedin-pages
- Pinterest Boards: pick the Board from a dynamic list, or enter an ID via expression. Backed by the API endpoint documented at https://docs.upload-post.com/api/get-pinterest-boards

### User Actions (incl. JWT for custom platform integration)
- ⚠️ JWT endpoints are only needed if you integrate Upload-Post into your own platform and want end-users to link their social accounts via your UI.
- **List Users**: Retrieve Upload-Post profiles created under your API key.
- **Create User**: Create a new user profile.
  - Parameters: New User Identifier (username).
- **Delete User**: Delete an existing user profile.
  - Parameters: Username to delete.
- **Generate JWT (for platform integration)**: Generate a connection URL (JWT) for a given profile so the user can link social accounts.
  - Parameters: User Identifier (username). Optional branding parameters may apply server-side.
- **Validate JWT (for platform integration)**: Validate a connection token if you need to check it from your backend.
  - Parameters: JWT.

Refer to the [Upload Post API Documentation](https://docs.upload-post.com) for detailed information on parameters and platform requirements.

### Waiting for asynchronous uploads

Some uploads are processed asynchronously and the API returns immediately with a `request_id`. This happens when:
- You enable "Upload Asynchronously" in the node, or
- The upload takes longer than ~59 seconds and the API switches to async mode automatically.

You have two ways to handle this in n8n:

1) Best-effort polling inside the node
- In Upload operations (Photos/Video/Text), enable "Wait for Completion".
- Configure "Poll Interval (Seconds)" (default 10) and "Timeout (Seconds)".
- The node sleeps between checks (using n8n's `sleep`) and calls `GET /api/uploadposts/status?request_id=...` until success/failure or timeout.
- Note: This does not guarantee completion in hosted environments with strict execution limits.

2) Workflow-level polling (recommended for reliability)
- Use the Upload operation, read `request_id` from its output.
- Add a Wait node (e.g., 10s), then call "Get Upload Status" passing the `request_id`.
- Loop with an IF node until the status is final (success/failed) or a max attempts limit is reached.

### Notable platform-specific options
- Facebook: Media Type (Reels/Stories); Page picker; optional link for Text.
- LinkedIn: Visibility; Organization picker; optional description override.
- TikTok: Post Mode (Direct Post / Media Upload), privacy, duet/comment/stitch toggles.
- Instagram: Media type (Image/Stories/Reels), video options (cover, audio, tags, etc.).
- YouTube: Thumbnail via URL or file; description override; tags/category/privacy and related flags.
- Threads: Description override for video; thread-related handling on backend.
- Pinterest: Board picker; optional link; cover image options (URL/base64/key frame).

### Title & Description overrides
- `Title / Main Content`: generic title used across platforms.
- Platform title overrides: `[platform]_title` (e.g., `x_title`, `pinterest_title`).
- `Description (Optional)`: generic description used across platforms when supported.
- Platform description overrides: `[platform]_description` (e.g., `youtube_description`, `linkedin_description`).

Related docs:
- Profiles & JWT reference (context): [User Profiles API](https://docs.upload-post.com/api/user-profiles#create-user-profile)

## Resources

*   [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
*   [Upload Post Website](https://www.upload-post.com/)
*   [Upload Post API Documentation](https://docs.upload-post.com)

## Compatibility

Tested with n8n version 1.x.
Requires Node.js version 20.15 or later.

## Development

If you want to contribute to this node or run it locally for development:

1.  Clone this repository: `git clone https://github.com/Upload-Post/n8n-nodes-upload-post` (replace `your-github-username`)
2.  Install dependencies: `npm i`
3.  Build the node: `npm run build`
4.  Link the package to your n8n instance for testing. Refer to [Run your node locally](https://docs.n8n.io/integrations/creating-nodes/test/run-node-locally/).

## License

[MIT](LICENSE.md)
