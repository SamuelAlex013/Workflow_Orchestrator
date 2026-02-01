> **Currently in BETA and under active development.**

![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-useapi

This n8n community node enables seamless integration of **[useapi.net](http://useapi.net) in your [n8n](https://n8n.io) workflows**.

Implementing in this nodes the following services, via the useapi.net API:
- Midjourney
- Runway
- MiniMax
- Pika (not started yet)
- Riffusion (not started yet)
- Mureka (not started yet)
- PixVerse (not started yet)
- InsightFaceSwap (not started yet)


## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## More information

You need to set up and configure the Midjourney, Mureka, Runway, InsightFaceSwap, Pika or PixVerse as well as subscribe to useapi.net service before you can start using this experimental API. 

I am not affiliated in any way with useapi.net. Drop me a note if you have any questions. I will try to help and add new features as soon as possible.

## Features

### Runway
- **Task checker**: Check the status of a task.
- **Image to video**: Convert images into videos with RunwayML RunGen3 Turbo
- **Describe image**: Describe an image using RunwayML's image captioning model.
- **Assets listing**: List all assets available on RunwayML.
- **Video to video (experimental)**: Convert a video into another video using RunwayML RunGen3 Turbo.
- **Lipsync**: Generate lip sync animation using RunwayML's lip sync model.
- **Instant image generation**: Generate an image using RunwayML's Instant Generation model.

### Midjourney
- **Imagine**: Generate images using Midjourney.
- **Retrieve job status**: Retrieve the status of a job.
- **Upscale**: Upscale an image using Midjourney.

### Minimax
- **Create video**: Create a video using Minimax.
- **Retrieve video**: Get a video using Minimax.
- **Upload a file**: Upload a file to Minimax.

## Credentials

You will need an API key from useapi.net to use this node. Add the API key to the credentials section in the settings of the node.

## Version history

### 0.2.2
- Move some constants to shared external file to reuse in other nodes.
- Minimax Create, Get, Delete images.
- Now in Create video will load models based on Input Type.

### 0.2.1
- Updated axios in n8n-workflow

### 0.2.0
- Updated packages to latest.
- Updated codes to new packages.

### 0.1.9
- Updated readme.

### 0.1.8
- Gulp to v 5.0

### 0.1.7
- Small bugs fixed.

### 0.1.6
- MidJourney Imagine, Button U1, U2 etc, Get Job Status.

### 0.1.5
- Renamed nodes to be more easy to regognize.
- Added create account in UseNet APi as needed, to not create online.
- Started to add Minimax nodes (Create video and Get video).

### 0.1.3
- Text2Image node added.
- Lipsync node added.
- Gen-3 Alpha Turbo Video to Video node added.

### 0.1.2
Initial version, RunwayML integrated with some services.

## Compatibility

1.80.0 and above

## License

[MIT](https://github.com/n8n-io/n8n-nodes-useapi/blob/master/LICENSE.md)
