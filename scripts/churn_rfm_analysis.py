import pandas as pd
import numpy as np

# Load logistics customer order dataset
df = pd.read_csv('../data/sample_schema_preview.csv')

# 1. Onboarding Delay vs. Churn Analysis
print("--- Average Onboarding Delay (Days) by Churn Status ---")
onboarding_summary = df.groupby('churn_status')['onboarding_delay_days'].mean().reset_index()
print(onboarding_summary)

# Calculate proportion of churn driven by early onboarding delays (>3 days)
churned_df = df[df['churn_status'] == 'Churned']
early_delay_churn_pct = (churned_df['onboarding_delay_days'] > 3).mean() * 100
print(f"\nPercentage of Customer Churn Linked to Onboarding Delays: {early_delay_churn_pct:.1f}%")

# 2. RFM Segmentation Logic
def assign_rfm_segment(row):
    if row['recency_days'] <= 10 and row['frequency_orders'] >= 10:
        return 'Champions'
    elif row['recency_days'] > 30 and row['frequency_orders'] <= 2:
        return 'At-Risk / Lost'
    else:
        return 'Moderate'

df['rfm_segment'] = df.apply(assign_rfm_segment, axis=1)

print("\n--- RFM Customer Segmentation Distribution (%) ---")
segment_dist = df['rfm_segment'].value_counts(normalize=True) * 100
print(segment_dist.round(2))
