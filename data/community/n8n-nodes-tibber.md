# n8n-nodes-tibber

This is an n8n node to access the Tibber API. It allows you to fetch data from your Tibber account, including home information, consumption data, and price information.

[Tibber](https://tibber.com/) is a digital electricity supplier that provides real-time energy consumption data and smart home integration.

## Installation

### In n8n Desktop or Cloud
1. Go to **Settings > Community Nodes**
2. Click on **Install**
3. Enter `n8n-nodes-tibber` in the **Name** field
4. Click **Install**

### In your own n8n instance
1. Install the package:
```bash
npm install n8n-nodes-tibber
```
2. Restart n8n

## Usage

### Authentication
To use this node, you need a Tibber API token:

1. Create a developer account at [developer.tibber.com](https://developer.tibber.com/)
2. Generate an access token
3. Use this token in the Tibber API credentials in n8n

### Available Operations

#### Home
- **Get**: Retrieves information about all homes in your Tibber account
- **Get Consumption**: Fetches consumption data for a specific home with various resolution options (hourly, daily, weekly, monthly, annual)
- **Get Price**: Retrieves current, today's, and tomorrow's price information for a specific home

## Example Workflows

### Monitor Energy Prices
Create a workflow that checks energy prices daily and sends you a notification when prices are low.

### Track Energy Consumption
Set up a workflow to record your energy consumption data to a database for long-term analysis.

## Resources
- [Tibber API Documentation](https://developer.tibber.com/)
- [n8n Documentation](https://docs.n8n.io/)

## Version History

### 1.1.17 (2025-08-11)
- Fixed package loading issue by removing conflicting n8n configuration
- Resolved dual configuration conflict between main entry point and explicit n8n paths
- Package now uses consistent main entry point approach for reliable loading in n8n
- Eliminated "The specified package could not be loaded" error caused by configuration conflicts

### 1.1.16 (2025-08-11)
- Fixed gulp-sourcemaps module not found error during build process
- Resolved dependency resolution issues that prevented build from completing
- Build process now works correctly with both npm and pnpm package managers

### 1.1.15 (2025-08-11)
- Added source map generation (.map files) to the build process
- Installed gulp-sourcemaps dependency for proper source map handling
- Modified gulpfile.js TypeScript compilation to generate source maps alongside compiled JavaScript files
- Source maps now available in dist directory for better debugging support

### 1.1.14 (2025-08-11)
- Version increment for package maintenance

### 1.1.13 (2025-08-11)
- Restructured project by moving credentials and nodes directories from src/ to root level
- Removed src/ directory entirely as requested to simplify project structure
- Updated all file references and imports to reflect new directory layout
- Modified main.ts, index.js, gulpfile.js, and tsconfig.json to use new paths
- Added package.json copying to dist directory during build process
- Updated TypeScript configuration for incremental builds

### 1.1.12 (2025-08-11)
- Fixed package loading issue by resolving configuration conflicts between main entry point and n8n section
- Added index.js to files array in package.json to ensure main entry point is included in package
- Removed conflicting nodes and credentials paths from n8n configuration to rely on main entry point
- Resolved "The specified package could not be loaded" error by using consistent package structure

### 1.1.11 (2025-08-11)
- Fixed build system by adding TypeScript compilation to gulp build process
- Resolved compilation errors related to NodeConnectionType usage in Tibber.node.ts
- Updated gulpfile.js to include build:tsc task for proper TypeScript compilation
- Ensured all compiled JavaScript files are properly generated in dist directory

### 1.1.10 (2025-08-11)
- Updated n8n package configuration to point to individual compiled node and credential files
- Fixed package structure to follow n8n documentation requirements for file organization
- Corrected paths in package.json to reference dist/src/nodes/Tibber/Tibber.node.js and dist/src/credentials/TibberApi.credentials.js

### 1.1.9 (2025-08-11)
- Simplified n8n package configuration to resolve "The specified package could not be loaded" error
- Removed explicit nodes and credentials paths from n8n section, relying on main entry point approach
- Fixed potential configuration conflicts that could prevent n8n from loading the community package

### 1.1.8 (2025-08-11)
- Version increment to resolve npm publish conflict with previously published version 1.1.7
- No functional changes, package ready for republishing to npm registry

### 1.1.7 (2025-08-11)
- Fixed n8n package configuration by adding explicit nodes and credentials paths
- Resolved "The specified package does not contain any nodes" error by properly configuring the n8n section in package.json
- N8n can now correctly discover and load the Tibber nodes and credentials from the package

### 1.1.6 (2025-08-06)
- Fixed node export format to export class constructors instead of instantiated objects
- Resolved "The specified package does not contain any nodes" error by using proper n8n export format
- N8n now correctly recognizes and loads the Tibber nodes from the package

### 1.1.5 (2025-08-06)
- Fixed gulp commands in package.json scripts to use npx for proper local package execution
- Resolved "gulp: not found" error when using pnpm by ensuring gulp is called via npx
- Improved compatibility with different package managers (npm, yarn, pnpm)

### 1.1.4 (2025-08-06)
- Added missing gulpfile.js for build automation with gulp tasks
- Created index.js as main entry point that exports from compiled main.js
- Updated package.json main field to use index.js instead of dist/main.js
- Added gulp-based build system with TypeScript compilation and asset copying
- Installed gulp, gulp-typescript, and gulp-clean as development dependencies

### 1.1.3 (2025-08-06)
- Fixed node export structure to export instantiated objects instead of class constructors
- Resolved "The specified package does not contain any nodes" error by properly instantiating TibberNode and TibberApi classes
- N8n can now properly detect and load the Tibber nodes from the package

### 1.1.2 (2025-08-05)
- Added Node.js engine requirements (>=20.0.0) to package.json
- Resolved npm engine warnings by specifying minimum Node.js version
- Added npm version requirement (>=8.0.0) for better compatibility

### 1.1.1 (2025-08-05)
- Removed conflicting n8n configuration section from package.json
- Fixed package loading issues by using single main.js entry point approach
- Resolved dual configuration that was preventing n8n from properly loading the community node

### 1.1.0 (2025-08-05)
- Updated main.ts to use ES6 import/export syntax instead of CommonJS module.exports
- Changed from exporting node/credential metadata to directly exporting class instances
- Improved compatibility with modern n8n community node standards

### 1.0.9 (2025-08-05)
- Renamed index.ts to main.ts to follow n8n community node naming convention
- Updated package.json main and types fields to point to dist/main.js and dist/main.d.ts
- Updated TypeScript configuration to include main.ts instead of index.ts

### 1.0.8 (2025-08-05)
- Fixed sourcePath references in index.ts to correctly point to compiled JavaScript files
- Resolved package loading issues by ensuring consistent file path references

### 1.0.7 (2025-08-05)
- Fixed n8n configuration paths in package.json to match actual compiled file structure
- Corrected credentials and nodes paths to use dist/src/ prefix for proper package loading

### 1.0.6 (2025-08-05)
- Fixed file paths in index.ts to match actual compiled structure in dist/src/
- Corrected sourcePath references to resolve package loading issues

### 1.0.5 (2025-08-05)
- Fixed module exports to use CommonJS format required by n8n community nodes
- Updated index.ts to export nodes and credentials arrays with proper structure

### 1.0.4 (2025-08-05)
- Moved index.ts from src/ to root directory for proper n8n community node structure
- Updated TypeScript configuration to handle mixed source locations

### 1.0.3 (2025-08-05)
- Corrected package name to "n8n-nodes-tibber" (with 's') for proper n8n compatibility
- Updated all references and installation instructions to use correct package name

### 1.0.2 (2025-08-05)
- Fixed package name to match directory name for proper loading in n8n
- Updated all references to use consistent package name

### 1.0.1 (2025-08-05)
- Added n8n-community-node-package keyword for better discoverability
- Fixed build script to use npx for better package manager compatibility

### 1.0.0 (2025-08-05)
- Initial release
- Support for retrieving home information
- Support for fetching consumption data with various resolution options
- Support for retrieving price information

## License
MIT