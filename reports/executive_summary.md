# Executive Summary: Online Retail EDA

## Overview

This analysis explores transactional data from a UK-based online retailer over two years. The goal is to understand sales patterns, customer behavior, and product performance to support business decisions.

## Data Quality Findings

- **Missing values:** Customer ID is missing for a portion of transactions (guest checkouts). These rows are excluded from customer-level analysis but retained for product and revenue analysis where appropriate.
- **Duplicates:** Some duplicate rows exist, likely from system or data export issues. Duplicates are removed in the cleaning step.
- **Invalid entries:** Negative quantities indicate cancellations/refunds. Zero or negative prices are removed. Negative quantities are flagged as "cancellation" order status.
- **Country imbalance:** UK dominates the dataset. Cross-country analysis should account for this when comparing metrics.

## Revenue and Time Trends

- **Monthly patterns:** Revenue shows seasonal peaks, often around holiday periods (e.g., November–December). Summer months may show different behavior.
- **Peak hours:** The hour vs weekday heatmap reveals when customers shop most. Typically, business hours and evening peaks are visible.
- **Action:** Align inventory, staffing, and marketing campaigns with identified peak periods.

## Product Insights

- **Top sellers:** A small set of products drives a large share of volume. Focus on availability and cross-sell for these items.
- **Price distribution:** Most products are low-to-mid price. High-value items exist but are fewer in count.
- **Action:** Bundle high-volume items, and create targeted campaigns for high-value products.

## Customer Behavior

- **RFM segments:** Champions (high recency, frequency, monetary) are the most valuable. At Risk and Lost segments need re-engagement.
- **Basket size:** Average basket varies by country. UK and some European markets show higher basket sizes.
- **Action:** Loyalty programs for Champions; win-back campaigns for At Risk and Lost.

## Cross-Country Analysis

- **UK dominance:** UK contributes the majority of revenue. International expansion potential exists in other European markets.
- **Growth markets:** Identify countries with strong retention and growing basket size for investment.
- **Action:** Localize offers and shipping for high-potential international markets.

## Cohort Retention

- **Retention heatmap:** Shows how well each cohort retains customers over time. Early retention (first 1–3 months) is a key indicator of long-term value.
- **Action:** Improve onboarding and first-purchase experience to boost early retention.

## Clustering

- **Customer clusters:** K-means on RFM reveals distinct groups (e.g., high-value frequent buyers vs occasional low-spenders).
- **Action:** Use cluster profiles for personalized marketing and product recommendations.

## Recommendations

1. **Inventory:** Stock top products ahead of peak seasons; monitor cancellation rates.
2. **Marketing:** Segment campaigns by RFM; re-engage At Risk and Lost customers.
3. **International:** Prioritize markets with strong retention and growth; test localized offers.
4. **Retention:** Invest in first-purchase experience and early retention programs.
5. **Product mix:** Balance volume drivers with high-margin items; explore bundling.
