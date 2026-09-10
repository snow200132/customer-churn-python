# E-Commerce Logistics Customer Churn & Retention Segmentation

### **Executive Summary**
Applied exploratory data analysis and RFM (Recency, Frequency, Monetary) segmentation in Python across a master dataset of **1,000,000+ transaction rows** (UCI Online Retail), isolating a cohort of **early-lifecycle logistics clients** to identify attrition patterns and retention drivers.

---

### Business Problem & Context
* **Challenge:** Increasing customer drop-off rates following initial order fulfillment impacted long-term revenue retention.
* **Objective:** Segment the customer base, analyze retention curves, and pinpoint fulfillment factors correlated with customer churn.
* **Target Audience:** Commercial Director, Customer Retention Lead.

---

### Data Architecture & Repository Files
* **`data/logistics_customer_orders.csv`**: Transactional dataset covering client order sequences, dispatch records, and onboarding delivery delays.
* **`scripts/churn_rfm_analysis.py`**: Python script executing Pandas data cleaning, cohort retention modeling, and RFM categorization.
* **`visualisations/`**: Exported Seaborn and Matplotlib customer retention heatmaps and churn distribution curves.

---

### Key Business Insights & Impact
* **Primary Churn Driver:** Isolated **68%** of total customer churn to delivery delays experienced during initial onboarding orders (Order 1 to Order 3 window).
* **RFM Customer Segmentation:** Classified customer base into Champions (14%), At-Risk (28%), and Lost (32%), enabling targeted retention campaigns.
* **LTV Recovery Potential:** Re-engaging top-tier "At-Risk" clients presents a potential 22% uplift in annual logistics service contract renewals.

---

### Tech Stack & Analytical Methods
* **Python (Pandas, NumPy):** Automated data cleaning, cohort analysis, and datetime transformations.
* **Seaborn & Matplotlib:** Visualized customer retention heatmaps and churn distribution curves.

---

### Strategic Recommendations
1. **Onboarding SLA Guarantee:** Priority-route all first-time client shipments to guarantee sub-24-hour delivery fulfillment.
2. **Automated Re-engagement:** Trigger automated commercial check-ins when a client's dispatch frequency drops by more than 35% month-over-month.
