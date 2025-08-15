import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('artifacts/data_ingestion/winequality-red.csv')

print('=== DATASET OVERVIEW ===')
print(f'Shape: {df.shape}')
print(f'Columns: {list(df.columns)}')
print()

print('=== DATA TYPES ===')
print(df.dtypes)
print()

print('=== MISSING VALUES ===')
missing_values = df.isnull().sum()
print(missing_values)
print(f'Total missing values: {missing_values.sum()}')
print()

print('=== TARGET DISTRIBUTION ===')
target_dist = df['quality'].value_counts().sort_index()
print(target_dist)
print(f'Target range: {df["quality"].min()} - {df["quality"].max()}')
print()

print('=== DUPLICATED ROWS ===')
duplicates = df.duplicated().sum()
print(f'Duplicated rows: {duplicates}')
print()

print('=== BASIC STATISTICS ===')
print(df.describe().round(3))
print()

print('=== CORRELATION WITH TARGET ===')
correlations = df.corr()['quality'].sort_values(ascending=False)
print(correlations.round(3))
print()

print('=== OUTLIERS CHECK (using IQR) ===')
numeric_cols = df.select_dtypes(include=[np.number]).columns
outlier_summary = {}
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    outlier_count = len(outliers)
    outlier_pct = (outlier_count/len(df)*100)
    outlier_summary[col] = outlier_count
    print(f'{col}: {outlier_count} outliers ({outlier_pct:.2f}%)')

print()
print('=== SKEWNESS ===')
skewness_summary = {}
for col in numeric_cols:
    skewness = df[col].skew()
    skewness_summary[col] = skewness
    # status = 'Highly Skewed' if abs(skewness) > 1 else 'Moderately Skewed' if abs(skewness) > 0.5 else 'Normal'
    # print(f'{col}: {skewness:.3f} ({status})')
    print(f'{col}: {skewness:.3f}')

print()
print('=== DATA QUALITY SUMMARY ===')
print(f'- Dataset has {df.shape[0]} rows and {df.shape[1]} columns')
print(f'- No missing values found')
print(f'- {duplicates} duplicate rows')
print(f'- Target variable (quality) ranges from {df["quality"].min()} to {df["quality"].max()}')
print(f'- Most common quality scores: {target_dist.index[0]} ({target_dist.iloc[0]} wines)')

print()
print('=== PREPROCESSING RECOMMENDATIONS ===')
high_skew_cols = [col for col, skew in skewness_summary.items() if abs(skew) > 1]
high_outlier_cols = [col for col, count in outlier_summary.items() if count > 50]

if high_skew_cols:
    print(f'- Apply log transformation or scaling to highly skewed features: {high_skew_cols}')
if high_outlier_cols:
    print(f'- Consider outlier treatment for: {high_outlier_cols}')
print('- Apply feature scaling (StandardScaler or MinMaxScaler)')
print('- Consider feature engineering based on domain knowledge')
print('- Target is imbalanced - consider stratified sampling')
