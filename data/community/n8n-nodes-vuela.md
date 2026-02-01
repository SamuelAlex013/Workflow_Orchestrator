# n8n-nodes-vuela

<div align="center">
  <img src="https://vuela.ai/logo.png" alt="Vuela AI" width="200"/>
  <h3>Nodo de n8n para Vuela AI</h3>
  <p>Creado por <a href="https://va360.pro">Valen - VA360.pro</a> en colaboración con <a href="https://vuela.ai">Vuela.ai</a></p>
</div>

---

This is an n8n community node. It lets you use Vuela AI in your n8n workflows.

[Vuela AI](https://vuela.ai) es una poderosa plataforma de IA para generar contenido y videos de alta calidad usando inteligencia artificial.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## 🎓 ¿Quieres aprender a crear tus propios nodos de n8n?

> **Únete a [VA360.pro](https://va360.pro)** - La mayor comunidad de IA y automatizaciones de habla hispana. 
> 
> En VA360.pro encontrarás:
> - 📚 Tutoriales paso a paso para crear nodos de n8n
> - 🤝 Una comunidad activa de automatizadores
> - 🎯 Casos de uso reales y ejemplos prácticos
> - 🚀 Las últimas novedades en IA y automatización
> - 💡 Soporte directo de expertos
>
> **[¡Entra ahora en VA360.pro!](https://va360.pro)**

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

1. Go to **Settings > Community Nodes**
2. Select **Install**
3. Enter `n8n-nodes-vuela` in the field
4. Select **Install**

## Operations

### Authentication
- **Validate Token** - Validate your API token

### Content
- **Generate Article** - Generate AI-powered articles with customizable parameters
- **Get** - Retrieve a specific content by ID
- **Get Many** - List all your contents with filtering options

### Video
- **Generate** - Create videos in three modes:
  - **Single Voice**: One narrator throughout the video
  - **Scenes**: Multiple characters with scene-based dialogues
  - **Avatar**: Virtual presenter mode
- **Get** - Retrieve a specific video by ID
- **Get Many** - List all your videos

### Project
- **Get** - Retrieve a specific project by ID
- **Get Many** - List all your projects

## Credentials

To use this node, you need:

1. A Vuela AI account
2. An API token from your Vuela dashboard

### Getting your API Token

1. Log in to your [Vuela AI dashboard](https://app.vuela.ai)
2. Navigate to API settings
3. Generate or copy your API token
4. In n8n, add new credentials:
   - Select "Vuela AI API" 
   - Paste your API token
   - Click "Save"

## Usage Examples

### Generate an Article

```json
{
  "resource": "content",
  "operation": "generateArticle",
  "title": "10 Ways AI is Transforming Business",
  "language": "en",
  "country": "US",
  "additionalFields": {
    "focus": "productivity and automation",
    "add_internal_links": true
  }
}
```

### Generate a Video

```json
{
  "resource": "video",
  "operation": "generate",
  "mode": "single_voice",
  "video_script": "Welcome to our AI tutorial. Today we'll explore how artificial intelligence is transforming modern business.",
  "language": "en",
  "country": "US",
  "aspect_ratio": "16:9",
  "voice_id": "21m00Tcm4TlvDq8ikWAM",
  "animation_type": "moving_image",
  "add_subtitles": true
}
```

## Features

- **Easy to Use**: User-friendly dropdowns for all major settings
- **Multi-language Support**: 14+ languages and 20+ countries
- **Voice Library**: 20+ pre-configured voices in multiple languages
- **Avatar Support**: 10+ diverse AI avatars for video generation
- **Professional Styling**: 35+ visual styles and 15+ background music tracks
- **Custom Options**: Advanced users can use custom IDs for voices, avatars, and music

## Documentation

For detailed documentation, examples, and advanced usage, visit:
- [Complete Documentation](./DOCUMENTATION.md)
- [Vuela.ai API Documentation](https://docs.vuela.ai)

## Support & Community

- **Issues**: Report bugs or request features on [GitHub Issues](https://github.com/vuela-ai/n8n-node-vuela/issues)
- **Community**: Join the [VA360.pro community](https://va360.pro) for support and discussions
- **Tutorials**: Learn more about n8n automation at [VA360.pro](https://va360.pro)

## About the Creator

**Valen** - Creador de contenido especializado en IA y automatizaciones

- **Twitter**: [@Valen](https://twitter.com/Valen)
- **Instagram**: [@valentin_ayesa](https://instagram.com/valentin_ayesa)
- **Website**: [VA360.pro](https://va360.pro)
- **LinkedIn**: [Valentín Ayesa](https://linkedin.com/in/valentin-ayesa)

### Learn More

¿Quieres aprender a crear tus propios nodos de n8n como este? 

**[Únete a VA360.pro](https://va360.pro)** - La mayor comunidad de IA y automatizaciones en español donde encontrarás:

- Tutoriales paso a paso
- Comunidad activa de automatizadores
- Casos de uso reales
- Las últimas novedades en IA
- Soporte directo de expertos

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Vuela.ai](https://vuela.ai) por proporcionar la increíble API de IA
- [n8n](https://n8n.io) por la fantástica plataforma de automatización
- La comunidad de [VA360.pro](https://va360.pro) por el feedback y soporte

---

<div align="center">
  <p><strong>Creado con ❤️ por <a href="https://va360.pro">Valen - VA360.pro</a></strong></p>
  <p>Twitter: <a href="https://twitter.com/Valen">@Valen</a> | Instagram: <a href="https://instagram.com/valentin_ayesa">@valentin_ayesa</a> | Website: <a href="https://va360.pro">VA360.pro</a></p>
</div>