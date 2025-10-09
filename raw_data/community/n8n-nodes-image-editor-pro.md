# 📸 ImageEditorPro – Custom Node for n8n

Advanced image manipulation node for [n8n.io](https://n8n.io) using [sharp](https://sharp.pixelplumbing.com/) and [@napi-rs/canvas](https://github.com/Brooooooklyn/canvas).

---

## ✨ Features

### 🧩 Collage Mode  
Combine multiple images into a grid layout with:
- Custom number of rows and columns (e.g. 2x2, 3x3)
- Spacing between images
- Background color

### ✍️ Add Text Mode  
Overlay styled text onto an image with full control:
- Text content
- Font size
- Font color
- Opacity
- Position:
  - `top-left`
  - `center`
  - `bottom-right`
  - `custom` (X/Y coordinates)
- Background shape behind the text:
  - `none` (default)
  - `rectangle`
  - `circle`
- Background shape styling:
  - `backgroundColor`: Fill color (e.g. `#00000088`)
  - `padding`: Space around the text inside the shape
  - `borderColor`: Outline color
  - `borderWidth`: Outline thickness

### 💦 Add Watermark Mode  
Add a watermark text to an image:
- Watermark content
- Positioning (same options as Add Text)
- Opacity

---

## 🌐 Input Options

Supports both:
- Binary image input from previous n8n nodes (e.g. HTTP Request → Binary)
- URLs (comma-separated string)

---

## 📤 Output

Returns the processed image as a binary PNG with key: `data`.

---

## 🧪 Example Use-Cases

- Add price or name labels to product images
- Generate automatic preview collages
- Brand content with watermarks
- Highlight information with background text badges

---

## 🚀 Installation

### Option 1: Install via n8n Community Nodes (Recommended)

1. Go to **Settings → Community Nodes** in your n8n instance  
2. Click **Install a Community Node**  
3. Enter the package name:

```
n8n-nodes-image-editor-pro
```

4. Click **Install**

### ⚠️ Requirements (Linux / Alpine-based systems)

If installation fails with errors related to `canvas.node` or missing libraries, you need to install system dependencies:

#### For Ubuntu/Debian:

```bash
sudo apt update
sudo apt install -y libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev librsvg2-dev build-essential g++
```

#### For Alpine (e.g., in Docker):

```bash
apk add --no-cache \
  cairo-dev \
  jpeg-dev \
  pango-dev \
  giflib-dev \
  librsvg-dev \
  build-base \
  gcc \
  g++ \
  python3 \
  nodejs \
  npm
```

Then **rebuild the node container** or restart n8n.

---

## 🧱 Development & Manual Installation

```bash
git clone https://github.com/YOUR_USERNAME/n8n-nodes-image-editor-pro.git
cd n8n-nodes-image-editor-pro
npm install
npm run build
```

---

## 🛠 Troubleshooting

- Error about `canvas.node`: make sure all system libraries for `node-canvas` are installed (see above).
- Use `npm rebuild canvas` inside `.n8n/nodes/node_modules/n8n-nodes-image-editor-pro` if issues persist.
- You may also need to restart the container if running n8n in Docker.

---

## 📦 Publishing

To publish your own version to npm:

```bash
npm version patch
npm publish
```

---

## 🧠 Contribute

Pull requests are welcome! Ideas for features:
- Support SVG inputs
- Auto-resize text to fit area
- Add borders/shadows to text or images
