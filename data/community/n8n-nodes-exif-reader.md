# n8n EXIF Reader Node

A custom n8n node to extract EXIF metadata from images.

## Features

- Extract EXIF data from images in binary format or via URL
- Structured JSON output with organized metadata categories
- Support for GPS coordinates (with decimal conversion)
- Camera and lens information extraction
- Exposure settings (aperture, shutter speed, ISO)
- Timestamp handling with ISO 8601 conversion
- Configurable output options

## Installation

```bash
npm install n8n-nodes-exif-reader
```

## Usage

### Input Sources

The node supports two input methods:

1. **Binary Data**: Read image data from a binary property in the input data
2. **URL**: Download image directly from a URL

### Configuration Options

- **Input Source**: Choose between binary data or URL input
- **Binary Property**: Name of the binary property containing image data (for binary input)
- **Image URL**: URL of the image to process (for URL input)
- **Output Property**: Name of the property where EXIF data will be stored (default: "exif")
- **Include GPS Data**: Whether to include GPS coordinates if available
- **Include Image Size**: Whether to include image dimensions
- **Convert Timestamps**: Whether to convert EXIF timestamps to ISO 8601 format

### Output Structure

The node outputs structured JSON with the following categories:

```json
{
  "exif": {
    "fileInfo": {
      "fileName": "IMG_1234.jpg",
      "fileSizeBytes": 2048576,
      "fileSizeFormatted": "2 MB"
    },
    "imageSize": {
      "width": 3024,
      "height": 4032
    },
    "camera": {
      "make": "Apple",
      "model": "iPhone 12 Pro",
      "software": "14.4"
    },
    "lens": {
      "model": "iPhone 12 Pro back triple camera 5.1mm f/1.6",
      "focalLength": "5.1mm"
    },
    "exposure": {
      "shutterSpeed": "1/120",
      "aperture": "f/1.6",
      "iso": 64,
      "mode": "Auto",
      "flash": "Did not fire"
    },
    "gps": {
      "latitude": 37.7749,
      "longitude": -122.4194,
      "latitudeDecimal": 37.7749,
      "longitudeDecimal": -122.4194
    },
    "timestamp": {
      "original": 1640995200,
      "iso": "2022-01-01T12:00:00.000Z",
      "formatted": "1/1/2022, 12:00:00 PM"
    },
    "raw": {
      // Complete raw EXIF data
    }
  }
}
```

## Use Cases

- **Photo Management**: Organize photos by camera, date, or location
- **Workflow Automation**: Trigger different flows based on image metadata
- **Data Analysis**: Extract and analyze photography patterns
- **Content Processing**: Enhance media workflows with metadata-driven decisions
- **Location Services**: Use GPS data from images for mapping applications

## Error Handling

The node includes comprehensive error handling:
- Validates input data availability
- Handles network errors for URL downloads
- Gracefully handles images without EXIF data
- Supports "Continue on Fail" mode for batch processing

## Development

To work on this node locally:

1. Clone the repository
2. Run `npm install`
3. Build with `npm run build`
4. Test with `npm run lint`

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
