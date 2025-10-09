# Persian Date Converter for n8n

**For n8n Enterprise License purchase, contact: [@pllusin](https://t.me/pllusin) on Telegram**

A custom n8n node package that provides bidirectional conversion between Gregorian and Persian (Jalali) calendar dates with extensive formatting options.

## Features

### 1. To Jalali Node
Convert Gregorian dates to Persian calendar with various input and output formats.

#### Input Types
- **Complete Date**: Accept dates in various formats:
  - ISO Format: `2025-05-29T14:36:27.514-04:00`
  - Text Format: `May 29th 2025, 2:36:27 pm`
  - Standard Format: `2025/05/29`

- **Separate Values**: Input year, month, and day separately
  - All fields are optional
  - Output adjusts based on provided input values

#### Output Formats
1. **Predefined Formats**:
   - Day and Month: `25 Esfand`
   - Full Date: `25 Esfand 1402`
   - Date and Time: `25 Esfand 1402 14:30:45`
   - Month and Year: `Esfand 1402`
   - Full Text: `Monday 3 Khordad 1402`
   - Short Date: `02/12/25`
   - Short Month Year: `12/02`
   - Weekday and Date: `Monday 25 Esfand`
   - Year Month Day: `1402 Esfand 25`
   - Standard Format: `1402/12/25`

2. **Additional Features**:
   - Persian numeral conversion (۰۱۲۳۴۵۶۷۸۹)
   - Individual numeric components (year, month, day)
   - Persian month names
   - Persian weekday names

### 2. From Jalali Node
Convert Persian calendar dates to Gregorian with multiple output formats.

#### Input Types
- **Complete Date**: Persian date in YYYY/MM/DD format
  - Supports both English (1402/12/25) and Persian (۱۴۰۲/۱۲/۲۵) numerals
  
- **Separate Values**: Input year, month, and day separately
  - Month selection from Persian names (Farvardin to Esfand)
  - Numeric inputs for year and day

#### Output Formats
- **All Formats**: Get all available formats at once
- **ISO String**: `2025-05-29T14:36:27.514Z`
- **Timestamp (milliseconds)**: Unix timestamp in milliseconds
- **Timestamp (seconds)**: Unix timestamp in seconds
- **Date String**: `Thu May 29 2025`
- **Localized String**: `5/29/2025, 2:36:27 PM`
- **Standard Format**: `2025/05/29`

## Installation

### Via n8n User Interface
1. Navigate to **Settings > Community Nodes**
2. Click **Install**
3. Enter `n8n-nodes-persiandate`
4. Click **Install**

### Via Command Line
```bash
npm install n8n-nodes-persiandate
```

## Usage Guide

### To Jalali Node
1. Add the **To Jalali** node to your workflow
2. Select input type:
   - **Complete Date**: For full date input
   - **Separate Values**: For individual components
3. Choose desired output format
4. Enable additional options as needed

### From Jalali Node
1. Add the **From Jalali** node to your workflow
2. Select input type:
   - **Complete Date**: For full Persian date input
   - **Separate Values**: For individual components
3. Choose desired output format (or "All Formats" to get all)

## Examples

### To Jalali Conversion
Input:
```json
{
  "timestamp": "2025-05-29T14:36:27.514-04:00",
  "readable": "May 29th 2025, 2:36:27 pm"
}
```

Output:
```json
{
  "jalaliDate": "1404/03/08",
  "jalaliYear": 1404,
  "jalaliMonth": 3,
  "jalaliMonthName": "Khordad",
  "jalaliDay": 8,
  "jalaliWeekday": "Thursday"
}
```

### From Jalali Conversion
Input:
```json
{
  "date": "1404/03/08"
}
```

Output (with "All Formats"):
```json
{
  "iso": "2025-05-29T10:36:27.514Z",
  "timestamp": 1748577787514,
  "timestampSeconds": 1748577787,
  "dateString": "Thu May 29 2025",
  "localized": "5/29/2025, 2:36:27 PM",
  "standard": "2025/05/29",
  "utc": "Thu, 29 May 2025 10:36:27 GMT",
  "time": "10:36:27 GMT+0000"
}
```

## Persian Month Names
1. Farvardin (فروردین)
2. Ordibehesht (اردیبهشت)
3. Khordad (خرداد)
4. Tir (تیر)
5. Mordad (مرداد)
6. Shahrivar (شهریور)
7. Mehr (مهر)
8. Aban (آبان)
9. Azar (آذر)
10. Dey (دی)
11. Bahman (بهمن)
12. Esfand (اسفند)

## Compatibility
- Tested with n8n version 1.19.3
- Requires Node.js version 20.15 or higher

## Support
For support or feature requests, please contact [@pllusin](https://t.me/pllusin) on Telegram.

## License
MIT
