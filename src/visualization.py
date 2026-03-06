"""
Visualization utilities for Online Retail EDA.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# Consistent style for publication-ready plots
try:
    plt.style.use("seaborn-v0_8-whitegrid")
except OSError:
    plt.style.use("seaborn-whitegrid")
COLORS = ["#2ecc71", "#3498db", "#9b59b6", "#e74c3c", "#f39c12", "#1abc9c"]


def setup_plot_style():
    """Set consistent matplotlib style."""
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.rcParams["font.size"] = 11
    plt.rcParams["axes.titlesize"] = 14
    plt.rcParams["axes.labelsize"] = 12


def save_figure(filename: str, dpi: int = 150, bbox_inches: str = "tight"):
    """Save current figure to reports/figures."""
    fig_path = Path(__file__).parent.parent / "reports" / "figures" / filename
    fig_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(fig_path, dpi=dpi, bbox_inches=bbox_inches)
    plt.close()


def plot_monthly_revenue(monthly_df, ax=None):
    """Line chart of monthly revenue."""
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(monthly_df.index, monthly_df.values, color="#3498db", linewidth=2)
    ax.fill_between(monthly_df.index, monthly_df.values, alpha=0.3)
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue")
    ax.set_title("Monthly Revenue Trend")
    ax.tick_params(axis="x", rotation=45)
    return ax


def plot_heatmap(data, xlabel="", ylabel="", title="", cmap="YlOrRd"):
    """Create a heatmap."""
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(data, annot=True, fmt=".0f", cmap=cmap, ax=ax, cbar_kws={"label": "Sales"})
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    return fig, ax


def plot_top_n_bars(series, n=10, title="", color="#3498db", horizontal=True):
    """Bar chart for top N items."""
    top = series.head(n)
    fig, ax = plt.subplots(figsize=(10, 6))
    if horizontal:
        top.plot(kind="barh", ax=ax, color=color)
        ax.set_ylabel("")
    else:
        top.plot(kind="bar", ax=ax, color=color)
        ax.set_xlabel("")
    ax.set_title(title)
    ax.tick_params(axis="x", rotation=45)
    return fig, ax
