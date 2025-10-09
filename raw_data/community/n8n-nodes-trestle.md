# n8n-nodes-trestle

This is an n8n community node. It lets you use Trestle in your n8n workflows.

Trestle provides advanced phone validation and contact verification APIs with real-time activity scoring, fraud detection, and comprehensive contact data enrichment.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### Phone Validation (International)
- **Validate Phone Number** - Validates international phone numbers from input data and returns comprehensive metadata including:
  - Activity score (0-100) indicating phone connectivity
  - Line type (Mobile, Landline, VoIP, etc.)
  - Carrier information
  - Country details
  - Prepaid status
  - Optional litigator checks

### Real Contact (US Only)
- **Verify Contact** - Comprehensive contact verification that validates and grades:
  - Phone numbers with activity scoring
  - Email addresses with deliverability checks and age scoring
  - Physical addresses
  - Name matching across all contact points
  - Contact quality grading (A-F scale)
  - Optional fraud and litigator risk assessments

## Credentials

To use this node, you need a Trestle API key.

1. Sign up for a Trestle account at [trestleiq.com](https://trestleiq.com)
2. Generate your API key from the Trestle dashboard
3. In n8n, create a new credential of type "Trestle API"
4. Enter your API key in the credential configuration

## Compatibility
for 
This node is compatible with n8n version 1.0.0 and above.

## Usage

### Phone Validation
1. Add the Trestle node to your workflow
2. Select "Phone Validation" as the resource
3. Configure your Trestle API credentials
4. Set the "Phone Numbers Field" to the input field containing phone numbers
5. Optionally, provide a country hint using ISO-3166 alpha-2 country code (e.g., US)
6. Enable litigator checks if needed (additional cost)
7. Execute the node to validate phone numbers and retrieve activity scores

### Real Contact Verification
1. Add the Trestle node to your workflow
2. Select "Real Contact" as the resource
3. Configure your Trestle API credentials
4. Map input fields for required data:
   - **Name Field** - Field containing contact names
   - **Phone Number Field** - Field containing phone numbers
5. Map optional fields:
   - **Email Field** - Email addresses
   - **Address Field** - Street addresses
   - **City Field**, **State Field**, **Postal Code Field** - Address components
6. Enable additional checks:
   - **Email Deliverability** - Verify email deliverability (additional cost)
   - **Email Age Score** - Get email age scoring (additional cost)
   - **Litigator Check** - Check for litigation risk (additional cost)
7. Execute the node for comprehensive contact verification and grading

## Key Features

- **Real-time Activity Scoring** - Unique 0-100 phone activity scores to identify disconnected numbers
- **Batch Processing** - Process multiple contacts from input data streams
- **Comprehensive Validation** - Phone, email, and address verification in one API
- **Risk Assessment** - Fraud detection and litigator risk identification
- **Quality Grading** - A-F contact quality scores for lead qualification
- **Global Coverage** - International phone validation; US-only contact verification

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Trestle Phone Validation API documentation](https://trestle-api.redoc.ly/Current/tag/Phone-Validation-API)
* [Trestle Real Contact API documentation](https://trestle-api.redoc.ly/Current/tag/Real-Contact-API)
* [Trestle API Documentation](https://trestle-api.redoc.ly/)