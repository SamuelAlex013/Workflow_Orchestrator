# n8n-nodes-extruct

![Extruct AI Banner](icons/banner.png)

**n8n community node for Extruct AI**

This node lets you enrich and fetch company data from Extruct AI, right inside your n8n workflows.
Define your own table structure, add any custom columns, and get exactly the data you need.

### Instant preview

Suppose you want to enrich a company by website and get its funding, team size, recent news headline, patent count, and head of HR LinkedIn profile.


```json
{
  "company_name": {
    "value": {
      "answer": "Stripe",
      "source": [
        "https://en.wikipedia.org/wiki/Stripe,_Inc."
      ],
      "explanation": "Full company name as listed on the Stripe Wikipedia page."
    }
  },
  "company_website": {
    "value": {
      "answer": "https://stripe.com/",
      "source": [
        "https://en.wikipedia.org/wiki/Stripe,_Inc.",
        "https://stripe.com"
      ],
      "explanation": "Canonical homepage confirmed on Wikipedia and the stripe.com domain."
    }
  },
  "recent_news_headline": {
    "value": {
      "answer": "Stripe’s first employee, the founder of fintech Increase, sort of bought a bank",
      "source": [
        "https://techcrunch.com/2025/07/03/stripes-first-employee-the-founder-of-fintech-increase-sort-of-bought-a-bank"
      ],
      "explanation": "Headline from a TechCrunch article published July 3, 2025, as the latest news about Stripe."
    }
  },
  "team_size": {
    "value": {
      "answer": "8550",
      "source": [
        "https://techcrunch.com/2025/01/21/stripe-is-laying-off-300-people-but-says-it-still-plans-to-hire-in-2025"
      ],
      "explanation": "About 8,550 employees after a January 2025 layoff of 300 people, per TechCrunch."
    }
  },
  "patent_count": {
    "value": {
      "answer": "247",
      "source": [
        "https://insights.greyb.com/stripe-patents"
      ],
      "explanation": "Total of 247 patents held globally by Stripe, according to GreyB Insights."
    }
  },
  "funding_amount": {
    "value": {
      "answer": "$9.81B",
      "source": [
        "https://tracxn.com/d/companies/stripe/__uahG_IGnVgsUsOG-f8otYHLkOkliWg7YFhJ5ZkNIkpI/funding-and-investors",
        "https://www.crunchbase.com/organization/stripe/company_financials"
      ],
      "explanation": "Raised $9.81 B over 24 rounds, including a $6.87 B round in March 2023, per Tracxn and Crunchbase."
    }
  },
  "head_of_hr_linkedin": {
    "value": {
      "answer": "https://www.linkedin.com/in/maiaj",
      "source": [
        "https://www.comparably.com/companies/stripe/maia-josebachvili",
        "https://www.linkedin.com/in/maiaj"
      ],
      "explanation": "Confirmed as Head of People at Stripe via Comparably and LinkedIn."
    }
  }
}
```



## What is Extruct AI?

**Extruct AI** is a data enrichment platform that lets you create custom tables with any columns you want, and then enrich them with company data from the web and public sources.  

- **Any info you want:** Define your own columns — get emails, social links, funding, tech stack, or anything else.
- **No limits:** Works for any company, in any country, any industry.
- **Built for automation:** Integrate with CRMs, lead gen, analytics, and more.



## Features

- Add a company to your Extruct table and trigger enrichment
- Poll for enrichment completion automatically
- Instantly fetch the enriched row with all your custom columns
- Use in any n8n workflow



## Installation

Follow the [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/) for installing custom nodes.



## Usage

1. **Create an Extruct table:**
   - You can start from a template table or create your own from scratch at [Extruct AI](https://extruct.ai).
   - Add any custom columns you need — you have full control over the table structure and fields.
2. **Get your Table ID:**
   - After creating the table, copy its Table ID from the Extruct dashboard, or simply grab it from the table page URL.
3. **Use in n8n:**
   - In the Extruct node, paste your Table ID.
   - Enter the company name or website you want to enrich:
     - You can type it manually in the node field,
     - Or pass it dynamically from a Form Trigger,
     - Or from any other node in your workflow — just connect it to the Extruct node.
   - Run the workflow — the node will add the company, trigger enrichment, and return the enriched data for your custom columns.

## Quick Demo

![n8n node demo](https://github.com/zodackwand/extruct_screenshots/blob/main/demo.gif?raw=true)


## Operations

### Enrich Company Info

- **Input:**  
  - Table ID (your Extruct table)
  - Company Input (website or name)
- **Output:**  
  - Returns a fully enriched row with all your custom columns as clean JSON, ready to use in your n8n workflow.

**How it works:**  
1. Adds a company to your Extruct table  
2. Triggers enrichment  
3. Waits for completion  
4. Returns the enriched row (with all your custom fields)



## Output
The node returns clean JSON with all enriched fields for the company, matching your custom table columns.



## Extruct Table Templates
Use these ready-to-go table templates for your n8n workflows:

- [Sales and Business Development](https://app.extruct.ai/tables/shared/jlcBdFwKXrC8uw21)  
  *Track leads, enrich company profiles, and automate sales research.*

- [Complete Startup Overview](https://app.extruct.ai/tables/shared/gQlqQK4pQgPDmk81)  
  *Get a 360° view of startups with funding, team, and product data.*

- [Social Enrichment](https://app.extruct.ai/tables/shared/VfGemEC1BujAIJx8)  
  *Enrich companies with social profiles, Twitter, LinkedIn, and more.*

Open a template, get the Table ID, and use it in your node.



## Credentials

- **Extruct API Token**  
  - Sign up at [extruct.ai](https://extruct.ai)
  - Get your API token from the dashboard
  - Add it as a credential in n8n



## Resources

- [Extruct AI website](https://extruct.ai)
- [n8n Community Nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Extruct AI API Docs](https://www.extruct.ai/docs/extruct-ai/product)



## Compatibility

- **n8n:** Tested with n8n v1.100.0
