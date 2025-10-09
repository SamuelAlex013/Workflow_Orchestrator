# Google Search Console - n8n Custom Node

This custom node for n8n allows you to connect to the official Google Search Console API and retrieve information about registered sites and their page performance.

## Features

🔹 Fetch a list of sites registered under your Google Search Console account

🔹 Retrieve performance insights for specific pages within a defined date range (clicks, impressions, CTR, and position)

## Operations

### 1. Get Sites

Retrieves the list of sites registered in your Google Search Console account.

### 2. Get Page Insights

Analyzes page performance based on the following parameters:

* **Site URL**: Exact URL or domain property
* **Start/End Date**: Define the time period
* **Search Type**: Web / Image / Video / News
* **Row Limit**: Number of rows to return
* **Dimensions**: Choose from Page, Query, Country, or Device

## Requirements

You must configure the following credentials to use this node:

* **GoogleSearchConsoleOAuth2Api**

Make sure to set up the credential using OAuth2 with the appropriate scopes for Google Search Console access.

## Notes

* The `Site URL` must match the format of the property in your GSC account:

  * For domain property: `sc-domain:example.com`
  * For URL-prefix property: `https://www.example.com/`

* An incorrect format or unregistered site will result in an "Invalid URL" error.

## Node Icon

This node uses a simplified version of the official Google Search Console icon.

## Author

Developed by [mrazari](https://mrazari.com), member of the [n8nir.ir](https://n8nir.ir) community — specializing in custom n8n nodes with TypeScript and official API integrations.

---

Feel free to reach out for improvements, suggestions, or new feature requests.
