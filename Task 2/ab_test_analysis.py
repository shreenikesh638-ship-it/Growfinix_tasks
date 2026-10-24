import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Set seed for reproducibility
np.random.seed(42)
n_samples = 1500

# 1. Simulate Campaign Data for 308 Group Luxury Birthday Event
# Edit A: Traditional Elegant Cinematic Cut
watch_time_A = np.random.normal(loc=38.5, scale=8.2, size=n_samples)
clicks_A = np.random.binomial(n=1, p=0.082, size=n_samples)  # 8.2% CTR

# Edit B: Dynamic Fast-Paced Cut
watch_time_B = np.random.normal(loc=42.1, scale=8.5, size=n_samples)
clicks_B = np.random.binomial(n=1, p=0.108, size=n_samples)  # 10.8% CTR

df_A = pd.DataFrame({'video_edit': 'Edit_A', 'watch_time_sec': watch_time_A, 'clicked_cta': clicks_A})
df_B = pd.DataFrame({'video_edit': 'Edit_B', 'watch_time_sec': watch_time_B, 'clicked_cta': clicks_B})
df = pd.concat([df_A, df_B], ignore_index=True)

# Save the dataset to CSV
df.to_csv('campaign_ab_data.csv', index=False)
print("=== Dataset saved as 'campaign_ab_data.csv' ===")

# 2. Metric 1: Watch Time Analysis (Two-Sample T-Test)
mean_wt_a = df[df['video_edit'] == 'Edit_A']['watch_time_sec'].mean()
mean_wt_b = df[df['video_edit'] == 'Edit_B']['watch_time_sec'].mean()

t_stat, p_val_watch = stats.ttest_ind(
    df[df['video_edit'] == 'Edit_A']['watch_time_sec'],
    df[df['video_edit'] == 'Edit_B']['watch_time_sec']
)

print("\n--- METRIC 1: WATCH TIME (CONTINUOUS) ---")
print(f"Edit A Mean Watch Time: {mean_wt_a:.2f} s")
print(f"Edit B Mean Watch Time: {mean_wt_b:.2f} s")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_val_watch:.4e}")
if p_val_watch < 0.05:
    print("Conclusion: Statistically Significant (p < 0.05). Edit B drove significantly longer retention.")
else:
    print("Conclusion: Not statistically significant.")

# 3. Metric 2: Click-Through Rate (CTR) (Chi-Square Contingency Test)
contingency = pd.crosstab(df['video_edit'], df['clicked_cta'])
chi2_stat, p_val_ctr, dof, _ = stats.chi2_contingency(contingency)

ctr_a = df[df['video_edit'] == 'Edit_A']['clicked_cta'].mean() * 100
ctr_b = df[df['video_edit'] == 'Edit_B']['clicked_cta'].mean() * 100

print("\n--- METRIC 2: CLICK-THROUGH RATE (CATEGORICAL) ---")
print(f"Edit A CTR: {ctr_a:.2f}%")
print(f"Edit B CTR: {ctr_b:.2f}%")
print(f"Chi-Square Stat: {chi2_stat:.4f}")
print(f"P-Value: {p_val_ctr:.4e}")
if p_val_ctr < 0.05:
    print("Conclusion: Statistically Significant (p < 0.05). Edit B drove higher conversion to CTA.")
else:
    print("Conclusion: Not statistically significant.")

# 4. Generate & Save Comparison Visualizations
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.set_theme(style="whitegrid")

# Plot 1: Watch Time Distribution
sns.boxplot(ax=axes[0], data=df, x='video_edit', y='watch_time_sec', palette=['#4A90E2', '#50E3C2'])
axes[0].set_title(f'Watch Time Comparison (p = {p_val_watch:.2e})', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Watch Time (seconds)')
axes[0].set_xlabel('Video Cut')

# Plot 2: CTR Comparison
ctr_df = pd.DataFrame({'Video Edit': ['Edit A', 'Edit B'], 'CTR (%)': [ctr_a, ctr_b]})
sns.barplot(ax=axes[1], data=ctr_df, x='Video Edit', y='CTR (%)', palette=['#4A90E2', '#50E3C2'])
axes[1].set_title(f'Click-Through Rate (p = {p_val_ctr:.4f})', fontsize=12, fontweight='bold')
axes[1].set_ylim(0, max(ctr_a, ctr_b) + 3)
for p in axes[1].patches:
    axes[1].annotate(f'{p.get_height():.2f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 8), textcoords='offset points', fontweight='bold')

plt.tight_layout()
plt.savefig('ab_testing_results.png', dpi=300)
print("\n=== Visualization saved as 'ab_testing_results.png' ===")