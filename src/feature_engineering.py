"""
Feature engineering for Online Retail II dataset.
"""

import pandas as pd
import numpy as np
from datetime import datetime


def parse_invoice_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert InvoiceDate to datetime and extract temporal features.
    """
    df = df.copy()
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month
    df["DayOfWeek"] = df["InvoiceDate"].dt.dayofweek
    df["DayName"] = df["InvoiceDate"].dt.day_name()
    df["Hour"] = df["InvoiceDate"].dt.hour
    df["Date"] = df["InvoiceDate"].dt.date

    return df


def create_sales_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create Sales = Quantity * UnitPrice.
    """
    df = df.copy()
    df["Sales"] = df["Quantity"] * df["UnitPrice"]
    return df


def create_order_status(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create order status category: 'normal' vs 'cancellation'.
    """
    df = df.copy()
    df["OrderStatus"] = np.where(df["Quantity"] < 0, "cancellation", "normal")
    return df


def aggregate_customer_metrics(df: pd.DataFrame, reference_date: datetime = None) -> pd.DataFrame:
    """
    Aggregate customer behavior: total revenue, frequency, recency.
    """
    if reference_date is None:
        reference_date = df["InvoiceDate"].max()

    customer_df = (
        df[df["OrderStatus"] == "normal"]
        .groupby("CustomerID")
        .agg(
            TotalRevenue=("Sales", "sum"),
            PurchaseFrequency=("InvoiceNo", "nunique"),
            LastPurchaseDate=("InvoiceDate", "max"),
        )
        .reset_index()
    )

    customer_df["RecencyDays"] = (
        pd.to_datetime(reference_date) - customer_df["LastPurchaseDate"]
    ).dt.days

    return customer_df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply full feature engineering pipeline.
    """
    df = parse_invoice_date(df)
    df = create_sales_column(df)
    df = create_order_status(df)
    return df
