![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-comfyui-image-to-image

This package provides n8n nodes to integrate with [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - A powerful and modular stable diffusion GUI with a graph/nodes interface.

## Features

- Execute ComfyUI workflows directly from n8n
- Transform images using stable diffusion models
- **Process two input images into one output image (dual image processing)**
- **Generate videos from two input images** 
- **Generate audio from text prompts using ACE Step Audio models**
- Support for workflow JSON import
- Automatic output retrieval from workflow outputs
- Progress monitoring and error handling
- Support for API key authentication
- Configurable timeout settings
- Multiple input types: URL, Base64, Binary
- Support for various video formats (MP4, WebM, GIF)
- Support for various audio formats (MP3, WAV, OGG)

## Prerequisites

- n8n (version 1.0.0 or later)
- ComfyUI instance running and accessible
- Node.js 16 or newer
- For video generation: ComfyUI with AnimateDiff, SVD, or other video generation extensions
- For audio generation: ComfyUI with ACE Step Audio models and extensions

## Installation

### Standard Installation

```bash
# Install from npm package (recommended)
npm install n8n-nodes-comfyui-image-to-image@1.0.0

# Or install from git repository
npm install github:StudioExitt/n8n-nodes-comfyui-image-to-image
```

### Docker Installation

For Docker installations, you can use one of the following methods:

#### Method 1: Volume Mount
```bash
# Create a directory for custom nodes
mkdir -p /path/to/custom/nodes

# Clone the repository
git clone https://github.com/StudioExitt/n8n-nodes-comfyui-image-to-image.git /tmp/custom-nodes
cd /tmp/custom-nodes

# Install dependencies and build
npm install
npm run build

# Copy the built files to your custom nodes directory
cp -r dist/* /path/to/custom/nodes/n8n-nodes-comfyui-image-to-image/

# Run n8n with the custom nodes directory mounted
docker run -d \
  --name n8n \
  -p 5678:5678 \
  -v /path/to/custom/nodes:/home/node/.n8n/custom/nodes \
  n8nio/n8n
```

#### Method 2: Custom Docker Image
```dockerfile
# Dockerfile
FROM n8nio/n8n

# Install the custom nodes package from GitHub
RUN cd /tmp && \
    npm install github:StudioExitt/n8n-nodes-comfyui-image-to-image && \
    cp -r /tmp/node_modules/n8n-nodes-comfyui-image-to-image /home/node/.n8n/custom/nodes/ && \
    chown -R node:node /home/node/.n8n
```

Build and run:
```bash
docker build -t n8n-with-comfyui .
docker run -d --name n8n -p 5678:5678 n8n-with-comfyui
```

#### Method 3: Docker Compose
```yaml
version: '3'

services:
  n8n:
    image: n8nio/n8n
    container_name: n8n
    ports:
      - "5678:5678"
    volumes:
      - n8n_data:/home/node/.n8n
      - ./custom-nodes:/home/node/.n8n/custom/nodes
    environment:
      - N8N_PORT=5678
      - N8N_PROTOCOL=http
      - NODE_ENV=production

volumes:
  n8n_data:
```

Then:
```bash
# Clone the repository
git clone https://github.com/StudioExitt/n8n-nodes-comfyui-image-to-image.git /tmp/custom-nodes
cd /tmp/custom-nodes

# Install dependencies and build
npm install
npm run build

# Copy the built files to your custom nodes directory
mkdir -p ./custom-nodes/n8n-nodes-comfyui-image-to-image
cp -r dist/* ./custom-nodes/n8n-nodes-comfyui-image-to-image/

# Start the docker-compose setup
docker-compose up -d
```

## Node Types

### ComfyUI Image Transformer Node

This node allows you to transform and enhance images using ComfyUI's image-to-image capabilities.

### ComfyUI Dual Image Transformer Node

This node processes two input images and generates one output image using ComfyUI workflows. Perfect for image blending, comparison, fusion, and other dual-image operations.

#### Settings

- **API URL**: The URL of your ComfyUI instance (default: http://127.0.0.1:8188)
- **API Key**: Optional API key if authentication is enabled
- **Workflow JSON**: The ComfyUI workflow in JSON format for image transformation
- **Input Type**: Choose between URL, Base64, or Binary input methods
- **Input Image**: URL or base64 string of the input image (when using URL or Base64 input type)
- **Binary Property**: Name of the binary property containing the image (when using Binary input type)
- **Timeout**: Maximum time in minutes to wait for image transformation

#### Input

The node accepts an image input in three ways:
1. **URL**: Provide a direct URL to an image
2. **Base64**: Provide a base64-encoded image string
3. **Binary**: Use an image from a binary property in the workflow (e.g., from an HTTP Request node)

#### Outputs

The node outputs the transformed image:
- In the `binary.data` property with proper MIME type and file information
- `fileName`: Name of the transformed image file
- `data`: Base64 encoded image data
- `fileType`: The type of image file (e.g., 'image')
- `fileSize`: Size of the image in KB
- `fileExtension`: File extension (png, jpg, webp)
- `mimeType`: MIME type of the image

### ComfyUI Video Generator Node

This node generates videos from two input images using ComfyUI's video generation capabilities.

#### Settings

- **API URL**: The URL of your ComfyUI instance (default: http://127.0.0.1:8188)
- **API Key**: Optional API key if authentication is enabled
- **Workflow JSON**: The ComfyUI workflow in JSON format with video generation nodes (AnimateDiff, SVD, etc.)
- **First Image Input Type**: Choose between URL, Base64, or Binary for the first image
- **First Image**: URL or base64 string of the first input image
- **First Image Binary Property**: Name of the binary property containing the first image
- **Second Image Input Type**: Choose between URL, Base64, or Binary for the second image  
- **Second Image**: URL or base64 string of the second input image
- **Second Image Binary Property**: Name of the binary property containing the second image
- **First Image Node ID**: Node ID in workflow for the first LoadImage node (default: "load_image_1")
- **Second Image Node ID**: Node ID in workflow for the second LoadImage node (default: "load_image_2")
- **Video Frame Count**: Number of frames to generate for the video (default: 16)
- **Video Frame Rate**: Frame rate for the output video (default: 8 FPS)
- **Timeout**: Maximum time in minutes to wait for video generation (default: 60)

#### Input

The node accepts two image inputs, each can be provided in three ways:
1. **URL**: Provide direct URLs to images
2. **Base64**: Provide base64-encoded image strings
3. **Binary**: Use images from binary properties in the workflow

#### Outputs

The node outputs the generated video:
- In the `binary.data` property with proper MIME type and file information
- `fileName`: Name of the generated video file
- `data`: Base64 encoded video data
- `fileType`: The type of file ('video' or 'image' for GIF)
- `fileSize`: Size of the video in KB
- `fileExtension`: File extension (mp4, webm, gif, mov)
- `mimeType`: MIME type of the video
- `frameCount`: Number of frames in the video
- `frameRate`: Frame rate of the video
- `duration`: Duration of the video in seconds

### ComfyUI Audio Generator Node

This node generates audio from text prompts using ComfyUI's ACE Step Audio models.

#### Settings

- **API URL**: The URL of your ComfyUI instance (default: http://127.0.0.1:8188)
- **API Key**: Optional API key if authentication is enabled
- **Workflow JSON**: The ComfyUI workflow in JSON format for text-to-audio generation
- **Text Prompt**: Description of the audio you want to generate (e.g., "Jazz piano with smooth saxophone")
- **Audio Duration**: Duration of the generated audio in seconds (default: 180)
- **Audio Quality**: Bitrate quality of the output audio (64k, 128k, 192k, 256k, 320k)
- **Seed**: Random seed for generation (-1 for random)
- **Steps**: Number of sampling steps (default: 50)
- **CFG Scale**: CFG scale for guidance strength (default: 5)
- **Timeout**: Maximum time in minutes to wait for audio generation (default: 30)

#### Input

The node accepts a text prompt describing the desired audio output.

#### Outputs

The node outputs the generated audio:
- In the `binary.data` property with proper MIME type and file information
- `fileName`: Name of the generated audio file
- `data`: Base64 encoded audio data
- `fileType`: The type of file ('audio')
- `fileSize`: Size of the audio in KB
- `fileExtension`: File extension (mp3, wav, ogg, m4a)
- `mimeType`: MIME type of the audio
- `prompt`: The original text prompt used
- `duration`: Duration setting used for generation
- `quality`: Quality setting used for generation

## Usage Examples

### Using the ComfyUI Image Transformer Node

1. Create a workflow in ComfyUI for image transformation (e.g., img2img, inpainting, style transfer)
2. Export the workflow as JSON (API)
3. Add the ComfyUI Image Transformer node
4. Paste your workflow JSON
5. Select the appropriate Input Type:
   - For URL: Enter the image URL
   - For Base64: Provide a base64 string
   - For Binary: Specify the binary property containing the image (default: "data")
6. Configure timeout as needed
7. Execute the workflow to generate a transformed image from your input image

### Using the ComfyUI Dual Image Transformer Node

1. Create a workflow in ComfyUI for dual image processing (e.g., image blending, comparison, fusion)
2. Ensure your workflow contains at least 2 LoadImage nodes
3. Export the workflow as JSON (API)
4. Add the ComfyUI Dual Image Transformer node
5. Paste your workflow JSON
6. Configure both image inputs:
   - Set input types for each image (URL, Base64, or Binary)
   - Provide image sources for both images
   - Specify binary property names if using Binary input type
7. Configure timeout as needed
8. Execute the workflow to generate a single output image from your two input images

#### Dual Image Workflow Requirements

Your ComfyUI workflow should include:
- At least two `LoadImage` nodes (the first two will be used automatically)
- Image processing nodes for blending, comparison, or fusion (e.g., `ImageBlend`, `ControlNet`, `IPAdapter`)
- Output nodes like `SaveImage` or `PreviewImage`

Common use cases:
- **Image Blending**: Combine two images with different blend modes
- **Style Transfer**: Apply the style of one image to another
- **Face Swapping**: Swap faces between two portrait images
- **Background Replacement**: Replace the background of one image with another
- **Image Comparison**: Create side-by-side or overlay comparisons

### Using the ComfyUI Video Generator Node

1. Create a workflow in ComfyUI with video generation capabilities:
   - Install AnimateDiff, SVD, or other video generation extensions
   - Create a workflow with two LoadImage nodes (IDs: "load_image_1" and "load_image_2")
   - Add video generation nodes (AnimateDiffSampler, VHS_VideoCombine, etc.)
   - Export the workflow as JSON (API)
2. Add the ComfyUI Video Generator node
3. Paste your workflow JSON
4. Configure both image inputs:
   - Set input types (URL, Base64, or Binary)
   - Provide image sources
   - Verify node IDs match your workflow
5. Set video parameters:
   - Frame count (how many frames to generate)
   - Frame rate (FPS)
   - Timeout (video generation takes longer than images)
6. Execute the workflow to generate a video transitioning between your two input images

#### Example Video Workflow Requirements

Your ComfyUI workflow should include:
- Two `LoadImage` nodes with specific IDs
- Video generation nodes like:
  - `AnimateDiffLoader` + `AnimateDiffSampler`
  - `SVD_img2vid_Conditioning` for Stable Video Diffusion
  - `VHS_VideoCombine` for video output
  - `LatentInterpolate` for smooth transitions between images

See `image_to_video_example.json` for a complete workflow example.

### Using the ComfyUI Audio Generator Node

1. Create or obtain a workflow in ComfyUI for audio generation:
   - Install ACE Step Audio models and extensions
   - Create a workflow with text encoding and audio generation nodes
   - Include nodes like `TextEncodeAceStepAudio`, `EmptyAceStepLatentAudio`, `VAEDecodeAudio`, `SaveAudioMP3`
   - Export the workflow as JSON (API)
2. Add the ComfyUI Audio Generator node
3. Paste your workflow JSON
4. Configure audio generation parameters:
   - Enter your text prompt describing the desired audio
   - Set audio duration (in seconds)
   - Choose audio quality/bitrate
   - Adjust sampling parameters (seed, steps, CFG scale)
   - Set appropriate timeout (audio generation can take several minutes)
5. Execute the workflow to generate audio from your text prompt

#### Example Audio Workflow Requirements

Your ComfyUI workflow should include:
- `TextEncodeAceStepAudio` node for text prompt encoding
- `EmptyAceStepLatentAudio` node for latent audio space initialization
- `CheckpointLoaderSimple` with ACE Step Audio model (e.g., ace_step_v1_3.5b.safetensors)
- `KSampler` for the generation process
- `VAEDecodeAudio` for decoding latent audio to actual audio
- `SaveAudioMP3` (or other audio save nodes) for output

See `text_to_audio_example.json` for a complete workflow example.

## Error Handling

The node includes comprehensive error handling for:
- API connection issues
- Invalid workflow JSON
- Execution failures
- Timeout conditions
- Input image validation

## Development

```bash
# Install dependencies
npm install

# Build
npm run build

# Test
npm run test

# Lint
npm run lint
```

## License

[MIT](LICENSE.md)

---

# 한국어 문서

## n8n-nodes-comfyui-image-to-image

이 패키지는 [ComfyUI](https://github.com/comfyanonymous/ComfyUI)와 통합하는 n8n 노드를 제공합니다 - 그래프/노드 인터페이스가 있는 강력하고 모듈식 안정적인 확산 GUI입니다.

## 기능

- n8n에서 직접 ComfyUI 워크플로우 실행
- 안정적인 확산 모델을 사용하여 이미지 및 비디오 생성
- **두 개의 입력 이미지를 하나의 출력 이미지로 처리 (듀얼 이미지 처리)**
- **이미지에서 비디오 생성** 
- **텍스트에서 오디오 생성 (ACE Step Audio 모델 사용)**
- 워크플로우 JSON 가져오기 지원
- 워크플로우 출력에서 자동 출력 검색
- 진행 모니터링 및 오류 처리
- API 키 인증 지원
- 구성 가능한 타임아웃 설정
- 다중 입력 유형: URL, Base64, Binary
- 다양한 비디오 형식 지원 (MP4, WebM, GIF)
- 다양한 오디오 형식 지원 (MP3, WAV, OGG)

## 사전 요구 사항

- n8n (버전 1.0.0 이상)
- ComfyUI 인스턴스가 실행 중이고 접근 가능
- Node.js 16 이상
- 비디오 생성을 위해: ComfyUI with AnimateDiff, SVD, 또는 기타 비디오 생성 확장 기능
- 오디오 생성을 위해: ComfyUI with ACE Step Audio 모델과 확장 기능

## 설치

### 표준 설치

```bash
# Install from npm package (recommended)
npm install n8n-nodes-comfyui-image-to-image@1.0.0

# Or install from git repository
npm install github:StudioExitt/n8n-nodes-comfyui-image-to-image
```

### 도커 설치

도커 설치의 경우 다음 방법 중 하나를 사용할 수 있습니다:

#### 방법 1: 볼륨 마운트
```bash
# 커스텀 노드를 위한 디렉토리 생성
mkdir -p /path/to/custom/nodes

# 저장소 복제
git clone https://github.com/StudioExitt/n8n-nodes-comfyui-image-to-image.git /tmp/custom-nodes
cd /tmp/custom-nodes

# 의존성 설치 및 빌드
npm install
npm run build

# 빌드된 파일을 커스텀 노드 디렉토리로 복사
cp -r dist/* /path/to/custom/nodes/n8n-nodes-comfyui-image-to-image/

# 커스텀 노드 디렉토리를 마운트하여 n8n 실행
docker run -d \
  --name n8n \
  -p 5678:5678 \
  -v /path/to/custom/nodes:/home/node/.n8n/custom/nodes \
  n8nio/n8n
```

#### 방법 2: 커스텀 도커 이미지
```dockerfile
# Dockerfile
FROM n8nio/n8n

# GitHub에서 커스텀 노드 패키지 설치
RUN cd /tmp && \
    npm install github:StudioExitt/n8n-nodes-comfyui-image-to-image && \
    cp -r /tmp/node_modules/n8n-nodes-comfyui-image-to-image /home/node/.n8n/custom/nodes/ && \
    chown -R node:node /home/node/.n8n
```

빌드 및 실행:
```bash
docker build -t n8n-with-comfyui .
docker run -d --name n8n -p 5678:5678 n8n-with-comfyui
```

#### 방법 3: 도커 컴포즈
```yaml
version: '3'

services:
  n8n:
    image: n8nio/n8n
    container_name: n8n
    ports:
      - "5678:5678"
    volumes:
      - n8n_data:/home/node/.n8n
      - ./custom-nodes:/home/node/.n8n/custom/nodes
    environment:
      - N8N_PORT=5678
      - N8N_PROTOCOL=http
      - NODE_ENV=production

volumes:
  n8n_data:
```

그리고:
```bash
# 저장소 복제
git clone https://github.com/StudioExitt/n8n-nodes-comfyui-image-to-image.git /tmp/custom-nodes
cd /tmp/custom-nodes

# 의존성 설치 및 빌드
npm install
npm run build

# 빌드된 파일을 커스텀 노드 디렉토리로 복사
mkdir -p ./custom-nodes/n8n-nodes-comfyui-image-to-image
cp -r dist/* ./custom-nodes/n8n-nodes-comfyui-image-to-image/

# 도커 컴포즈 설정 시작
docker-compose up -d
```

## 노드 유형

### ComfyUI Image Transformer Node

이 노드를 사용하면 ComfyUI의 이미지-이미지 변환 기능을 사용하여 이미지를 변환하거나 개선할 수 있습니다.

#### Settings

- **API URL**: The URL of your ComfyUI instance (default: http://127.0.0.1:8188)
- **API Key**: Optional API key if authentication is enabled
- **Workflow JSON**: The ComfyUI workflow in JSON format for image transformation
- **Input Type**: Choose between URL, Base64, or Binary input methods
- **Input Image**: URL or base64 string of the input image (when using URL or Base64 input type)
- **Binary Property**: Name of the binary property containing the image (when using Binary input type)
- **Timeout**: Maximum time in minutes to wait for image transformation

#### Input

The node accepts an image input in three ways:
1. **URL**: Provide a direct URL to an image
2. **Base64**: Provide a base64-encoded image string
3. **Binary**: Use an image from a binary property in the workflow (e.g., from an HTTP Request node)

#### Outputs

The node outputs the transformed image:
- In the `binary.data` property with proper MIME type and file information
- `fileName`: Name of the transformed image file
- `data`: Base64 encoded image data
- `fileType`: The type of image file (e.g., 'image')
- `fileSize`: Size of the image in KB
- `fileExtension`: File extension (png, jpg, webp)
- `mimeType`: MIME type of the image

### ComfyUI Video Generator Node

This node generates videos from two input images using ComfyUI's video generation capabilities.

#### Settings

- **API URL**: The URL of your ComfyUI instance (default: http://127.0.0.1:8188)
- **API Key**: Optional API key if authentication is enabled
- **Workflow JSON**: The ComfyUI workflow in JSON format with video generation nodes (AnimateDiff, SVD, etc.)
- **First Image Input Type**: Choose between URL, Base64, or Binary for the first image
- **First Image**: URL or base64 string of the first input image
- **First Image Binary Property**: Name of the binary property containing the first image
- **Second Image Input Type**: Choose between URL, Base64, or Binary for the second image  
- **Second Image**: URL or base64 string of the second input image
- **Second Image Binary Property**: Name of the binary property containing the second image
- **First Image Node ID**: Node ID in workflow for the first LoadImage node (default: "load_image_1")
- **Second Image Node ID**: Node ID in workflow for the second LoadImage node (default: "load_image_2")
- **Video Frame Count**: Number of frames to generate for the video (default: 16)
- **Video Frame Rate**: Frame rate for the output video (default: 8 FPS)
- **Timeout**: Maximum time in minutes to wait for video generation (default: 60)

#### Input

The node accepts two image inputs, each can be provided in three ways:
1. **URL**: Provide direct URLs to images
2. **Base64**: Provide base64-encoded image strings
3. **Binary**: Use images from binary properties in the workflow

#### Outputs

The node outputs the generated video:
- In the `binary.data` property with proper MIME type and file information
- `fileName`: Name of the generated video file
- `data`: Base64 encoded video data
- `fileType`: The type of file ('video' or 'image' for GIF)
- `fileSize`: Size of the video in KB
- `fileExtension`: File extension (mp4, webm, gif, mov)
- `mimeType`: MIME type of the video
- `frameCount`: Number of frames in the video
- `frameRate`: Frame rate of the video
- `duration`: Duration of the video in seconds

## 사용 예제

### ComfyUI Image Transformer Node 사용하기

1. ComfyUI에서 이미지 변환을 위한 워크플로우 생성(예: img2img, inpainting, style transfer)
2. 워크플로우를 JSON으로 내보내기(API)
3. ComfyUI Image Transformer node 추가
4. 워크플로우 JSON 붙여넣기
5. 적절한 입력 유형 선택:
   - For URL: Enter the image URL
   - For Base64: Provide a base64 string
   - For Binary: Specify the binary property containing the image (default: "data")
6. 필요에 따라 타임아웃 구성
7. 워크플로우를 실행하여 입력 이미지에서 변환된 이미지 생성 

### ComfyUI Dual Image Transformer Node 사용하기

1. ComfyUI에서 듀얼 이미지 처리를 위한 워크플로우 생성(예: 이미지 블렌딩, 비교, 융합)
2. 워크플로우에 최소 2개의 LoadImage 노드가 포함되어 있는지 확인
3. 워크플로우를 JSON으로 내보내기(API)
4. ComfyUI Dual Image Transformer node 추가
5. 워크플로우 JSON 붙여넣기
6. 두 이미지 입력 구성:
   - 각 이미지의 입력 유형 설정(URL, Base64, 또는 Binary)
   - 두 이미지의 소스 제공
   - Binary 입력 유형 사용 시 바이너리 속성 이름 지정
7. 필요에 따라 타임아웃 구성
8. 워크플로우를 실행하여 두 입력 이미지에서 하나의 출력 이미지 생성

#### 듀얼 이미지 워크플로우 요구 사항

ComfyUI 워크플로우는 다음을 포함해야 합니다:
- 최소 두 개의 `LoadImage` 노드 (처음 두 개가 자동으로 사용됨)
- 블렌딩, 비교, 또는 융합을 위한 이미지 처리 노드 (예: `ImageBlend`, `ControlNet`, `IPAdapter`)
- `SaveImage` 또는 `PreviewImage`와 같은 출력 노드

일반적인 사용 사례:
- **이미지 블렌딩**: 다양한 블렌드 모드로 두 이미지 결합
- **스타일 전송**: 한 이미지의 스타일을 다른 이미지에 적용
- **얼굴 교체**: 두 인물 사진 간의 얼굴 교체
- **배경 교체**: 한 이미지의 배경을 다른 이미지로 교체
- **이미지 비교**: 나란히 또는 오버레이 비교 생성

### ComfyUI Video Generator Node 사용하기

1. ComfyUI에서 비디오 생성 기능을 포함한 워크플로우 생성:
   - AnimateDiff, SVD, 또는 기타 비디오 생성 확장 기능 설치
   - 두 개의 LoadImage 노드(IDs: "load_image_1" 및 "load_image_2")를 포함한 워크플로우 생성
   - 비디오 생성 노드(AnimateDiffSampler, VHS_VideoCombine 등) 추가
   - 워크플로우를 JSON으로 내보내기(API)
2. ComfyUI Video Generator node 추가
3. 워크플로우 JSON 붙여넣기
4. 두 이미지 입력 구성:
   - 입력 유형(URL, Base64, 또는 Binary) 설정
   - 이미지 소스 제공
   - 워크플로우 노드 ID 확인
5. 비디오 파라미터 설정:
   - 프레임 수(생성할 프레임 수)
   - 프레임 속도(FPS)
   - 타임아웃(이미지보다 비디오 생성이 더 오래 걸림)
6. 워크플로우를 실행하여 두 입력 이미지 사이를 전환하는 비디오 생성 

#### 예제 비디오 워크플로우 요구 사항

ComfyUI 워크플로우는 다음을 포함해야 합니다:
- 특정 ID를 가진 두 개의 `LoadImage` 노드
- 비디오 생성 노드 예:
  - `AnimateDiffLoader` + `AnimateDiffSampler`
  - `SVD_img2vid_Conditioning` for Stable Video Diffusion
  - `VHS_VideoCombine` for video output
  - `LatentInterpolate` for smooth transitions between images

`image_to_video_example.json`을 참조하여 완전한 워크플로우 예제 확인 