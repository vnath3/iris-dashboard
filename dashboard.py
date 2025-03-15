import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("iris.csv")

# Title of your dashboard
st.title("🌸 Iris Flower Dashboard")

# Display dataset
st.header("Dataset Overview")
st.write(df)

# Species selection box
species = st.selectbox("Choose Iris species:", df["species"].unique())

# Filter data based on selection
filtered_df = df[df["species"] == species]

# Display filtered data
st.subheader(f"Data for species: {species}")
st.write(species, "has", len(df[df["species"] == species]), "entries")

# Simple visualization
st.subheader("Distribution of Sepal Length")
st.bar_chart(df[df['species'] == species]['sepal_length'])


# Scatter plot: Sepal Length vs Sepal Width
st.subheader("Sepal Length vs Sepal Width")

fig, ax = plt.subplots()
ax.scatter(filtered_df['sepal_length'], filtered_df['sepal_width'], color='green')

ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')
ax.set_title(f"{species.capitalize()} Sepal Dimensions")

st.pyplot(fig)


# Histogram of Petal Length distribution
st.subheader("Petal Length Distribution (Histogram)")

fig, ax = plt.subplots()
ax.hist(df["petal_length"], bins=10, color="purple", alpha=0.7)
ax.set_xlabel("Petal Length")
ax.set_ylabel("Frequency")

st.pyplot(fig)

# Line chart visualization: Sepal Length across all samples
st.subheader("Line Chart - Sepal Length across samples")

fig, ax = plt.subplots()
ax.plot(df["sepal_length"], marker='o')
ax.set_xlabel("Sample Number")
ax.set_ylabel("Sepal Length")
ax.set_title("Sepal Length Variation")

st.pyplot(fig)

# Pie chart: Species distribution
st.subheader("Pie Chart - Iris Species Distribution")

species_count = df["species"].value_counts()

fig, ax = plt.subplots()
ax.pie(species_count, labels=species_count.index, autopct='%1.1f%%', startangle=90)
ax.axis("equal")  # Ensures pie chart is circular

st.pyplot(fig)
