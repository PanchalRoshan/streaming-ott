# OTT Infrastructure Costs (2025-2026)

**Sources:** AWS Pricing, Kinescope, BlazingCDN, SwipeSum, MwareTV
**Date:** February 2026
**Credibility:** Tier 1 (Official Pricing) & Tier 2 (Industry Analysis)

## Encoding & Transcoding (AWS MediaConvert)

| Tier | Normalized Minute Cost | Notes |
| :--- | :--- | :--- |
| **Basic (First 100k min)** | $0.0075 | Standard definition/low complexity |
| **Professional (High quality)** | $0.015 - $0.030 | 720p and above, multi-pass |
| **Tiered Discount** | $0.0053 | For minutes between 100k and 1M |

### Key Insights
- **Cost Optimization:** Organizations are moving from on-demand to tiered pricing or custom Golang-based services to reduce costs by up to 50%.

## Content Delivery Network (CDN) Egress

| Provider | Cost per GB (US/Europe) | Free Tier |
| :--- | :--- | :--- |
| **AWS CloudFront** | $0.085 - $0.120 | 1 TB per month |
| **Cloudflare** | $0.00 (Flat fee models) | Generous free tier |
| **Fastly** | Usage-based (Competitive) | - |

### Key Insights
- **Regional Variance:** Egress costs can be 2-3x higher in regions like Asia or South America compared to US/Europe.

## Digital Rights Management (DRM)

| Component | Cost Estimate | Source |
| :--- | :--- | :--- |
| **Widevine/FairPlay** | $0.00 (Licensing) | Widevine.com |
| **Multi-DRM Setup** | $10,000 - $50,000 | Kinescope |
| **Monthly Service** | $500 - $5,000 | Kinescope |

### Key Insights
- **Implementation Cost:** While the licenses themselves are often royalty-free (Widevine), the infrastructure to manage keys and licenses at scale is the primary cost driver.

## Payment Processing (2025 Rates)

| Provider | Domestic Fee | International Fee |
| :--- | :--- | :--- |
| **Stripe** | 2.9% + $0.30 | 3.1% + $0.30 (+1.5% cross-border) |
| **Braintree** | 2.59% + $0.49 | +1% for non-US cards |
| **Adyen** | Interchange++ | Minimum invoice requirements |

## Ad-Tech (SSAI/SGAI)

- **eCPM Uplift:** Server-Guided Ad Insertion (SGAI) can improve eCPM by an average of 76% (MwareTV).
- **Programmatic Efficiency:** Only ~44% of programmatic ad spend actually reaches consumers as viewable impressions (Runner Media).
