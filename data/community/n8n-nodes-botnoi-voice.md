# 🔊 n8n-BotnoiVoice

Plug-in to connect [Botnoi Voice API](https://voice.botnoi.ai/api-login) to [n8n](https://n8n.io/) — allowing easy use of **Thai Text-to-Speech (TTS)** and **Subtitle Generation (Gensub)** directly inside your n8n workflows.

---

## 📌 Requirements before starting

### 1. Install basic tools

- [Git](https://git-scm.com/downloads)
- Node.js version **20+**
- Recommended via [nvm](https://github.com/nvm-sh/nvm) (Linux, Mac, WSL)
- For Windows, see [Microsoft Docs](https://learn.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows)
- Install n8n globally:

```bash
npm install -g n8n
````

---

## 🚀 How to use the plugin

### ✅ Install from npm (recommended)

1. Create a custom n8n extensions folder:

```bash
mkdir -p ~/.n8n/custom
cd ~/.n8n/custom
npm init -y
```

2. Install the plugin:

```bash
npm i n8n-nodes-botnoi-voice
```

3. Start n8n:

```bash
n8n start
```

> 💡 Once installed, search in n8n for **Botnoi Voice** or **Botnoi Gensub** nodes.

---

### 🛠️ Install locally (if cloning repo)

1. Clone and install dependencies:

```bash
git clone https://github.com/phoovadetnoobdev/n8n-nodes-botnoi-voice
cd n8n-nodes-botnoi-voice
npm install
```

2. Build and link the plugin:

```bash
npm run build
npm link
```

3. Link to your n8n instance:

```bash
mkdir -p ~/.n8n/custom
cd ~/.n8n/custom
npm init -y
npm link n8n-nodes-botnoi-voice
```

4. Start n8n:

```bash
n8n start
```

---

## 🔐 Get API Key from Botnoi Voice

1. Visit [https://voice.botnoi.ai/api-login](https://voice.botnoi.ai/api-login)
2. Login or sign up for a free account
3. Click **Generate API Key**
4. Copy the key for use in n8n

<p align="center">
  <img src="https://github.com/user-attachments/assets/53cae275-c947-49ac-aa5f-49c224914da9" width="640" alt="Generate API Key"/>
</p>

---

## ⚙️ Add API Key in n8n

1. Open **Credentials** tab in n8n
2. Create a new credential → Select **Botnoi Voice**
3. Paste your API key and test connection

<p align="center">
  <img src="https://github.com/user-attachments/assets/7ddb26c4-2241-420f-8212-5096e1e052c5" width="640"/>
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/2d5a905a-7f46-4447-a5fe-aa682a318621" width="640"/>
</p>

> ✅ If the key is correct, it will show “Connection tested successfully”.

---

## 🗣️ Botnoi Voice (TTS)

Convert any text into natural-sounding speech in Thai, English, Japanese, Vietnamese, and more.

### 🧾 Usage Steps

#### 1️⃣ Enter text to convert

<p align="center">
  <img src="https://github.com/user-attachments/assets/a20ee802-7ecb-4005-bc18-7ffe18e2ac92" width="640"/>
</p>

* Add a `Botnoi Voice` node
* Enter text manually or use expression (e.g. `{{ $json.output }}`)

#### 2️⃣ Choose a speaker

<p align="center">
  <img src="https://github.com/user-attachments/assets/1628e724-a7c6-4f76-a203-dad037eca3a4" width="640"/>
</p>

* Over 300 voices available (Eva, Bo, Max, Alisa, etc.)

#### 3️⃣ Select language

<p align="center">
  <img src="https://github.com/user-attachments/assets/8fb5380f-f4b2-48cf-89f6-03d77e8679d4" width="640"/>
</p>

* Supports multiple languages — choose `Thai`, `English`, `Japanese`, etc.

#### 4️⃣ Generate audio

<p align="center">
  <img src="https://github.com/user-attachments/assets/06ecb4b4-cd85-45a2-b99e-6db17f63f443" width="640"/>
</p>

* Click **Execute Step** → Output shows `audio_url` for playback or download.

---

## 🎧 Botnoi Gensub (Subtitle Generator)

Generate subtitles (SRT / JSON) automatically from any **audio URL** via [Botnoi Voice API](https://voice.botnoi.ai/api-login).

Ideal for creating Thai transcripts, podcast captions, or speech analytics.

### 🧩 Overview

* Supports **URL input only**
* Generates **SRT or JSON** subtitles
* Adjustable silence and duration segmentation
* Perfect with free hosting (e.g., [EdgeOne Pages](https://pages.edgeone.ai/drop))

---

### 🧱 Example: Generate Subtitles from an Audio URL

#### ✅ Step 1 — Upload audio

Use [EdgeOne Pages Drop](https://pages.edgeone.ai/drop) to host your file:

1. Go to [https://pages.edgeone.ai/drop](https://pages.edgeone.ai/drop)
2. Enter a temporary domain name
3. Upload your `.mp3` or `.wav`
4. Copy the URL (e.g.)

   ```
   https://forward-cyan-xo4dfpu9q6.edgeone.app/Recording.mp3
   ```

<p align="center">
  <img alt="Image" src="https://github.com/user-attachments/assets/02666ee6-50c8-40fc-a1c8-f0d4908559f0" width="640"/>
</p>

---

#### ✅ Step 2 — Configure Botnoi Gensub Node

| Field                          | Example                                                     | Description                              |
| ------------------------------ | ----------------------------------------------------------- | ---------------------------------------- |
| **Credential to connect with** | Botnoi account                                              | Use your `botnoiApi` credential          |
| **Audio URL**                  | `https://forward-cyan-xo4dfpu9q6.edgeone.app/Recording.mp3` | Publicly accessible file URL             |
| **Max Duration (Seconds)**     | `10`                                                        | Max duration per subtitle segment        |
| **Max Silence (Seconds)**      | `0.3`                                                       | Silence threshold before splitting lines |
| **Return SRT**                 | `Yes`                                                       | Choose “Yes” to get SRT subtitle text    |
| **Timeout (Ms)**               | `60000`                                                     | Request timeout (default 60s)            |

<p align="center">
 	<img alt="Image" src="https://github.com/user-attachments/assets/4c46f6c1-594d-48dc-83df-b23db3abb38c" width="640"/>
</p>

---

#### ✅ Step 3 — Execute and check result

```json
{
  "message": "Transcribe successfully",
  "data": {
    "text": "1\n00:00:00,390 --> 00:00:02,220\nสวัสดีตอนเช้า\n",
    "current_point": 509,
    "current_monthly_point": 0,
    "used_points": 15
  }
}
```

**Result (SRT format):**

```
1
00:00:00,390 --> 00:00:02,220
สวัสดีตอนเช้า
```

<p align="center">
  <img alt="Image" src="https://github.com/user-attachments/assets/f992c796-8185-482d-80f5-188fd6599706" width="640"/>
</p>

---

## ⚙️ Tips

* Both nodes share the same credential `botnoiApi`
* Ensure your audio URL is **publicly accessible** (no login needed)
* Supported file formats: `.mp3`, `.wav`, `.m4a`
* Recommended audio length ≤ 60 seconds for best transcription quality

---

## 📚 References

* [Botnoi Voice API Docs](https://www.botnoigroup.com/botnoivoice/doc/api-user-guide)
* [EdgeOne Pages Drop](https://pages.edgeone.ai/drop) — free quick hosting
* [n8n Node Developer Docs](https://docs.n8n.io/integrations/creating-nodes/)

---

## 🧑‍💻 Maintainer

Developed by **Phoovadet Noobdev**

---

## 📝 License

[MIT License](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
