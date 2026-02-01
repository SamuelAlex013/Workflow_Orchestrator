# n8n-nodes-ifc-extractor

This is an n8n community node that provides three powerful tools for working with IFC (Industry Foundation Classes) files and 3D models:

1. **IFC Extractor**: Extract information, elements, and properties from IFC files
2. **IFC to GLB Converter**: Convert IFC files to GLB (GLTF Binary) format for 3D visualization
3. **GLB Analyzer**: Analyze GLB files and calculate detailed geometry properties for building elements

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-ifc-extractor` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes.
5. Select **Install**.

After installation, the **IFC Extractor**, **IFC to GLB Converter**, and **GLB Analyzer** nodes will be available in your n8n instance.

## IFC Extractor Node

### Operations

#### Extract All Elements
Extracts all elements from the IFC file and returns them with their types and data. Optionally includes resolved properties from property sets.

#### Extract by Type
Extracts only elements of a specific IFC type (e.g., IFCWALL, IFCDOOR, IFCWINDOW, etc.). Optionally includes resolved properties from property sets.

#### Extract Elements with Properties
Specialized operation that extracts elements and automatically resolves their properties using IFC relationships (IfcRelDefinesByProperties). Returns only elements that have properties attached.

#### Get File Info
Returns basic information about the IFC file, including total element count and statistics by type.

#### Extract Properties
Extracts detailed properties for specific elements by their IDs.

### Configuration

#### Input Data Source
- **Binary Data**: Use binary data from a previous node (e.g., from HTTP Request or Read Binary File nodes)
- **File Path**: Specify a direct file path to the IFC file

#### Parameters
- **Include Properties**: Whether to automatically resolve and include element properties (for Extract All/By Type operations)
- **IFC Type**: When using "Extract by Type", specify the IFC entity type (e.g., IFCWALL, IFCDOOR)
- **Filter Elements**: When using "Extract Elements with Properties", specify comma-separated IFC types to include (leave empty for all)
- **Element IDs**: When using "Extract Properties", provide comma-separated element IDs
- **Binary Property**: Name of the binary property containing the IFC data (default: "data")
- **File Path**: Direct path to the IFC file when using file path input

### Property Resolution

The node can automatically resolve element properties by following IFC relationships:

- **IfcRelDefinesByProperties**: Links elements to property sets
- **IfcPropertySet**: Contains groups of properties
- **IfcPropertySingleValue**: Individual property values
- **IfcPropertyEnumeratedValue**: Properties with enumerated values
- **IfcPropertyListValue**: Properties with multiple values
- **IfcPropertyBoundedValue**: Properties with upper/lower bounds

Properties are organized by property set name and include:
- Property name and description
- Property value (with proper type conversion)
- Property units (when available)
- Property type information

### Usage Examples

#### Example 1: Extract All Walls from an IFC File
1. Use **HTTP Request** node to download an IFC file
2. Connect to **IFC Extractor** node
3. Set operation to "Extract by Type"
4. Set IFC Type to "IFCWALL"
5. Set Input Data Source to "Binary Data"

#### Example 2: Get File Statistics
1. Use **Read Binary File** node to read a local IFC file
2. Connect to **IFC Extractor** node
3. Set operation to "Get File Info"
4. Set Input Data Source to "Binary Data"

#### Example 3: Extract Properties for Specific Elements
1. First run "Extract All Elements" or "Extract by Type" to get element IDs
2. Use another **IFC Extractor** node
3. Set operation to "Extract Properties"
4. Enter the element IDs you want to analyze

### Common IFC Types

Here are some common IFC entity types you can extract:

- `IFCWALL` - Walls
- `IFCDOOR` - Doors  
- `IFCWINDOW` - Windows
- `IFCSLAB` - Slabs (floors, ceilings)
- `IFCBEAM` - Beams
- `IFCCOLUMN` - Columns
- `IFCSTAIR` - Stairs
- `IFCRAILING` - Railings
- `IFCFURNISHINGELEMENT` - Furniture
- `IFCSPACE` - Spaces/rooms
- `IFCBUILDING` - Building information
- `IFCBUILDINGSTOREY` - Building stories/floors

### Output

The node returns JSON data with the following structure:

```json
{
  "operation": "extractByType",
  "result": {
    "type": "IFCWALL",
    "count": 25,
    "elements": [
      {
        "id": 123,
        "type": "IFCWALL",
        "data": { /* IFC element data */ }
      }
    ]
  }
}
```

### Error Handling

The node includes comprehensive error handling:
- Invalid IFC files will return an error message
- Missing elements will be skipped with warnings
- Unknown IFC types will return an error
- Network issues when fetching files will be caught

Enable "Continue on Fail" in the node settings to handle errors gracefully in your workflow.

## IFC to GLB Converter Node

The IFC to GLB Converter node transforms IFC files into GLB (GLTF Binary) format, making them suitable for 3D visualization in web browsers, game engines, and other 3D applications.

### Operations

#### Convert to GLB
Converts IFC geometry and materials to GLB format with comprehensive options for optimization and quality control.

### Configuration

#### Input Data Source
- **Input Data**: Use IFC binary data from input (from previous nodes like HTTP Request or Read Binary File)
- **Binary Property**: Use IFC data from a specific binary property name

#### Output Options
- **Include Geometry**: Whether to include 3D mesh geometry in the output (default: true)
- **Include Materials**: Whether to include material information and colors (default: true)
- **Compression**: Choose compression method:
  - None: No compression (fastest)
  - GZIP: Standard compression
  - Draco: Advanced geometry compression (smallest file size)
- **Precision**: Geometric precision level (0.001-1.0, lower = higher compression)
- **Output Format**: 
  - GLB (Binary): Recommended for most use cases
  - GLTF (JSON): Human-readable format with separate asset files

### Output Data

The node returns both binary GLB data and metadata:

```json
{
  "binary": {
    "data": {
      "data": "base64-encoded GLB data",
      "mimeType": "model/gltf-binary",
      "fileName": "model.glb",
      "fileSize": "1024000"
    }
  },
  "json": {
    "success": true,
    "meshCount": 156,
    "vertexCount": 45230,
    "fileSize": 1024000,
    "materialCount": 12,
    "metadata": {
      "generatedAt": "2025-01-05T12:00:00.000Z",
      "options": { /* conversion options */ },
      "threejsVersion": "158"
    }
  }
}
```

### Usage Examples

1. **Basic IFC to GLB Conversion**:
   - HTTP Request node to fetch IFC file
   - IFC to GLB Converter node (default settings)
   - HTTP Response node to serve GLB file

2. **Optimized Web Viewing**:
   - Read Binary File node for local IFC
   - IFC to GLB Converter with Draco compression and reduced precision
   - Write Binary File node to save optimized GLB

- Use Draco compression for web delivery to reduce file sizes by 50-90%
- Reduce precision (0.01-0.1) for architectural visualization where exact measurements aren't critical
- Disable materials if only geometry is needed to reduce file size
- Process large IFC files in chunks by element types for better performance

## GLB Analyzer Node

The GLB Analyzer node provides comprehensive geometric analysis of GLB (GLTF Binary) files, calculating detailed properties for each building element including volume, surface areas, perimeters, orientations, and dimensions.

### Features

The node analyzes each mesh in a GLB file and calculates:

1. **Volume**: Total volume of each element using signed tetrahedron calculation
2. **Face Areas**: Surface area breakdown by orientation:
   - Top faces (upward-facing surfaces)
   - Bottom faces (downward-facing surfaces)
   - Left faces (left-facing surfaces)
   - Right faces (right-facing surfaces)
   - Front faces (forward-facing surfaces)
   - Back faces (backward-facing surfaces)
3. **Face Perimeters**: Perimeter length of each individual face
4. **Face Orientations**: Angle from horizontal plane (in degrees) for each face
5. **Dimensions**: Width, height, and depth measurements
6. **Bounding Box**: 3D spatial bounds of each element

### Configuration

#### Input Options
- **GLB File**: Field name containing the GLB file data (ArrayBuffer, base64 string, or Buffer object)

#### Analysis Options
- **Include Volume Calculation**: Calculate volume for each element (default: true)
- **Include Face Areas**: Calculate surface areas by orientation (default: true)
- **Include Face Perimeters**: Calculate perimeter of each face (default: true)
- **Include Face Orientations**: Calculate angle from horizontal for each face (default: true)
- **Include Dimensions**: Calculate width, height, depth (default: true)
- **Include Metadata**: Include vertex count, face count, and material info (default: true)
- **Precision**: Number of decimal places for calculations (0-6, default: 3)

#### Output Format Options
- **Detailed**: Individual meshes + summary statistics
- **Summary Only**: Overall statistics only
- **Meshes Only**: Individual mesh data only

### Output Data

The node returns comprehensive analysis data in JSON format:

```json
{
  "meshes": [
    {
      "name": "Wall_001",
      "volume": 2.456,
      "faceAreas": {
        "top": 12.5,
        "bottom": 12.5,
        "left": 8.2,
        "right": 8.2,
        "front": 3.1,
        "back": 3.1
      },
      "facePerimeters": [4.2, 6.8, 4.2, 6.8, 3.5, 3.5],
      "faceOrientations": [0, 180, 90, 90, 90, 90],
      "boundingBox": {
        "min": {"x": 0, "y": 0, "z": 0},
        "max": {"x": 5.0, "y": 2.5, "z": 0.2}
      },
      "dimensions": {
        "width": 5.0,
        "height": 2.5,
        "depth": 0.2
      },
      "metadata": {
        "vertexCount": 48,
        "faceCount": 16,
        "materialName": "Concrete"
      }
    }
  ],
  "summary": {
    "totalMeshes": 1,
    "totalVolume": 2.456,
    "totalSurfaceArea": 47.7,
    "averageFaceOrientation": 67.5,
    "overallDimensions": {
      "width": 50.0,
      "height": 12.0,
      "depth": 30.0
    },
    "overallBoundingBox": {
      "min": {"x": -25, "y": 0, "z": -15},
      "max": {"x": 25, "y": 12, "z": 15}
    }
  },
  "metadata": {
    "analyzedAt": "2025-01-05T12:00:00.000Z",
    "options": { /* analysis options */ },
    "processingTimeMs": 1250
  }
}
```

### Usage Examples

#### Example 1: Complete Building Analysis
1. **IFC to GLB Converter** node to convert IFC file
2. **GLB Analyzer** node with all analysis options enabled
3. **Code** node to process and format results for reporting

#### Example 2: Volume and Area Calculation Only
1. **HTTP Request** node to fetch GLB file
2. **GLB Analyzer** node with only volume and area calculations enabled
3. **Set** node to extract specific metrics

#### Example 3: Building Element Classification
1. **Read Binary File** node for local GLB file
2. **GLB Analyzer** node to get detailed mesh properties
3. **IF** node to classify elements by volume/dimensions
4. **Spreadsheet File** node to export results

### Applications

- **Quantity Takeoff**: Calculate material volumes and surface areas
- **Cost Estimation**: Use surface areas for painting/finishing calculations
- **Energy Analysis**: Use surface areas and orientations for thermal analysis
- **Compliance Checking**: Verify dimensions against building codes
- **Quality Control**: Identify irregularities in geometry
- **Asset Management**: Track building element properties

### Performance Tips

- Use Draco compression for web delivery to reduce file sizes by 50-90%
- Reduce precision (0.01-0.1) for architectural visualization where exact measurements aren't critical
- Disable materials if only geometry is needed to reduce file size
- Process large IFC files in chunks by element types for better performance

## Requirements

- n8n version 0.174.0 or higher
- Node.js version 16 or higher
- Sufficient memory for processing large IFC files
- For IFC to GLB conversion, the `@gltf-transform/core` package is required

## Limitations

- Large IFC files may require significant memory and processing time
- Some proprietary IFC extensions may not be fully supported
- Binary data size is limited by n8n's configuration
- GLB conversion is limited to the capabilities of the underlying `web-ifc` and `@gltf-transform/core` libraries

## Contributing

If you encounter issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

MIT License - see LICENSE file for details.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [web-ifc library](https://github.com/ThatOpen/engine_web-ifc)
- [IFC specification](https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/)
- [GLTF/GLB format specification](https://www.khronos.org/gltf/)

## Version History

- **v0.5.0**: Added GLB Analyzer node for comprehensive geometry analysis of building elements
- **v0.4.0**: Added IFC to GLB Converter node with Three.js and web-ifc integration
- **v0.3.0**: Refactored to modular architecture with separate extractors
- **v0.2.0**: Added property extraction capabilities
- **v0.1.2**: Fixed SVG icon compatibility issues
- **v0.1.0**: Initial release with basic IFC element extraction
