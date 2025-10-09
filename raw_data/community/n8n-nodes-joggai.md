# n8n-nodes-joggai

Automate the creation of digital human and marketing videos in your n8n workflows via API.

---

JoggAI transforms the days-long manual process of video creation into an automated task that takes just a few minutes. Whether you're batch-producing personalized marketing videos or automatically converting blog posts into videos, you can do it all effortlessly within n8n.

## ✨ Features

- ✅ **Create Video from Digital Human:** Generate talking head videos using Avatars you've created in your JoggAI dashboard or free ones from the public library.
- ✅ **Create Video from Template:** Dynamically populate content into preset templates from your JoggAI dashboard to generate videos.
- ✅ **URL to Video:** Instantly convert any product link into a marketing video.
- ✅ **Create Digital Human:** Supports various digital human likenesses and voice cloning.
- ✅ **Check Video Status:** Asynchronously fetch video generation progress, suitable for long rendering tasks.

## Prerequisites

Before using this node, please ensure you have:

- A running n8n instance.
- A JoggAI account. If you don't have one, you can [register for free here](https://app.jogg.ai/register).

## 🚀 Quick Start

1.  **Install the Node in n8n:**
    - Go to `Settings > Community Nodes`.
    - Click `Install` and search for `n8n-nodes-jogg-ai`.

2.  **Configure JoggAI Credentials:**
    - In the `Credentials` section of n8n, click `Add Credential`.
    - Search for and select `JoggAI API`.
    - Go to your [JoggAI API settings page](https://app.jogg.ai/home) to copy your API Key and paste it.
      ![Find your JoggAI API Key](https://res.jogg.ai/upload/sam/2025-07-11/292683374000458e91c7a55c4a3915b5.png)

## 💡 Example: Automatically Generate Videos from Google Sheets Content

This workflow automatically creates an Talking avatar video using data from n8n Form.
![N8N Form to JoggAI Workflow Example](https://res.jogg.ai/upload/sam/2025-07-11/3be2a12eb38a468594af1e9dd474a917.png)

1.  Use the `N8N Form Trigger` node to monitor for new rows.
2.  Connect the `JoggAI` node.
3.  In the "Text Script" field of the JoggAI node, use an expression to reference column data from the N8N Form, for example: `{{ $json.script }} welcome to joggAI`.
4.  Execute the workflow, and the video will be created automatically.

> Want to use this template directly? [Click here to copy the workflow in one click](https://gist.githubusercontent.com/joggaiteam/ab4065803111fd860584deb3dd245689/raw/ef28aa8d6c85bd2213c7c9a177b0c8c3d9e953b0/joggai-example.json).

## 🔗 Resources

- ⚙️ **Full JoggAI API Documentation:** [docs.jogg.ai](https://docs.jogg.ai/api-reference/QuickStart/GettingStarted)

## 💬 Support & Feedback

- For any bugs or feature requests, please raise them in [GitHub Issues](https://github.com/joggaiteam/n8n-nodes-joggai/issues).
- If you have questions about usage, feel free to ask and @mention us on the [n8n Community Forum](https://community.n8n.io/).
