import pandas as pd

# Load the dataset
df = pd.read_csv('../iris/iris.csv')

# Print first 5 rows to confirm
print(df.head(2))

print(df.columns)
