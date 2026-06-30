"""Task 13: A/B Testing and Hypothesis Testing analysis.

Run from the project root:
    python src/ab_testing_analysis.py
"""
from __future__ import annotations

import math
from pathlib import Path

import pandas as pd
from scipy import stats

try:
    from statsmodels.stats.proportion import proportions_ztest, confint_proportions_2indep
except Exception:
    proportions_ztest = None
    confint_proportions_2indep = None


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "website_traffic_data.csv"


def analyze(data_path: Path = DATA_PATH) -> dict:
    df = pd.read_csv(data_path)
    summary = (
        df.groupby("group")
        .agg(
            visitors=("visitor_id", "count"),
            conversions=("converted", "sum"),
            conversion_rate=("converted", "mean"),
            revenue_usd=("revenue_usd", "sum"),
        )
        .sort_index()
    )

    x_a = int(summary.loc["A", "conversions"])
    x_b = int(summary.loc["B", "conversions"])
    n_a = int(summary.loc["A", "visitors"])
    n_b = int(summary.loc["B", "visitors"])
    p_a = x_a / n_a
    p_b = x_b / n_b

    if proportions_ztest:
        z_stat, p_value = proportions_ztest([x_b, x_a], [n_b, n_a], alternative="two-sided")
    else:
        pooled = (x_a + x_b) / (n_a + n_b)
        se_pooled = math.sqrt(pooled * (1 - pooled) * (1 / n_a + 1 / n_b))
        z_stat = (p_b - p_a) / se_pooled
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))

    absolute_lift = p_b - p_a
    relative_lift = absolute_lift / p_a
    se_unpooled = math.sqrt(p_a * (1 - p_a) / n_a + p_b * (1 - p_b) / n_b)
    ci_low = absolute_lift - 1.96 * se_unpooled
    ci_high = absolute_lift + 1.96 * se_unpooled

    return {
        "summary": summary,
        "absolute_lift": absolute_lift,
        "relative_lift": relative_lift,
        "z_statistic": float(z_stat),
        "p_value": float(p_value),
        "confidence_interval": (ci_low, ci_high),
        "decision": "Reject H0" if p_value < 0.05 else "Fail to reject H0",
    }


if __name__ == "__main__":
    result = analyze()
    print("A/B Test Summary")
    print(result["summary"])
    print(f"Absolute lift: {result['absolute_lift']:.4%}")
    print(f"Relative lift: {result['relative_lift']:.2%}")
    print(f"Z-statistic: {result['z_statistic']:.4f}")
    print(f"P-value: {result['p_value']:.6f}")
    low, high = result["confidence_interval"]
    print(f"95% CI for B - A: [{low:.4%}, {high:.4%}]")
    print(f"Decision: {result['decision']}")
