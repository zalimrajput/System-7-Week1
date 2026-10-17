# Pandas: Series, DataFrames, filtering, sorting, missing values


# 1. Series

import pandas as pd

print("Pandas Series Example:")
marks = pd.Series([85, 90, 75, 60])
print(marks)

# Creating a Series with a custom index
print("\nPandas Series with Custom Index:")
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)


# DataFrames
print("\nPandas DataFrame Example:")

import pandas as pd

data = {
    "Name": ["Ali", "Ahmed", "Sara"],
    "Age": [22, 21, 23],
    "Marks": [85, 72, 95]
}

df = pd.DataFrame(data)
print(df)


# Useful DataFrame Commands
print("\nDataFrame Info:")
print(df.head())       # First 5 rows
print(df.tail())       # Last 5 rows
print(df.shape)        # Number of rows and columns
print(df.columns)      # Column names
print(df.info())       # Data types and non-null counts
print(df.describe())   # Statistical summary



# 2. Filtering and Sorting
print("\nFiltering and Sorting Example:")

# Filtering
print("Filtering rows where Marks > 80:")
import pandas as pd

data = {
    "Name": ["Ali", "Ahmed", "Sara", "Zara"],
    "Age": [22, 21, 23, 20],
    "Marks": [85, 72, 95, 55]
}

df = pd.DataFrame(data)
print(df[df["Marks"] > 80])




print("\nFiltering rows where Marks > 80 and Age > 21:")
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Zara"],
    "Age": [22, 21, 23, 20],
    "Marks": [85, 72, 95, 55]
}

df = pd.DataFrame(data)
print(df[(df["Marks"] > 80) & (df["Age"] > 21)])


# Sorting
print("\nSorting by Marks in Ascending order:")
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Zara"],
    "Age": [22, 21, 23, 20],
    "Marks": [85, 72, 95, 55]
}

df = pd.DataFrame(data)
print(df.sort_values(by="Marks"))


# 3. Missing Values

print("Missing Values")
import pandas as pd
import numpy as np

data = {
    "Name": ["Ali", "Ahmed", "Sara", "Zara"],
    "Age": [22, np.nan, 23, 20],
    "Marks": [85, 72, np.nan, 55]
}

df = pd.DataFrame(data)

print(df)


# find missing values

print(df.isnull())
print(df.isnull().sum())

# Cleans & remove missing values

clean_df = df.dropna()
print(clean_df)

# Fill missing values

df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Marks"] = df["Marks"].fillna(0)


