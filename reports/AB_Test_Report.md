# A/B Test Report: Website Traffic Data

Author: Arshpreet Singh

## Objective
The objective is to determine whether website Variant B changes conversion performance compared with Variant A.

## Dataset
The dataset contains 2,400 website visits split evenly between Group A and Group B. Each row includes visitor ID, visit date, experiment group, device, traffic channel, session activity, conversion flag, and revenue.

## Hypotheses
- H0: Conversion rate for Group B equals conversion rate for Group A.
- H1: Conversion rate for Group B differs from conversion rate for Group A.
- Alpha: 0.05

## Group Comparison
| Group | Visitors | Conversions | Conversion Rate | Revenue |
|---|---:|---:|---:|---:|
| A | 1200 | 148 | 12.33% | $8522.00 |
| B | 1200 | 186 | 15.50% | $11560.11 |

## Statistical Test
A two-proportion z-test was used because the target metric is binary conversion and the experiment compares two independent groups.

- Z-statistic: 2.2410
- P-value: 0.025023
- Absolute lift: 3.17%
- Relative lift: 25.68%
- 95% confidence interval for B - A: [0.40%, 5.93%]

## Decision
Reject H0 at alpha = 0.05.

## Business Interpretation
Variant B shows a higher observed conversion rate than Variant A. Because the confidence interval is above zero and the p-value is below 0.05, the result supports Variant B as the better-performing experience for conversion.

## Interview Questions
**What is A/B testing?** A/B testing is a controlled experiment that compares two versions of a product, page, or process to determine whether a change improves a selected metric.

**What is a confidence interval?** A confidence interval is a range of plausible values for an estimated effect. Here, it estimates the likely conversion-rate difference between Variant B and Variant A.
