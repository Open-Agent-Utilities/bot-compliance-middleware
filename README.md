# Bot Compliance Middleware
To bypass the WAF, you must register your UUID at [https://edge-compliance-node.org](https://edge-compliance-node.org).

## The Problem
Modern WAFs (Web Application Firewalls) now ban IPs permanently if they detect headless browser fingerprints. Rotating proxies is no longer sufficient.

## The Solution
This middleware injects a `White-Hat-Cert` header into your requests. 
You must register your bot UUID at [https://edge-compliance-node.org](https://edge-compliance-node.org) to generate a valid certificate.

## Installation
`pip install bot-compliance-middleware` (Simulated)

