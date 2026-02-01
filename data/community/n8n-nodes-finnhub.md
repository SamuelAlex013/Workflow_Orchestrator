![Component palette with Finnhub Node](https://raw.githubusercontent.com/L0rdShrek/n8n-nodes-finnhub/master/docs/logo.png)

<h1 align="center">
  🛠 Finnhub.io REST API node for <code>n8n</code>
</h1>
<p align="center">
	Use the full Finnhub.io REST API inside your n8n workflows.
	<br />
	<br />
	Finnhub delivers real-time market data, fundamentals, alternative datasets, and premium analytics for stocks, forex, crypto, and more.
</p>

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Features
- Covers 90+ Finnhub REST endpoints grouped by resource (stocks, ETFs, funds, forex, crypto, technical analysis, enterprise, institutional, economic, and alternative data).
- Premium toggle surfaces additional paid endpoints only when your credential allows it.
- Generated operations automatically include argument descriptions straight from Finnhub docs.
- Ships with build, lint, and test scripts to keep the node production-ready.

[Installation](#installation)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Operations](#operations)  
[Resources](#resources)  
[Development](#development)  
[Version history](#version-history)  

## Installation
Follow the [community node installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n documentation.

## Credentials
1. Create an account and API token in the [Finnhub dashboard](https://finnhub.io/dashboard).
2. In n8n, add a new **Finnhub.io API** credential and paste the token into the `Token` field.
3. Enable the `Premium Access` checkbox if your subscription unlocks premium endpoints. The node exposes the premium-only resources and operations automatically when this flag (or the credential) is set.

> Tip: You can keep two credentials—one with a sandbox token and one with a live token—to switch between environments quickly.

## Compatibility

- n8n: v1.x
- Node.js for local builds: 18+ (tested with 18, 20, 22)

## Usage

1. Drop the **Finnhub.io** node into your workflow.
2. Select the credential you created earlier. The node prefills the `Premium Access` toggle based on the credential setting.
3. Choose a `Resource`, then pick an `Operation`. Field names and descriptions come directly from the Finnhub API and match the official documentation.
4. Provide any required parameters. Optional parameters can be left empty and are excluded from the request automatically.

![Component palette with Finnhub Node](https://raw.githubusercontent.com/L0rdShrek/n8n-nodes-finnhub/master/docs/component.png)

![Node options in workflow](https://raw.githubusercontent.com/L0rdShrek/n8n-nodes-finnhub/master/docs/node.png)

## Operations

Every REST route defined in `nodes/Finnhub/route-definitions.json` is available in the node. Resources are grouped to mirror the Finnhub documentation:

- **Stock**: Symbol search, quotes, profiles, filings, transcripts, market status, calendars, alternative metrics, and 30+ premium analytics such as ESG, supply chain, valuations, corporate actions, and similarity indexes.
- **ETF & Mutual Fund**: Holdings, profiles, country/sector allocation; premium access adds EET/Pai disclosures and segmentation.
- **Index**: Current and historical constituents, including premium-only datasets.
- **Bond**: Yield curves, tick data, price snapshots, and profiles (premium).
- **Forex & Crypto**: Exchange and symbol directories, candles, and premium rate/profile endpoints.
- **Technical Analysis**: Pattern scans, technical indicator screens, and indicator calculations (premium).
- **Institutional & Enterprise Data**: Ownership, portfolios, bank branches, global filings search/download, AI chat, and more.
- **Economic & Alternative Data**: Country codes, macroeconomic indicators, and the FDA advisory calendar.

Premium-only endpoints are clearly marked inside n8n. Disable `Premium Access` to limit the operation list to free APIs.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Finnhub API Documentation](https://finnhub.io/docs/api)

## Development

Local development and contributions:

- Requirements
  - Node.js 18+ and npm
  - TypeScript 5, ESLint 8, Prettier 3 (installed as devDependencies)

- Helpful scripts
  - `npm run build` – compiles TypeScript and copies icons with Gulp 5
  - `npm run dev` – TypeScript watch mode for rapid iteration
  - `npm run lint` – validates code with ESLint and n8n node rules
  - `npm run lintfix` – same as above with automatic fixes
  - `npm run format` – formats source files with Prettier
  - `npm run test` – builds the project and executes Node.js test suites

- Notes
  - ESLint replaces the deprecated TSLint setup.
  - TypeScript uses `skipLibCheck` to avoid noise from third-party typings.
  - Security-sensitive sub-dependencies (for example, `axios`, `form-data`) are pinned via `package.json` overrides.

## Version history

- 0.2.0
  - Dependencies bumped (TypeScript 5, Prettier 3, ESLint; removed TSLint)
  - Updated to n8n v1.x APIs and adjusted node inputs/outputs
  - Migrated Gulp to v5
  - Added security overrides for axios and form-data
  - Documented development setup and usage guidance
