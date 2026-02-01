# Ragic n8n Node

This repository contains a **custom n8n node** for integrating with **Ragic**.  
It allows you to automate and interact with your Ragic database directly from n8n workflows.

## Features

The node currently supports the following functionalities:

- **Webhook**: Listen for real-time events from Ragic.
- **Read**: Retrieve records from your Ragic database.
- **Update**: Update existing records in your Ragic database.
- **Create**: Create new records with custom logic in your Ragic database.
- **Retrieve File**: Fetch files from your Ragic database.

## Version History

- **v2.4.0**
  - Added support for **credential verification**

- **v2.3.1**
  - Bug fix: Corrected behavior when creating/updating records so that **formula**, **default value**, **link & load**, **workflow**, and **notification** are properly executed.

- **v2.3.0**
  - Added support for **Upload File**
  - Added **Update Subtable Fields**
  - Support for setting **multiple values in multi-select fields** within Field Method
  - Updated display name of **Ragic Trigger** in the nodes panel
  - Other bug fixes

- **v2.2.1**
  - Added support for **Retrieve File**

- **v2.1.0**
  - Added support for **Read Data**

- **v2.0.0**
  - Added support for **field-based configuration**

- **v1.0.0**
  - Initial release: **Webhook**, **Update**, **Create**