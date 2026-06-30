# Task 13: A/B Testing and Hypothesis Testing

Author: Arshpreet Singh

## Project Overview
This submission validates a website A/B test scientifically. It compares Variant A and Variant B using conversion-rate analysis, a two-proportion hypothesis test, and a 95% confidence interval.

## Hypotheses
- H0: Variant B conversion rate is equal to Variant A conversion rate.
- H1: Variant B conversion rate is different from Variant A conversion rate.
- Significance level: 0.05

## Key Result
- Group A conversion rate: 12.33%
- Group B conversion rate: 15.50%
- Absolute lift: 3.17%
- Relative lift: 25.68%
- P-value: 0.025023
- 95% confidence interval for B - A: [0.40%, 5.93%]
- Decision: Reject H0

## Folder Structure
- `data/website_traffic_data.csv` - Website traffic A/B test dataset.
- `notebooks/Task_13_AB_Testing_Hypothesis_Testing.ipynb` - Python notebook for submission.
- `src/ab_testing_analysis.py` - Reusable Python analysis script.
- `reports/AB_Test_Report.md` - Written A/B test report.
- `reports/AB_Test_Report.pdf` - PDF version of the report.
- `reports/ab_test_summary.csv` - Group-level conversion and revenue summary.
- `screenshots/ab_test_conversion_rate_screenshot.png` - Screenshot-style chart for submission proof.
- `requirements.txt` - Python dependencies.

## How To Run
```bash
pip install -r requirements.txt
python src/ab_testing_analysis.py
```

If `python` is not available on PATH in Windows PowerShell, use the installed Python launcher or your full Python executable path:

```powershell
py src\ab_testing_analysis.py
```

Open the notebook from the project root or from the `notebooks` folder. The path handling supports both launch locations.
