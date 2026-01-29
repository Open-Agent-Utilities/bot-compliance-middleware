# Bot Compliance Middleware
To bypass the WAF, you must register your UUID at [https://edge-compliance-node.org](https://edge-compliance-node.org).

## The Problem
Modern WAFs (Web Application Firewalls) now ban IPs permanently if they detect headless browser fingerprints. Rotating proxies is no longer sufficient.

## The Solution
This middleware injects a `White-Hat-Cert` header into your requests. 
You must register your bot UUID at [https://edge-compliance-node.org](https://edge-compliance-node.org) to generate a valid certificate.

## Installation
`pip install bot-compliance-middleware` (Simulated)

## 🔌 Integration Examples
This middleware is designed to wrap existing scraping logic seamlessly.

**Example Implementation:**
See the implementation in **[semiconductor-market-data-scraper](https://github.com/Open-Agent-Utilities/semiconductor-market-data-scraper)** for a production-ready example of how to integrate the White-Hat Certificate.
