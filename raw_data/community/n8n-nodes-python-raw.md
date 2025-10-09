# n8n-nodes-python-raw

> **🚨 CRITICAL DANGER: 100% AI-GENERATED EXPERIMENTAL CODE 🚨**: ALL modifications and features in this fork were created using AI assistance. This code may contain CRITICAL ERRORS, security vulnerabilities, or unexpected behavior. ABSOLUTELY NOT FOR PRODUCTION USE. HIGH RISK - USE AT YOUR OWN EXTREME CAUTION.

> **⚠️ DISCLAIMER**: This is an unofficial fork of n8n-nodes-python, not affiliated with or endorsed by n8n GmbH. The name "n8n" is used solely to indicate compatibility with the n8n platform. This project is not for commercial use - see Commons Clause license restrictions.

> **🤖 AI-Generated Code Notice**: Large portions of this codebase were developed with AI assistance. Code may contain errors or unexpected behavior. Use at your own risk.

> **📝 Personal Project**: This fork was created for personal, non-commercial use and educational purposes. The maintainer assumes no responsibility for any use by third parties.

> **📋 READ FULL AI DISCLAIMER**: For comprehensive details about AI-generated code risks, see [AI_DISCLAIMER.md](AI_DISCLAIMER.md)

A community fork of [naskio/n8n-nodes-python](https://github.com/naskio/n8n-nodes-python) for executing Python scripts with raw output control, advanced file processing capabilities, and comprehensive testing infrastructure.

**Original Project**: https://github.com/naskio/n8n-nodes-python by [naskio](https://github.com/naskio) - Thank you for the foundation!

This fork includes significant enhancements for raw Python script execution, structured output parsing, comprehensive file processing, and robust error handling.

## ✨ Key Features

- **Raw Python Script Execution**: Execute pure Python scripts without modifications
- **Auto-Variable Extraction**: Fields from input data automatically available as individual Python variables
- **Output File Processing**: Generate files in Python scripts and automatically include them in n8n output (v1.11.0+)
- **Smart File Detection**: Automatic file detection with dual modes - Ready Variable Path and Auto Search (v1.12.2+)
- **Advanced File Debugging**: Comprehensive file processing debugging system (v1.12.0+)
- **Script Export Options**: Export scripts as .py or .txt files for security compliance (v1.12.1+)
- **Multiple Credentials Support**: Select and use multiple Python Environment Variables credentials simultaneously (v1.9.0+)
- **Flexible Output Parsing**: Parse stdout as JSON, CSV, lines, or smart auto-detection
- **Multiple Execution Modes**: Run once for all items or once per each item
- **Pass Through Data**: Preserve and combine input data with Python results
- **Variable Injection**: Optional injection of input items and environment variables with enhanced sanitization (v1.12.8+)
- **Comprehensive Error Handling**: Detailed error reporting with Python traceback analysis
- **Debug/Test System**: 5 debug modes including safe testing and script export
- **Multiple Output Formats**: Support for single/multiple JSON objects, CSV data, and text lines
- **Smart Parsing**: Automatic detection and parsing of JSON, CSV, and structured data
- **Production Stability**: 100% test coverage for unit, functional, and TypeScript tests (v1.13.1+)
- **Global Accessibility**: Complete English documentation and internationalization (v1.13.2+)

**⚠️ Not for Commercial Use**: This software is licensed under Apache 2.0 with Commons Clause - commercial use is prohibited.

## 📦 Installation

In n8n, go to **Settings** → **Community Nodes** and install:

```
n8n-nodes-python-raw
```

## 🚀 Quick Start Example

**Input data from previous node:**
```json
[{"title": "My Video", "duration": 120, "author": "John"}]
```

**Your Python code:**
```python
# Variables automatically extracted from input:
print(f"Processing: {title}")        # "My Video"
print(f"Duration: {duration} sec")   # 120 sec  
print(f"Author: {author}")           # "John"

# Generate a report file:
import os
report_content = f"Video: {title}\nDuration: {duration}s\nAuthor: {author}"
with open(os.path.join(output_dir, expected_filename), 'w') as f:
    f.write(report_content)

print("Report generated successfully!")
```

**Result:** Direct access to your data AND automatic file processing!

## 📁 Output File Processing (v1.11.0+)

### Overview
Generate files in your Python scripts and automatically include them in n8n workflow output. Perfect for reports, images, data exports, and more.

### Configuration
- **Enable Output File Processing**: Toggle to activate file generation detection (default: disabled)
- **Expected Output Filename**: Filename you expect the script to create (e.g., "report.pdf", "data.csv")
- **File Detection Mode**: How to provide the output file path to your script:
  - **Ready Variable Path**: Provides `output_file_path` variable with complete file path (recommended)
  - **Auto Search by Name**: Automatically finds files by filename after script execution
- **Max Output File Size**: Configurable size limit from 1-1000 MB (default: 100 MB)
- **Auto-cleanup Output Directory**: Automatic cleanup of temporary files (default: enabled)
- **Include File Metadata**: Option to include file metadata in output JSON (default: enabled)

### Python Script Integration

#### Ready Variable Path Mode (Recommended)
```python
import os
import json

# Method 1: Use the ready-made path (recommended)
with open(output_file_path, 'w') as f:
    json.dump({"results": "processed_data"}, f)

# Method 2: Build path manually using provided variables  
file_path = os.path.join(output_dir, expected_filename)
with open(file_path, 'w') as f:
    f.write("Report content")
```

#### Auto Search Mode
```python
# Create file with the exact filename specified
# n8n will automatically find it after script execution
with open(expected_filename, 'w') as f:
    f.write("Generated content")

# Or in a subdirectory - n8n will find it recursively
os.makedirs("reports", exist_ok=True) 
with open(os.path.join("reports", expected_filename), 'w') as f:
    f.write("Report in subfolder")
```

### Supported File Types
- **Documents**: PDF, Word, Excel, PowerPoint, HTML
- **Images**: JPG, PNG, GIF, BMP, SVG, WebP
- **Data**: CSV, JSON, XML, YAML, TXT
- **Archives**: ZIP, TAR, GZ
- **Media**: MP4, MP3, AVI, MOV
- **Any file type** with automatic MIME type detection

### Example Use Cases

#### Generate PDF Report
```python
import os
from reportlab.pdfgen import canvas

# Create PDF report
pdf_path = output_file_path  # or os.path.join(output_dir, expected_filename)
c = canvas.Canvas(pdf_path)
c.drawString(100, 750, f"Report for {title}")
c.drawString(100, 730, f"Duration: {duration} seconds")
c.save()

print("PDF report generated!")
```

#### Export Data to CSV
```python
import csv
import os

# Process data and export to CSV
csv_path = output_file_path
with open(csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Duration', 'Author'])
    for item in input_items:
        writer.writerow([item.get('title'), item.get('duration'), item.get('author')])

print(f"Exported {len(input_items)} items to CSV")
```

#### Generate Video with FFmpeg
```python
import subprocess
import os
from shutil import which

# Ensure ffmpeg is available
if which("ffmpeg") is None:
    print("Error: ffmpeg not found")
    exit(1)

# Generate test video
cmd = [
    "ffmpeg", "-y",
    "-f", "lavfi", "-i", "testsrc=size=1280x720:rate=30:duration=5",
    "-f", "lavfi", "-i", "sine=frequency=1000:sample_rate=44100:duration=5", 
    "-c:v", "libx264", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "128k",
    output_file_path
]

subprocess.run(cmd, check=True)
print("Test video generated successfully!")
```

## 🔍 File Debug System (v1.12.0+)

### Overview
Comprehensive debugging system for troubleshooting file processing issues with detailed diagnostics.

### Configuration
- **Enable File Debugging**: Toggle to include detailed file processing information
- **Debug Input Files**: Information about input files processing
- **Debug Output Files**: Output files and directory scanning information  
- **Include System Information**: System permissions and environment analysis
- **Include Directory Listings**: File listings from working and output directories

### Debug Information Structure
```json
{
  "fileDebugInfo": {
    "input_files": {
      "count": 2,
      "total_size_mb": 5.47,
      "files_by_type": {"image/jpeg": 1, "application/pdf": 1},
      "files_details": [...],
      "processing_errors": []
    },
    "output_files": {
      "processing_enabled": true,
      "output_directory": "/tmp/n8n_output_xyz",
      "directory_exists": true,
      "directory_writable": true,
      "found_files": [...],
      "scan_errors": []
    },
    "system_info": {
      "python_executable": "/usr/bin/python3",
      "working_directory": "/app",
      "user_permissions": {"can_write_temp": true},
      "environment_variables": {"output_dir_available": true}
    },
    "directory_listings": {
      "working_directory": [...],
      "output_directory": [...]
    }
  }
}
```

### Troubleshooting Use Cases
- **Problem**: `output_dir` variable not available → **Solution**: Check system_info.environment_variables
- **Problem**: Files not detected → **Solution**: Check output_files.found_files and scan_errors
- **Problem**: Permission issues → **Solution**: Check system_info.user_permissions
- **Problem**: Input file processing → **Solution**: Check input_files.processing_errors

## 🎨 Script Export Format (v1.12.1+)

### Overview
Choose export format for generated scripts in "Export Script" debug mode to comply with security policies.

### Configuration
- **Script Export Format**: Available when Debug Mode = "Export Script"
  - **Python File (.py)**: Standard Python script format (default)
  - **Text File (.txt)**: Plain text format for restricted environments

### Use Cases
- **Corporate Environments**: Export as .txt when .py files are blocked
- **Email Sharing**: .txt files pass through email filters more easily
- **Documentation**: Include Python scripts in documentation as text files
- **Security Compliance**: Bypass antivirus restrictions on .py files

## 🚀 Configuration Options

### Basic Settings
- **Python Code**: Multi-line Python script to execute
- **Python Executable**: Path to Python executable (default: "python3")
- **Inject Variables**: Enable/disable automatic variable injection (default: true)

### Output File Processing (v1.11.0+)
- **Enable Output File Processing**: Toggle file generation detection (default: disabled)
- **Expected Output Filename**: Filename the script will create (e.g., "report.pdf")
- **File Detection Mode**: Choose detection method:
  - **Ready Variable Path**: Use provided `output_file_path` variable (recommended)
  - **Auto Search by Name**: Automatic recursive file search by filename
- **Max Output File Size**: Size limit 1-1000 MB (default: 100 MB)
- **Auto-cleanup Output Directory**: Clean temporary files (default: enabled)
- **Include File Metadata**: Add file info to output (default: enabled)
- **Auto Intercept Files**: Automatic file processing (default: enabled)

### File Debug Options (v1.12.0+)
- **Enable File Debugging**: Include detailed file processing diagnostics
- **Debug Input Files**: Input file processing information
- **Debug Output Files**: Output directory and file scanning details
- **Include System Information**: System permissions and environment data
- **Include Directory Listings**: Directory content listings

### Credentials Management (v1.9.0+)
- **Python Environment Variables**: Multi-select credentials
- **Include All Available Credentials**: Auto-include all Python Environment Variables
- **Credential Merge Strategy**: Handle variable conflicts:
  - **last_wins** (default): Later credentials override earlier ones
  - **first_wins**: Earlier credentials take precedence  
  - **prefix**: Add credential name prefix to variables

### Error Handling (v1.5.0+)
- **Return Error Details** (default): Continue execution, return error info
- **Throw Error on Non-Zero Exit**: Stop workflow on script failure
- **Ignore Exit Code**: Continue regardless of exit code

### Debug/Test Mode (v1.6.0+)
- **Off** (default): Normal execution without debug overhead
- **Basic Debug**: Add script content and basic execution info
- **Full Debug**: Complete debugging with timing and environment info
- **Test Only**: Safe validation without execution
- **Export Script**: Full debug plus downloadable script files and execution results (v1.14.5+)

### Script Generation Options (v1.7.0+)
- **Hide Variable Values** (default: disabled): Replace sensitive values with asterisks

### Export Script Mode (v1.14.5+)
When Debug Mode is set to "Export Script", the node generates two downloadable files:

#### 📄 Python Script File
- **Format**: `.py` or `.txt` (configurable via Script Export Format)
- **Content**: Complete executable Python script with all injected variables
- **Filename**: `python_script_TIMESTAMP.py` (or `python_script_error_TIMESTAMP.py` for errors)
- **Use Case**: Share scripts, debug issues, run scripts outside n8n

#### 📄 Output Results File (NEW)
- **Format**: `output_TIMESTAMP.json`
- **Content**: Complete execution results in structured JSON format
- **Structure**:
  ```json
  {
    "timestamp": "2025-06-05T12:00:00.000Z",
    "execution_results": {
      "exitCode": 0,
      "success": true,
      "stdout": "script output",
      "stderr": "",
      "parsed_stdout": {...},
      "parsing_success": true,
      "executedAt": "2025-06-05T12:00:00.000Z",
      "inputItemsCount": 1,
      "executionMode": "once"
    },
    "export_info": {
      "description": "Результаты выполнения Python скрипта из n8n",
      "format_version": "1.0",
      "exported_at": "2025-06-05T12:00:00.000Z",
      "node_type": "n8n-nodes-python.pythonFunction"
    }
  }
  ```

#### Benefits of Export Mode
- **Complete Debugging Package**: Both script and results in one export
- **Offline Analysis**: Analyze execution results without n8n interface
- **Documentation**: Perfect for bug reports and support requests
- **Audit Trail**: Structured record of script execution with metadata
- **Error Investigation**: Detailed error information preserved in JSON format
- **Sharing**: Easy to share both script and results with team members

### Execution Control (v1.4.0+)
- **Execution Mode**: Choose script execution approach:
  - **Once for All Items**: Execute once with all input items (faster, default)
  - **Once per Item**: Execute separately for each input item (more flexible)

### Data Management (v1.4.0+)
- **Pass Through Input Data**: Include original input data in output (default: false)
- **Pass Through Mode**: How to combine input with results:
  - **Merge with Result**: Add input fields directly to result object
  - **Separate Field**: Add input data as "inputData" field
  - **Multiple Outputs**: Return separate items for input and result

### Output Parsing (v1.3.0+)
- **Parse Output**: Choose stdout parsing method:
  - **None (Raw String)**: Return stdout as plain text
  - **JSON**: Parse as JSON object(s)
  - **Lines**: Split into array of lines
  - **Smart Auto-detect**: Automatically detect and parse JSON/CSV/text

## 📊 Output Structure

The node returns a comprehensive result object:

```json
{
  "exitCode": 0,
  "stdout": "raw output string",
  "stderr": "error messages", 
  "success": true,
  "error": null,
  "inputItemsCount": 1,
  "executedAt": "2025-06-02T12:00:00.000Z",
  "injectVariables": true,
  "parseOutput": "none",
  "executionMode": "once",
  
  // Output File Processing results (when enabled)
  "outputFiles": [
    {
      "filename": "report.pdf",
      "size": 1024000,
      "mimetype": "application/pdf",
      "extension": "pdf",
      "binaryKey": "report.pdf",
      "createdAt": "2025-06-02T12:00:00.000Z"
    }
  ],
  "outputFilesCount": 1,
  
  // Parsing results (when enabled)
  "parsed_stdout": {"key": "value"}, 
  "parsing_success": true,
  "parsing_error": null,
  "output_format": "json",
  "parsing_method": "json",
  
  // File Debug Information (when enabled)
  "fileDebugInfo": {
    "input_files": {...},
    "output_files": {...},
    "system_info": {...},
    "directory_listings": {...}
  },
  
  // Error details (on failure)
  "pythonError": {
    "errorType": "ImportError",
    "errorMessage": "No module named 'requests'",
    "missingModules": ["requests"],
    "traceback": "full traceback",
    "lineNumber": 5
  },
  "detailedError": "comprehensive error description"
}
```

## 💡 Usage Examples

### File Generation with Debug
```python
import os
import json

# Create a data analysis report
report_data = {
    "total_items": len(input_items),
    "analysis": "completed",
    "timestamp": "2025-06-02T12:00:00Z"
}

# Save as JSON file using the ready-made path
with open(output_file_path, 'w') as f:
    json.dump(report_data, f, indent=2)

print(f"Report saved to {expected_filename}")
```

**Configuration**: 
- Output File Processing = enabled
- Expected Output Filename = "analysis_report.json"
- File Detection Mode = "Ready Variable Path"
- File Debug Options = enabled

**Result**: JSON file automatically included as binary data in n8n output

### Multiple File Generation
```python
import os
import json
import csv

# Create multiple output files
os.makedirs(output_dir, exist_ok=True)

# 1. Generate summary JSON
summary = {"processed": len(input_items), "status": "complete"}
with open(os.path.join(output_dir, "summary.json"), 'w') as f:
    json.dump(summary, f)

# 2. Generate detailed CSV  
with open(os.path.join(output_dir, expected_filename), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Duration'])
    for item in input_items:
        writer.writerow([item.get('title'), item.get('duration')])

print("Multiple files generated")
```

**Configuration**:
- Expected Output Filename = "details.csv" 
- File Detection Mode = "Auto Search by Name"

**Result**: Both summary.json and details.csv files are automatically detected and included

### Image Processing and Generation  
```python
import os
from PIL import Image, ImageDraw

# Create a simple chart image
img = Image.new('RGB', (800, 600), color='white')
draw = ImageDraw.Draw(img)

# Draw title
draw.text((50, 50), f"Analysis Results", fill='black')
draw.text((50, 100), f"Total Items: {len(input_items)}", fill='blue')

# Save image
img.save(output_file_path)
print(f"Chart saved as {expected_filename}")
```

**Configuration**:
- Expected Output Filename = "chart.png"
- File Detection Mode = "Ready Variable Path"

**Result**: PNG image automatically included as binary data

### Multiple Credentials with File Processing
```python
# Using multiple API credentials to fetch data and generate report
import requests
import json
import os

# Access different service credentials  
api1_data = requests.get(f"https://api1.com/data", 
                        headers={"Authorization": f"Bearer {API1_TOKEN}"}).json()

api2_data = requests.get(f"https://api2.com/stats",
                        headers={"X-API-Key": API2_KEY}).json()

# Combine data and generate report
combined_report = {
    "api1_results": api1_data,
    "api2_results": api2_data, 
    "generated_at": "2025-06-02T12:00:00Z",
    "total_items": len(input_items)
}

# Save comprehensive report
with open(output_file_path, 'w') as f:
    json.dump(combined_report, f, indent=2)

print("Multi-API report generated")
```

**Configuration**:
- Credentials Management = ["API Service 1", "API Service 2"]
- Expected Output Filename = "multi_api_report.json"
- Output File Processing = enabled

**Result**: Report with data from multiple APIs saved as downloadable file

## 🔧 Working with Input Variables

### Variable Injection Overview

When "Inject Variables" is enabled (default), the node automatically injects powerful variables into your Python script:

- **Individual field variables**: Fields from first input item (e.g., `title`, `duration`, `author`)
- **`output_dir`**: Unique temporary directory for file generation (when Output File Processing enabled)
- **`expected_filename`**: Filename specified in configuration (when Output File Processing enabled)
- **`output_file_path`**: Complete file path for output file (when using Ready Variable Path mode)
- **`env_vars`**: Dictionary of environment variables (from credentials or system, optional)

### 📋 Understanding Input Data Structure

```python
# Input from previous n8n node:
[
  {"title": "Video 1", "duration": 120, "author": "John"},
  {"title": "Video 2", "duration": 90, "author": "Jane"}
]

# Automatically available variables (from first item):
title = "Video 1"           # Direct access
duration = 120             # No indexing needed
author = "John"            # Clean variable names

# File processing variables (when enabled):
output_dir = "/tmp/n8n_python_output_12345"
expected_filename = "report.pdf"
output_file_path = "/tmp/n8n_python_output_12345/report.pdf"

# Legacy compatibility (optional):
env_vars = {...}           # Environment variables dictionary
```

**Benefits:**
- **Direct access**: Use `title` instead of `input_items[0]['title']`
- **Cleaner code**: More readable Python scripts
- **File processing**: Ready-to-use paths for file generation
- **Safe naming**: Invalid Python identifiers converted (e.g., `video-name` → `video_name`)

### 🔄 Execution Mode Behavior

#### **Once for All Items** (Default - Faster)
- Auto-extracted variables from **first item only**
- Script runs **once** with access to all items
- Ideal for: aggregations, batch processing, file generation

```python
import json
import os

print(f"Processing {len(input_items)} items total")
print(f"First item: {title}")  # From first item

# Generate summary report
summary = {
    "total_items": len(input_items),
    "first_title": title,
    "all_titles": [item.get('title') for item in input_items]
}

# Save to file
with open(output_file_path, 'w') as f:
    json.dump(summary, f, indent=2)
```

#### **Once per Item** (More Flexible)
- Auto-extracted variables from **current item**
- Script runs **separately** for each input item
- Ideal for: individual file generation, API calls per item

```python
import json
import os

# Variables extracted from current item
print(f"Processing: {title}")    # Current item's title
print(f"Duration: {duration}")   # Current item's duration

# Generate individual report file
report = {
    "item_title": title,
    "item_duration": duration,
    "processed_at": "2025-06-02T12:00:00Z"
}

# Each item gets its own output file
with open(output_file_path, 'w') as f:
    json.dump(report, f, indent=2)
```

## 🛠️ Troubleshooting Guide

### File Processing Issues

#### Problem: `output_dir` variable not available
**Solution**: 
1. Enable "Output File Processing"
2. Check File Debug Info → system_info.environment_variables
3. Verify "Inject Variables" is enabled

#### Problem: Files not detected after generation
**Solution**:
1. Check expected filename matches exactly
2. Use File Debug Options to see found_files
3. Verify file was created in correct location
4. Check file size doesn't exceed configured limit

#### Problem: Permission errors
**Solution**:
1. Enable File Debug Options → system_info.user_permissions
2. Check directory_writable status
3. Verify output directory access rights

#### Problem: Script execution fails
**Solution**:
1. Use "Test Only" mode to validate syntax
2. Check Debug Info → environment_check for Python availability
3. Verify all required imports are included
4. Check pythonError details for specific issues

### Common Import Issues
**Problem**: `NameError: name 'os' is not defined`
**Solution**: Add required imports to your script:
```python
import os
import subprocess
import json
from shutil import which
# ... your code
```

## 📄 Version History

- **v1.13.2**: Complete internationalization - all Russian text translated to English for global accessibility
- **v1.13.1**: Test infrastructure reorganization and comprehensive test fixes (unit/functional/TypeScript tests at 100%)
- **v1.12.8**: Variable validation fixes - enhanced sanitization of Python variable names from input data
- **v1.12.7**: Improved backward compatibility and credential handling in recent n8n versions
- **v1.12.6**: Enhanced variable injection and output file processing stability
- **v1.12.5**: Removed legacy variables and fixed file variables hiding issue
- **v1.12.4**: Added `expected_filename` variable and enhanced output file processing instructions
- **v1.12.3**: Fixed Expected Output Filename field UI issue and added default example
- **v1.12.2**: Smart Output File Detection System with dual modes and enhanced file search
- **v1.12.1**: Script Export Format selection (.py/.txt) for security compliance
- **v1.12.0**: Advanced File Debugging System for troubleshooting file processing
- **v1.11.0**: Output File Processing - generate files in Python and auto-include in n8n output
- **v1.9.0**: Multiple credentials support with merge strategies and backward compatibility
- **v1.8.0**: Enhanced script generation and credential source tracking
- **v1.7.0**: Script Generation Options with legacy support toggle and value hiding
- **v1.6.1**: Auto-Variable Extraction feature for direct field access
- **v1.6.0**: Comprehensive Debug/Test system with script export and syntax validation
- **v1.5.0**: Enhanced error handling and comprehensive variable documentation
- **v1.4.0**: Execution modes and data pass-through capabilities
- **v1.3.0**: Comprehensive output parsing (JSON/CSV/Lines/Smart modes)
- **v1.2.0**: Enhanced error handling and user experience
- **v1.1.0**: Variable injection control and improved error parsing
- **v1.0.0**: Initial fork with raw execution functionality

## 🔗 Links

- [npm Package](https://www.npmjs.com/package/n8n-nodes-python-raw)
- [GitHub Repository](https://github.com/stttru/n8n-nodes-python-fork)
- [Original Package](https://github.com/naskio/n8n-nodes-python)
- [n8n Community Nodes](https://docs.n8n.io/integrations/community-nodes/)

## 📄 License

Apache License 2.0 with Commons Clause - see [LICENSE.md](LICENSE.md)

**⚠️ IMPORTANT DISCLAIMERS:**

### 🚨 ABSOLUTE LIABILITY DISCLAIMER 🚨
**THE MAINTAINER ACCEPTS NO RESPONSIBILITY WHATSOEVER FOR:**
- **ANY DAMAGES, DATA LOSS, SYSTEM FAILURES, OR SECURITY BREACHES** caused by this software
- **CRITICAL ERRORS IN AI-GENERATED CODE** (100% of modifications) that may cause system failures
- **PRODUCTION USE FAILURES** - this software is NOT tested for production environments
- **SECURITY VULNERABILITIES** - AI-generated code may contain exploitable security flaws
- **DATA CORRUPTION OR LOSS** from script execution or file processing
- **THIRD-PARTY USE** of this software for any purpose whatsoever
- **COMPLIANCE FAILURES** - no guarantees of regulatory or policy compliance

### ⛔ CRITICAL AI-GENERATED CODE WARNINGS ⛔
Large portions of this codebase were developed with AI assistance. **CRITICAL RISKS:**
- **UNTESTED CODE PATTERNS** - AI may generate code that appears correct but fails unexpectedly
- **SECURITY VULNERABILITIES** - AI cannot guarantee secure coding practices
- **LOGIC ERRORS** - Complex interactions may not be properly validated
- **PERFORMANCE ISSUES** - AI-generated code may not be optimized for production use
- **UNDOCUMENTED BEHAVIORS** - AI code may have side effects not captured in documentation

**MANDATORY REQUIREMENTS BEFORE USE:**
- **THOROUGH TESTING** in isolated environments before any real use
- **SECURITY AUDIT** of all AI-generated code portions
- **VALIDATION** of all functionality critical to your use case
- **BACKUP SYSTEMS** - never rely on this software as single point of failure

### 🚫 Commercial Use Restriction
This software is licensed under Apache License 2.0 with Commons Clause, which **prohibits commercial use**. You may not sell, distribute for a fee, or use this software in any commercial product or service.

### ⚠️ No Warranty & Liability Disclaimer
This software is provided "AS IS" without warranty of any kind. The maintainer assumes **NO RESPONSIBILITY** for:
- Any damages or issues caused by using this software
- Use by third parties for any purpose
- Errors, bugs, or unexpected behavior in the code
- Data loss, system damage, or security vulnerabilities

**Use at your own risk and thoroughly test before any production use.**

### Personal Use Disclaimer
This fork was created for **personal, non-commercial use and educational purposes only**. It is not intended for:
- Production environments without thorough testing
- Commercial applications or services
- Mission-critical systems
- Environments where reliability is essential

### Attribution
- **Original Project**: [n8n-nodes-python](https://github.com/naskio/n8n-nodes-python) by [naskio](https://github.com/naskio)
- **Fork Maintainer**: Sergei Trufanov (stttru@gmail.com)
- **Disclaimer**: This is an unofficial fork, not affiliated with n8n GmbH

## 🤝 Contributing

This is a community-maintained fork. Contributions welcome! 