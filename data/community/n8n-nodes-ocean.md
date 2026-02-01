# n8n-nodes-ocean

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

This is an n8n community node for [Ocean.io](https://ocean.io) - the leading platform for lookalike company and people discovery.

[Ocean.io](https://ocean.io) helps businesses find their ideal customers by discovering companies and people similar to their best prospects. This n8n node brings Ocean.io's powerful lookalike discovery and data enrichment capabilities directly into your automation workflows.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

1. Go to **Settings > Community Nodes**
2. Select **Install**
3. Enter `n8n-nodes-ocean`
4. Agree to the risks of using community nodes
5. Select **Install**

After installation restart n8n to register the new nodes.

## Operations

### Company Resource

#### Search Companies (1 credit per company)
Find lookalike companies using Ocean.io's discovery engine. This is Ocean.io's core functionality for discovering companies similar to your ideal customers.

**Key Features:**
- **Lookalike Discovery**: Provide example company domains to find similar companies
- **Advanced Filtering**: Filter by employee count, industry, location, and more
- **Pagination Support**: Handle large result sets efficiently

**Parameters:**
- `Lookalike Domains`: Comma-separated list of company domains to find similar companies to
- `Company Name`: Search for companies by name (partial matches supported)
- `Domain`: Search for a specific company domain
- `Employee Count`: Filter by minimum and maximum employee count
- `Countries`: Filter by specific countries
- `Industries`: Filter by specific industries

#### Enrich Company (1 credit with domain, 5 credits without)
Enhance existing company data with Ocean.io's comprehensive database.

**Parameters:**
- `Domain`: Company domain to enrich (recommended for lower cost)
- `Company Name`: Company name to enrich

### Person Resource

#### Search People (1-3 credits per person)
Find lookalike people using Ocean.io's discovery engine. Perfect for finding decision-makers and prospects similar to your best customers.

**Key Features:**
- **Lookalike Discovery**: Provide example LinkedIn handles to find similar people
- **Job Title Filtering**: Target specific roles and seniority levels
- **Company Filtering**: Find people at specific companies or similar companies

**Parameters:**
- `Lookalike People`: Comma-separated list of LinkedIn handles to find similar people to
- `Person Name`: Search for people by name
- `Job Titles`: Filter by specific job titles
- `Company Domains`: Find people from specific companies
- `Countries`: Filter by location

#### Enrich Person (3 credits per person)
Enhance individual prospect data with Ocean.io's database.

**Parameters:**
- `Email`: Email address to enrich
- `LinkedIn Handle`: LinkedIn handle (the part after linkedin.com/in/)
- `Person Name`: Full name of the person to enrich

### Credits Resource

#### Get Credit Balance (Free)
Monitor your Ocean.io API credit usage and remaining balance.

**Returns:**
- Standard credits balance
- Email credits balance (for email reveal operations)
- Phone credits balance (for phone reveal operations)

## Authentication

This node uses Ocean.io's API key authentication. You can find your API key in your Ocean.io dashboard under **Settings > API Keys**.

1. In n8n, create new credentials of type "Ocean.io API"
2. Enter your Ocean.io API key
3. Save the credentials

## Credit Costs

Ocean.io operations consume credits from your account:

- **Company Search**: 1 credit per company returned
- **Company Enrich**: 1 credit (with domain) or 5 credits (without domain)
- **People Search**: 1-3 credits per person (depending on lookalike usage)
- **Person Enrich**: 3 credits per person
- **Credit Balance**: Free operation

## Example Workflows

### Find Lookalike Companies
1. Use **Company > Search Companies**
2. Set `Lookalike Domains` to your best customer domains (e.g., "stripe.com, shopify.com")
3. Add filters for employee count, industry, or location as needed
4. Process results for lead generation or market research

### Enrich CRM Data
1. Use **Company > Enrich Company** or **Person > Enrich Person**
2. Provide domain/email/LinkedIn handle from your CRM
3. Merge enriched data back into your CRM system

### Monitor Credit Usage
1. Use **Credits > Get Credit Balance** before expensive operations
2. Set up conditional logic to prevent workflows from running when credits are low
3. Send alerts when credit balance drops below threshold

## Rate Limits

Ocean.io API has a rate limit of 300 requests per minute. The node handles rate limiting automatically and will retry failed requests when appropriate.

## Error Handling

The node provides detailed error messages for common issues:
- Insufficient credits
- Invalid API key
- Validation errors
- Rate limiting

Enable "Continue on Fail" in your workflow to handle errors gracefully.

## Resources

- [Ocean.io API Documentation](https://docs.ocean.io/)
- [Ocean.io Dashboard](https://app.ocean.io/)
- [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)

## License

[MIT](https://github.com/bcharleson/n8n-nodes-ocean/blob/master/LICENSE.md)

## Support

For issues with this n8n community node, please [open an issue](https://github.com/bcharleson/n8n-nodes-ocean/issues) on GitHub.

For Ocean.io API support, contact [Ocean.io support](https://ocean.io/support).
