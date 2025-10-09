# n8n-nodes-hmac

This is an n8n community node. It lets you use **HMAC authentication** in your n8n workflows.

**HMAC (Hash-based Message Authentication Code)** is a cryptographic authentication method that ensures the integrity and authenticity of HTTP requests. This node enables secure API communication by automatically generating and attaching HMAC signatures to your HTTP requests, supporting various signature patterns used by popular APIs like AWS, Stripe, and Binance.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Usage](#usage)
[Resources](#resources)
[Version history](#version-history)

---

## Installation

Follow the installation guide in the n8n community nodes documentation.

1. Go to **Settings** > **Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-hmac` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5. Select **Install**. 

After installing the node, you can use it like any other node. n8n displays the node in search results in the **Nodes** panel.

---

## Operations

This node supports HTTP requests with HMAC signature authentication:

### HTTP Methods

* **GET** - Retrieve data from an API
* **POST** - Send data to create resources
* **PUT** - Update existing resources
* **PATCH** - Partially update resources
* **DELETE** - Remove resources

### HMAC Features

* **Multiple algorithms**: SHA-1, SHA-256, SHA-384, SHA-512
* **Encoding options**: Hexadecimal or Base64
* **Signature placement**: HTTP headers or query parameters
* **Timestamp support**: Unix, Unix milliseconds, or ISO 8601
* **Content types**: JSON, form data, or raw strings

### Signature Patterns

* **Simple** - Raw body string
* **AWS V4** - AWS-style canonical request format
* **Stripe** - Timestamp + body format
* **Binance** - Timestamp + method + path + query + body
* **Custom** - Define your own pattern with placeholders

---

## Credentials

This node requires HMAC API credentials:

### HMAC API Key

Set up your HMAC credentials with:

* **API Key/Secret**: The secret key used for HMAC signature generation

To configure:

* In n8n, go to **Credentials** and create new **HMAC API** credentials
* Enter your secret key in the **API Key** field
* Save and use in your HMAC Request nodes

---

## Compatibility

* **Tested on:** `1.111.1`

Known limitations:

* Custom signature patterns require understanding of the target API's specific requirements
* Some APIs may have additional header or parameter requirements beyond HMAC signatures

---

## Usage

### Basic Configuration

1. **Select HTTP method** (GET, POST, PUT, PATCH, DELETE)
2. **Enter the target URL**
3. **Choose HMAC algorithm** (SHA-256 recommended)
4. **Set encoding format** (hex or base64)
5. **Select signature pattern** or create custom pattern

### Signature Patterns

Choose from predefined patterns:

* **Simple**: Basic HMAC of request body
* **AWS V4**: Amazon Web Services signature format
* **Stripe**: Webhook signature verification format
* **Binance**: Cryptocurrency exchange API format
* **Custom**: Use placeholders like `{method}`, `{path}`, `{query}`, `{body}`, `{timestamp}`

### Request Body

For POST/PUT/PATCH requests:

* **JSON**: Structured data sent as application/json
* **Form Data**: URL-encoded form fields
* **Raw**: Plain text or custom format strings

### Additional Options

* **Headers**: Add custom HTTP headers
* **Query Parameters**: URL query string parameters
* **Timeout**: Request timeout in milliseconds
* **Timestamp**: Optional timestamp inclusion with various formats

---

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html)
* [Stripe Webhook Signatures](https://stripe.com/docs/webhooks/signatures)

---

## Version history

| Version | Changes                                                                                                    |
|---------|-----------------------------------------------------------------------------------------------------------|
| 1.0.0   | Initial release with support for HMAC signatures, multiple algorithms, signature patterns, and HTTP methods |