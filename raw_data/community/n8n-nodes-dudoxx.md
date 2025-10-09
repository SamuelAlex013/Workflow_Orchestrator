# n8n-nodes-dudoxx

![AssemblyAI N8N Hero](./images/assemblyai-n8n-hero.png)

This is an n8n community node package for interacting with the [AssemblyAI](https://www.assemblyai.com/) API.

It currently includes the following nodes:

*   **AssemblyAI Transcriber:** Transcribes audio files using the AssemblyAI API. Supports providing audio via URL or binary file input.

[n8n](https://n8n.io/) is a fair-code licensed workflow automation platform.

- [n8n-nodes-dudoxx](#n8n-nodes-dudoxx)
  - [Installation](#installation)
  - [Operations](#operations)
  - [Credentials](#credentials)
  - [Compatibility](#compatibility)
  - [Usage](#usage)
    - [Example Output (Transcript Text Only)](#example-output-transcript-text-only)
  - [Resources](#resources)
  - [Consulting \& Services](#consulting--services)
  - [License](#license)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

1.  Go to **Settings > Community Nodes**.
2.  Select **Install**.
3.  Enter `n8n-nodes-dudoxx` in the **Enter package name** field.
4.  Agree to the risks of using community nodes: select **I understand the risks, and I want to proceed**.
5.  Select **Install**.

After installing the node, you can use it like any other node. n8n displays the node in the node panel under **Community** > **Installed**.

## Operations

![AssemblyAI N8N Flow](./images/assemblyai-n8n-flow.png)

*   **AssemblyAI Transcriber:**
    *   Transcribe audio from a public URL.
    *   Transcribe audio from an n8n binary file property.
    *   Supports various AssemblyAI models (including 'best' and 'nano').
    *   Allows specifying additional options like language detection, speaker diarization, punctuation, text formatting, word boost, and more.
    *   Choose between outputting the full raw transcript or just the transcript text.
    *   Customize the field name for the transcript text output.
    *   Includes detailed metadata about the transcription process and audio source.

## Credentials

Requires AssemblyAI API credentials.

1.  Go to your [AssemblyAI Dashboard](https://www.assemblyai.com/dashboard/).
2.  Navigate to **API Keys**.
3.  Create a new API key or use an existing one.
4.  In n8n, create new credentials for the AssemblyAI Transcriber node.
5.  Enter your AssemblyAI API Key.

## Compatibility

Tested with n8n version 1.x.

## Usage

1.  Install the package in your n8n instance.
2.  Add the **AssemblyAI Transcriber** node to your workflow.
3.  Configure the node properties:
    *   Select the **Source** (URL or Binary Data).
    *   Provide the **Audio URL** or **Input Binary Field** name.
    *   Choose the desired **Speech Model** ('best' or 'nano').
    *   Configure **Additional Options** as needed (language detection, speaker labels, etc.).
    *   Select the **Output Format** (Full Response or Transcript Text Only).
    *   If using "Transcript Text Only" format, optionally specify a custom **Transcript Field Name** (defaults to `text`).
4.  Connect the node and run your workflow.

### Example Output (Transcript Text Only)

```json
{
  "text": "Yeah. As much as it's worth celebrating the first spacewalk with an all female team, I think many of us are looking forward to it just being normal. And I think if it signifies anything, it is to honor the women who came before us who were skilled and qualified and didn't get the same opportunities that we have today.",
  "metadata": {
    "duration_ms": 4693,
    "speech_model": "best",
    "audio_duration": 26,
    "confidence": 0.9740912,
    "source": "url",
    "url": "https://dpgr.am/spacewalk.wav"
  }
}
```

## Resources

*   [n8n Community Nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
*   [AssemblyAI API Documentation](https://www.assemblyai.com/docs/)
*   [GitHub Repository: dudoxx/n8n-nodes-dudoxx](https://github.com/dudoxx/n8n-nodes-dudoxx)

## Consulting & Services

For custom node development, workflow automation consulting, or other n8n-related services, please contact:

**DUDOXX Team**  
Email: [contact@dudoxx.com](mailto:contact@dudoxx.com)  
Website: [https://dudoxx.com](https://dudoxx.com)

## License

[MIT](LICENSE.md)
