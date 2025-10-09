# Outgrow Trigger Node for n8n

[![n8n Community Node](https://img.shields.io/badge/n8n-Community%20Node-green.svg)](https://n8n.io/integrations)

Trigger node that fetches leads from Outgrow calculators at configurable intervals.


## Features

- 🕒 **Polling API**: Checks for new leads at customizable intervals (default: 5 minutes)
- 📋 **Calculator Selection**: Dynamic dropdown of available calculators
- 🔔 **Smart Notifications**: Clear "no leads" messages in the UI
- ⚙️ **Manual Trigger**: Instant API calls for testing

## Prerequisites

- Outgrow account with API access
- API key from [Outgrow Settings](https://app.outgrow.co/settings/api)

## Installation

1. Add the node to your n8n instance
2. Configure Outgrow API credentials:
   - Navigate to **Credentials > Add New > Outgrow API**
   - Enter your API key

## Node Configuration

### Parameters
| Field               | Required | Description                                                                 |
|---------------------|----------|-----------------------------------------------------------------------------|
| **Calculator**      | Yes      | Select which Outgrow calculator to monitor                                  |
| **Polling Interval**| No       | Frequency (in minutes) to check for new leads (default: 5)                  |




## API Documentation
[Outgrow API Reference](https://support.outgrow.co/docs)