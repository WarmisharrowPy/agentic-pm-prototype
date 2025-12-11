import pandas as pd
df = pd.read_csv('data/telemetry_sample.csv')
print(df.head())
print("\nSummary:\n", df.describe(include='all'))
