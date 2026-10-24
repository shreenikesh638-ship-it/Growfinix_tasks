# Growfinix_tasks

# Growfinix Technology - Data Analytics Internship Projects

This repository contains the completed deliverables for the Growfinix Technology internship tasks, covering Business Intelligence dashboard development, exploratory data analysis, and statistical hypothesis testing.

---

## Task 1: Real Estate Interactive Pricing Dashboard
* **Tool:** Tableau Public
* **Dataset:** Real Estate Pricing Data (Kaggle)
* **Live Dashboard:** [View on Tableau Public](https://public.tableau.com/) *(replace with your link)*

### Key Features:
* Dynamic map visualization mapping property listings across target locations.
* Core scorecard KPI calculating `Average Property Price` dynamically.
* Interactive controls:
  * Multi-select neighborhood dropdown filter.
  * Square footage (`Clean_Size`) range slider.
  * Proximity to schools distance range slider.
* Unified data filtering linking all dashboard elements simultaneously.

---

## Task 2: A/B Testing Analysis for Media Campaigns
* **Tool:** Python (`pandas`, `scipy.stats`, `matplotlib`, `seaborn`)
* **Context:** Luxury campaign engagement testing (Edit A vs. Edit B) for the 308 Group.
* **Script:** `Task2_AB_Testing/ab_test_analysis.py`

### Statistical Analysis & Methodology:
1. **Watch Time Retention (Continuous Metric):**
   * Two-Sample Independent T-Test ($t$-test).
   * Verified statistical significance ($p < 0.05$) to demonstrate Edit B's superior viewer retention.
2. **Click-Through Rate (Categorical Metric):**
   * Chi-Square Test of Independence ($\chi^2$).
   * Confirmed statistically significant lift in user conversion toward the call-to-action (CTA).
* Output plots saved in `Task2_AB_Testing/ab_testing_results.png`.

---

## Task 4: Telco Customer Churn Analysis & Retention Strategy
* **Tool:** Tableau Public
* **Dataset:** Telco Customer Churn (Kaggle)
* **Live Dashboard:** [View on Tableau Public](https://public.tableau.com/) *(replace with your link)*

### Key Features:
* Executive scorecard tracking `Overall Churn Rate` via custom calculated fields.
* Segmented horizontal bar breakdown analyzing churn rates across contract types (Month-to-month, One year, Two year).
* Interactive filter controls for `Internet Service` (DSL, Fiber optic, No) and `Senior Citizen` status applied across all worksheets.

---

## Setup & Execution (Python Tasks)
To replicate the statistical tests:
```bash
cd Task2_AB_Testing
python3 ab_test_analysis.py
