# n8n Kodi Node

A powerful n8n community node for controlling Kodi media center through JSON-RPC API with intelligent method discovery and comprehensive media management capabilities.

## 🎯 Features

### **Dynamic Method Discovery**
- **Automatic Discovery**: Automatically discovers available JSON-RPC methods from your Kodi instance
- **JSON-RPC Introspection**: Uses Kodi's built-in `JSONRPC.Introspect` for accurate method information
- **Fallback Methods**: Comprehensive fallback to 40+ common Kodi methods if discovery fails
- **Smart Caching**: Efficient method caching with force refresh options

### **Three Core Operations**
1. **Execute Method**: Run specific Kodi methods with dynamic dropdown selection
2. **Raw JSON-RPC**: Send custom JSON-RPC commands for advanced users
3. **Discover Methods**: Automatically find and categorize available methods

### **Comprehensive Method Coverage**
- **Video Library**: Scan, clean, query movies, TV shows, episodes, music videos
- **Audio Library**: Manage audio content, albums, artists, songs
- **Player Control**: Play, pause, stop, seek, speed control
- **System Operations**: Shutdown, reboot, hibernate, suspend
- **Application Control**: Volume, notifications, window management
- **File Management**: Directory browsing, file details, media sources
- **Addon Management**: Install, configure, execute addons
- **GUI Control**: Notifications, window activation, properties

### **User Experience**
- **Category Organization**: Methods automatically organized by functional category
- **"All" Option**: View all methods across categories for power users
- **Method Descriptions**: Human-readable descriptions for each available method
- **Error Handling**: Comprehensive error handling with clear messages
- **Result Processing**: Intelligent result formatting for workflow integration

## 🚀 Installation

### **n8n Community Nodes**
```bash
npm install n8n-nodes-kodi
```

### **Manual Installation**
1. Clone this repository
2. Run `npm install`
3. Build with `npm run build`
4. Copy the `dist` folder to your n8n custom nodes directory

## 🔧 Configuration

### **Credentials Setup**
Create a new Kodi credential with:
- **Host**: Kodi server IP address or hostname
- **Port**: HTTP port (default: 8080)
- **Username**: HTTP username (if authentication enabled)
- **Password**: HTTP password (if authentication enabled)
- **Enable Discovery**: Toggle for dynamic method discovery
- **Discovery Timeout**: Timeout for discovery operations

### **Node Configuration**
1. **Operation**: Choose between Execute Method, Raw JSON-RPC, or Discover Methods
2. **Method Category**: Select from discovered categories or "All"
3. **Method**: Choose specific method from the selected category
4. **Raw JSON-RPC**: Custom JSON-RPC payload for advanced operations
5. **Options**: Force discovery refresh and include method information

## 📖 Usage Examples

### **Basic Video Library Scan**
```json
{
  "operation": "execute",
  "methodCategory": "VideoLibrary",
  "method": "VideoLibrary.Scan"
}
```

### **Get All Movies**
```json
{
  "operation": "execute",
  "methodCategory": "VideoLibrary",
  "method": "VideoLibrary.GetMovies"
}
```

### **Player Control**
```json
{
  "operation": "execute",
  "methodCategory": "Player",
  "method": "Player.PlayPause"
}
```

### **Custom JSON-RPC**
```json
{
  "operation": "raw",
  "rawPayload": {
    "jsonrpc": "2.0",
    "method": "Application.SetVolume",
    "params": {"volume": 50},
    "id": "n8n"
  }
}
```

### **Method Discovery**
```json
{
  "operation": "discover",
  "options": {
    "forceDiscovery": true,
    "includeMethodInfo": true
  }
}
```

## 🔍 Method Categories

### **VideoLibrary**
- `VideoLibrary.Scan` - Scan for new video content
- `VideoLibrary.Clean` - Clean video library
- `VideoLibrary.GetMovies` - Retrieve all movies
- `VideoLibrary.GetTVShows` - Get TV show list
- `VideoLibrary.GetEpisodes` - Get episode information
- `VideoLibrary.GetMusicVideos` - Retrieve music videos

### **AudioLibrary**
- `AudioLibrary.Scan` - Scan for new audio content
- `AudioLibrary.GetAlbums` - Retrieve album collection
- `AudioLibrary.GetArtists` - Get artist information
- `AudioLibrary.GetSongs` - Retrieve song library

### **Player Control**
- `Player.GetActivePlayers` - Check active players
- `Player.PlayPause` - Toggle play/pause
- `Player.Stop` - Stop playback
- `Player.Seek` - Seek to position
- `Player.SetSpeed` - Adjust playback speed

### **System Operations**
- `System.GetProperties` - Get system information
- `System.Shutdown` - Power off system
- `System.Reboot` - Restart system
- `System.Suspend` - Suspend system

### **Application Control**
- `Application.SetVolume` - Adjust volume
- `Application.Quit` - Exit Kodi
- `Application.Notify` - Show notifications

## 🏗️ Architecture

### **Core Components**
- **Kodi Node**: Main n8n node implementation with dynamic UI
- **KodiService**: Service layer for JSON-RPC communication
- **Method Discovery**: Intelligent method detection and categorization
- **Error Handling**: Comprehensive error management and user feedback

### **Technical Features**
- **TypeScript**: Full type safety and modern JavaScript features
- **Async/Await**: Non-blocking operations for better performance
- **Error Boundaries**: Graceful fallbacks when operations fail
- **Memory Management**: Efficient caching with cleanup mechanisms

## 🧪 Testing

### **Build Verification**
```bash
npm run build    # TypeScript compilation
npm run lint     # Code quality checks
npm run test     # Run test suite (if available)
```

### **Workflow Testing**
1. Create a simple workflow with the Kodi node
2. Configure credentials and test connection
3. Try different operations and verify results
4. Test error scenarios and edge cases

## 🤝 Contributing

### **Development Setup**
1. Fork the repository
2. Install dependencies: `npm install`
3. Make your changes
4. Run tests: `npm run build && npm run lint`
5. Submit a pull request

### **Code Standards**
- Follow TypeScript best practices
- Maintain comprehensive JSDoc comments
- Ensure all linting rules pass
- Test with multiple Kodi versions

## 📋 Requirements

- **n8n**: Version 1.82.0 or higher
- **Node.js**: Version 20.15 or higher
- **Kodi**: Version 18+ (Leia) or higher
- **Network**: HTTP access to Kodi instance

## 🔒 Security

- **Authentication**: Supports HTTP Basic Authentication
- **Network Security**: Works with HTTPS if configured
- **Credential Storage**: Secure credential management through n8n
- **Input Validation**: Comprehensive input sanitization and validation

## 📚 Resources

- [Kodi JSON-RPC API Documentation](https://kodi.wiki/view/JSON-RPC_API)
- [n8n Community Nodes Guide](https://docs.n8n.io/integrations/community-nodes/)
- [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 🙏 Acknowledgments

- **Kodi Team**: For the excellent JSON-RPC API
- **n8n Community**: For the robust node framework
- **Contributors**: For feedback, testing, and improvements

---

**Version**: 0.3.0  
**Last Updated**: August 2025  
**Maintainer**: Philipp Mundhenk
