![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)
# n8n-nodes-or

[![version](https://img.shields.io/npm/v/n8n-nodes-or.svg)](https://www.npmjs.org/package/n8n-nodes-or)
[![downloads](https://img.shields.io/npm/dt/n8n-nodes-or.svg)](https://www.npmjs.org/package/n8n-nodes-or)

OutputRocks this is a service for generating documents
Features:

- Authorization
	- Credential for OutputRocks API
- Format
	- PDF
	- TXT
	- HTML
- Webhook identifier
	- n8n
- Template Identifier
	- sample
- Metadata
	-	{
		 "filename": "test.pdf",
		 "eventId": "12345",
		 "documentName": "document.pdf"
       }
- Data
	- {
     "qrlink": "https://example.com/customer/1",
			"customer": {
			"salutation": 1,
			"firstname": "John",
			"surname": "Doe",
			"balance": 6000
			}

## Install

n8n-nodes-or

[`Documentation`](https://docs.n8n.io/integrations/community-nodes/installation/)
