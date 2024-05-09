import pandas as pd

csv_file_path = 'DATA SET.csv'
df_csv = pd.read_csv(csv_file_path)

json_file_path = 'ds.json'
df_json = pd.read_json(json_file_path)

print("CSV Data:")
print(df_csv.head())
print("\nJSON Data:")
print(df_json.head())

df_csv_cleaned = df_csv.dropna()
df_json_filled = df_json.fillna(0)

median_value = df_csv['Sales'].median()
upper_threshold = df_csv['Sales'].mean() + 2 * df_csv['Sales'].std()
lower_threshold = df_csv['Sales'].mean() - 2 * df_csv['Sales'].std()
df_csv['Sales'] = df_csv['Sales'].apply(lambda x: median_value if x > upper_threshold or x < lower_threshold else x)

filtered_data = df_csv[df_csv['Sales'] > 1000]
sorted_data = df_csv.sort_values(by='Sales', ascending=False)

numeric_columns = ['Sales', 'Cost', 'Profit']
grouped_data = df_csv.groupby('Category')[numeric_columns].mean()

print("\nCleaned CSV Data:")
print(df_csv_cleaned.head())
print("\nFilled JSON Data:")
print(df_json_filled.head())
print("\nFiltered Data:")
print(filtered_data.head())
print("\nSorted Data:")
print(sorted_data.head())
print("\nGrouped Data:")
print(grouped_data.head())
