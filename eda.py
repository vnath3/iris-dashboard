import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("iris.csv")

# Step 1: Check basic info and structure
print("Dataframe Info:")
print(df.info())

# Basic statistics
print("\nData Summary:")
print(df.describe())

# Count of each species
species_count = df['species'].value_counts()
print("\nSpecies count:")
print(species_count)

# Plot a simple bar chart of species count
species_count.plot(kind='bar')
plt.title("Count of Iris species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
