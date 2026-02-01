# n8n-nodes-yahoo-jp-yolp

This is an n8n community node. It lets you use **Yahoo JP YOLP** (Yahoo!ローカルサーチAPI、Yahoo!ジオコーダAPI、Yahoo!リバースジオコーダAPI) in your n8n workflows.

Yahoo! Open Local Platform (YOLP) is a map and local information API and SDK provided by Yahoo! Maps for developers.

[n8n](https://n8n.io/) is a [fair‑code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Resources](#resources)
[Version history](#version-history)

---

## Installation

Follow the **Installation guide** in the \[n8n community nodes documentation]
For self‑hosted instances: go to **Settings → Community Nodes**, click **Install**, enter `n8n‑nodes‑yahoo‑jp‑yolp`, acknowledge risks, and proceed ([docs.n8n.io][3]).

---

## Operations

- **Geocode**

  - Input: Address string
  - Output: Latitude and longitude
  - Endpoint: `https://map.yahooapis.jp/geocode/V1/geoCoder`

- **Reverse Geocoder**

  - Input: Latitude and longitude
  - Output: Address details
  - Endpoint: `https://map.yahooapis.jp/geoapi/V1/reverseGeoCoder`

---

## Credentials

This node requires an **AppId** (API key) from Yahoo! Developer Dashboard:

1. Go to the [Yahoo! Developer Dashboard](https://e.developer.yahoo.co.jp/dashboard/), sign in or sign up.
2. Create an application and obtain your **AppId**.
3. Paste the AppId into the `AppId` credential field in n8n.

---

## Compatibility

- **Minimum supported n8n version:** v1.97.1
- **Tested versions:** v1.97.1 (latest stable as of June 2025)
- **Known issues:** None reported so far

---

## Resources

- \[Installation guide for community nodes – n8n Docs]
- \[Submit community nodes – n8n Docs]&#x20;
- Yahoo! Open Local Platform (YOLP) API documentation:

  - Geocoder: `https://developer.yahoo.co.jp/webapi/map/openlocalplatform/v1/geocoder.html`
  - ReverseGeocoder: `https://developer.yahoo.co.jp/webapi/map/openlocalplatform/v1/reversegeocoder.html`

---

## Version history

| Version | Description                                         |
| ------- | --------------------------------------------------- |
| 0.0.2   | Initial release: Geocode & Reverse Geocoder support |
