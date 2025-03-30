# Module 1: Exploratory Analysis of USA House Prices

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("redfin_housing.csv")
print(df.info())
print(df.describe())

df.columns = df.columns.str.lower()

# Checks for missing values, removes missing values, verifies that missing values were dropped
print(df.isnull().sum())
df = df.dropna()
print(df.isnull().sum())

# Removing outliers using IQR method
Q1 = df["price (usd)"].quantile(0.25)
Q3 = df["price (usd)"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df_cleaned = df[(df["price (usd)"] >= lower_bound) & (df["price (usd)"] <= upper_bound)]

# Relevant columns converted to numeric types
df["price (usd)"] = pd.to_numeric(df["price (usd)"], errors="coerce")
df["beds"] = pd.to_numeric(df["beds"], errors="coerce")
df["baths"] = pd.to_numeric(df["baths"], errors="coerce")
df["area (sqft)"] = pd.to_numeric(df["area (sqft)"], errors="coerce")

# Bar plot: Avg price of house in each city
avg_price_by_city = df.groupby("city")["price (usd)"].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 7))
sns.barplot(x=avg_price_by_city.index, y=avg_price_by_city.values, color="#1B2452")
plt.xticks(rotation=45, ha="right")
plt.xlabel("City")
plt.ylabel("Average Price (USD)")
plt.title("Average House Price by City in the U.S.")
plt.show()

# Scatter plot: Price vs. Sq Ft
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["area (sqft)"], y=df["price (usd)"], alpha=0.5)
plt.title("House Price vs. Square Footage")
plt.xlabel("Square Footage")
plt.ylabel("Price (USD)")
plt.show()

# Relationship between number of bedrooms and price
bedroom_price_avg = df.groupby("beds")["price (usd)"].mean().reset_index()
plt.figure(figsize=(8, 4))
sns.barplot(x=bedroom_price_avg["beds"], y=bedroom_price_avg["price (usd)"], palette="coolwarm")
plt.title("Average House Price by Number of Bedrooms")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Average Price (USD)")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Relationship between number of bathrooms and price
bathroom_price_avg = df.groupby("baths")["price (usd)"].mean().reset_index()
plt.figure(figsize=(8, 4))
sns.barplot(x=bathroom_price_avg["baths"], y=bathroom_price_avg["price (usd)"], palette="coolwarm")
plt.title("Average House Price by Number of Bathrooms")
plt.xlabel("Number of Bathrooms")
plt.ylabel("Average Price (USD)")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
