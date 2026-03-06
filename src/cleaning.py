"""
Data cleaning utilities for Online Retail II dataset.
"""

import pandas as pd
import numpy as np
from pathlib import Path


def load_raw_data(data_path: str) -> pd.DataFrame:
    """
    Load the raw dataset. Supports CSV and Excel formats.
    """
    path = Path(data_path)
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {data_path}")

    if path.suffix.lower() == ".csv":
        df = pd.read_csv(path, encoding="utf-8")
    elif path.suffix.lower() in [".xlsx", ".xls"]:
        df = pd.read_excel(path, sheet_name=None)
        if isinstance(df, dict):
            df = pd.concat(df.values(), ignore_index=True)
    else:
        raise ValueError(f"Unsupported file format: {path.suffix}")

    return df


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names. Handles both 'Price' and 'UnitPrice' variants.
    """
    df = df.copy()
    col_map = {
        "Customer ID": "CustomerID",
        "Invoice": "InvoiceNo",
        "StockCode": "StockCode",
        "Description": "Description",
        "Quantity": "Quantity",
        "InvoiceDate": "InvoiceDate",
        "Price": "UnitPrice",
        "UnitPrice": "UnitPrice",
        "Country": "Country",
    }
    df = df.rename(columns={k: v for k, v in col_map.items() if k in df.columns})
    return df


def clean_retail_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply full cleaning pipeline:
    - Remove rows with missing CustomerID
    - Remove duplicate rows
    - Remove invalid quantities (zero or negative for non-cancellations)
    - Remove invalid prices (zero or negative)
    - Filter out cancellation-only rows if needed for analysis
    """
    df = df.copy()

    # Drop rows with missing CustomerID (required for customer analysis)
    df = df.dropna(subset=["CustomerID"])
    df["CustomerID"] = df["CustomerID"].astype(int)

    # Drop duplicate rows
    df = df.drop_duplicates()

    # Remove rows with zero or negative price
    df = df[df["UnitPrice"] > 0]

    # Keep negative quantities (cancellations) for now - we'll flag them
    # Only remove if both quantity and price are problematic
    df = df[df["Quantity"] != 0]

    return df.reset_index(drop=True)


def get_data_quality_summary(df: pd.DataFrame) -> dict:
    """
    Generate a summary of data quality issues.
    """
    summary = {
        "total_rows": len(df),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicates": df.duplicated().sum(),
        "negative_quantity_count": (df["Quantity"] < 0).sum(),
        "zero_quantity_count": (df["Quantity"] == 0).sum(),
        "negative_price_count": (df["UnitPrice"] < 0).sum() if "UnitPrice" in df.columns else 0,
        "zero_price_count": (df["UnitPrice"] == 0).sum() if "UnitPrice" in df.columns else 0,
        "unique_invoices": df["InvoiceNo"].nunique(),
        "unique_customers": df["CustomerID"].nunique() if "CustomerID" in df.columns else 0,
        "unique_products": df["StockCode"].nunique(),
        "countries": df["Country"].nunique(),
    }
    return summary
