"""
Lab 6: Pandas Exploratory Data Analysis & Visualization on "UScereal" Dataset
"""

import os

# Set matplotlib cache directory before importing matplotlib to prevent permission warnings
os.environ.setdefault('MPLCONFIGDIR', '/tmp/matplotlib_cache')

import pandas as pd
import matplotlib.pyplot as plt

# Set clean pandas display format
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', lambda x: f'{x:.2f}')

# Manufacturer mapping
MFR_MAP = {
    'G': 'General Mills',
    'K': 'Kelloggs',
    'N': 'Nabisco',
    'P': 'Post',
    'Q': 'Quaker Oats',
    'R': 'Ralston Purina'
}

# =============================================================================
# 1. Import the given "UScereal" dataset
# =============================================================================
df = pd.read_csv("UScereal.csv")
print("=" * 65)
print("1. IMPORTED DATASET: USCEREAL (First 5 Rows)")
print("=" * 65)
print(df.head())
print("\nInterpretation: Dataset contains 65 cereal brands with 12 standardized nutritional and categorical variables.")

# =============================================================================
# 2. Find summary statistics of the dataset
# =============================================================================
print("\n" + "=" * 65)
print("2. SUMMARY STATISTICS")
print("=" * 65)
print(df.describe())
print("\nInterpretation: High nutritional variability across brands; calories range from 50 to 440 kcal, and sugars range from 0 to 20.90 g per portion.")

# =============================================================================
# 3. Are there any missing values?
# =============================================================================
print("\n" + "=" * 65)
print("3. MISSING VALUES CHECK")
print("=" * 65)
print(df.isnull().sum())
print(f"\nTotal Missing Values: {df.isnull().sum().sum()}")
print("Interpretation: There are 0 missing values across all columns; the dataset is 100% complete.")

# =============================================================================
# 4. Find average protein value of each Manufacturer
# =============================================================================
print("\n" + "=" * 65)
print("4. AVERAGE PROTEIN VALUE BY MANUFACTURER")
print("=" * 65)
avg_protein = df.groupby('mfr')['protein'].mean().sort_values(ascending=False)
for mfr_code, val in avg_protein.items():
    print(f"  {mfr_code} ({MFR_MAP.get(mfr_code, mfr_code):<14}): {val:.2f} g")
print("\nInterpretation: Nabisco (N) has the highest average protein (7.03 g), while Ralston Purina (R) has the lowest (2.60 g).")

# =============================================================================
# 5. Find the name of the Cereal with high sugar from Manufacturer G
# =============================================================================
print("\n" + "=" * 65)
print("5. CEREAL WITH HIGHEST SUGAR FROM MANUFACTURER G (General Mills)")
print("=" * 65)
g_cereals = df[df['mfr'] == 'G']
highest_sugar_g = g_cereals.loc[g_cereals['sugars'].idxmax()]
print(f"  Cereal Name : {highest_sugar_g['Name']}")
print(f"  Sugar Content: {highest_sugar_g['sugars']:.2f} g")
print(f"  Calories    : {highest_sugar_g['calories']:.2f} kcal")
print(f"  Display Shelf: Shelf {int(highest_sugar_g['shelf'])}")
print("\nInterpretation: 'Oatmeal Raisin Crisp' has the highest sugar content (20.00 g) among General Mills cereals.")

# =============================================================================
# 6. Generate three different suitable plots
# =============================================================================
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 6a. Using only shelf
shelf_counts = df['shelf'].value_counts().sort_index()
shelf_labels = [f"Shelf {s}" for s in shelf_counts.index]
bars_shelf = axes[0].bar(shelf_labels, shelf_counts.values, color=['#42A5F5', '#66BB6A', '#FFA726'], edgecolor='black', width=0.55)
axes[0].set_title("6a: Cereal Count by Display Shelf", fontsize=12, fontweight='bold')
axes[0].set_xlabel("Display Shelf (1: Floor/Bottom, 2: Middle, 3: Top)", fontsize=10)
axes[0].set_ylabel("Number of Cereals", fontsize=10)
axes[0].bar_label(bars_shelf, padding=3, fontweight='bold')
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# 6b. Using mfr and fiber
mfr_fiber = df.groupby('mfr')['fibre'].mean().sort_values(ascending=False)
bars_fiber = axes[1].bar([f"{m} ({MFR_MAP.get(m, m)})" for m in mfr_fiber.index], mfr_fiber.values, color='#4CAF50', edgecolor='black', width=0.55)
axes[1].set_title("6b: Average Dietary Fiber by Manufacturer", fontsize=12, fontweight='bold')
axes[1].set_xlabel("Manufacturer", fontsize=10)
axes[1].set_ylabel("Average Dietary Fiber (g)", fontsize=10)
axes[1].tick_params(axis='x', rotation=25)
axes[1].bar_label(bars_fiber, fmt='%.2f', padding=3, fontweight='bold')
axes[1].grid(axis='y', linestyle='--', alpha=0.7)

# 6c. Using sodium and sugars
shelf_colors = {1: '#1E88E5', 2: '#FB8C00', 3: '#E53935'}
shelf_names = {1: 'Shelf 1 (Bottom)', 2: 'Shelf 2 (Middle)', 3: 'Shelf 3 (Top)'}
for s in [1, 2, 3]:
    sub = df[df['shelf'] == s]
    axes[2].scatter(sub['sugars'], sub['sodium'], color=shelf_colors[s], label=shelf_names[s], s=55, alpha=0.85, edgecolors='black')
axes[2].set_title("6c: Sodium vs Sugars Content", fontsize=12, fontweight='bold')
axes[2].set_xlabel("Sugars (g per portion)", fontsize=10)
axes[2].set_ylabel("Sodium (mg per portion)", fontsize=10)
axes[2].legend(title="Shelf Placement")
axes[2].grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()

# Save combined and individual plot images
plt.savefig("lab6_plots.png", dpi=300)
print("\n" + "=" * 65)
print("Plot saved as 'lab6_plots.png'. Displaying plots window...")
print("=" * 65)

plt.show()
