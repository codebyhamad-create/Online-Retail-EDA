# Online Retail EDA Project

Exploratory data analysis of the Online Retail II dataset from UCI/Kaggle. This project covers data quality assessment, feature engineering, time series analysis, customer segmentation (RFM), cohort retention, and clustering.

## Dataset

- **Source:** [Kaggle - Online Retail II](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci) or [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/online+retail+II)
- **Description:** Real transactional data from a UK-based online retailer spanning two years of global sales
- **Format:** CSV or Excel (multiple sheets for different years)

## Project Structure

```
Online-Retail-EDA/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/                 # Original dataset (do not modify)
│   ├── processed/           # Cleaned data for analysis
│   └── external/            # Reference data
├── notebooks/
│   ├── 01_data_overview.ipynb      # Data understanding, quality assessment
│   ├── 02_data_cleaning.ipynb      # Cleaning and feature engineering
│   ├── 03_eda.ipynb                # Main EDA and visualizations
│   └── 04_advanced_analysis.ipynb  # RFM, cohort, clustering
├── reports/
│   ├── figures/             # Exported charts
│   └── executive_summary.md # Business insights
└── src/
    ├── cleaning.py
    ├── feature_engineering.py
    └── visualization.py
```

## Setup

1. Place the dataset in `data/raw/` as `online_retail_II.csv` (or `OnlineRetailII.xlsx`)
2. Install dependencies: `pip install -r requirements.txt`
3. Run notebooks in order: 01 -> 02 -> 03 -> 04

## Key Deliverables

- **Data Quality:** Summary of missing values, duplicates, invalid entries, and cleaning strategy
- **Features:** InvoiceDate parsing, Sales (Quantity x Price), OrderStatus, customer aggregates
- **Visualizations:** Monthly revenue, hour/weekday heatmap, top products, price distribution, country analysis
- **Advanced:** RFM segmentation, cohort retention heatmap, K-means clustering

## Insights

See `reports/executive_summary.md` for business-oriented insights and recommendations.

## License

MIT (optional)
