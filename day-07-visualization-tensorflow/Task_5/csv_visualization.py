
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load CSV dataset
df = pd.read_csv("messy_ecommerce_sales_data.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# 2. Display basic information
print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn information:")
df.info()

# 3. Clean column names and categorical values
for column in ["Product", "Category", "Payment_Method", "Status"]:
    df[column] = df[column].astype("string").str.strip()

# Standardize category capitalization
df["Category"] = df["Category"].str.title()

# Convert numeric columns to numeric values
for column in ["Quantity", "Price", "Total"]:
    df[column] = pd.to_numeric(
        df[column].astype("string")
        .str.replace("$", "", regex=False)
        .str.strip(),
        errors="coerce"
    )

# Treat blank strings and text placeholders as missing
df = df.replace(r"^\s*$", pd.NA, regex=True)
df = df.replace(
    {column: {"nan": pd.NA, "NaN": pd.NA}
     for column in df.select_dtypes(include=["object", "string"]).columns}
)

# 4. Summary statistics
print("\nSummary Statistics:")
print(df.describe(include="all"))

# 5. Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 6. Duplicate records
print("\nDuplicate rows:", df.duplicated().sum())
print("Duplicate Order IDs:", df["Order_ID"].duplicated().sum())

# 7. Identify invalid values
print("\nInvalid quantities:")
print(df[df["Quantity"].notna() & (df["Quantity"] <= 0)])

print("\nInvalid prices:")
print(df[df["Price"].notna() & (df["Price"] < 0)])

# 8. Calculate totals for valid rows
# Do not overwrite the original Total column.
valid = (
    df["Quantity"].notna()
    & df["Price"].notna()
    & (df["Quantity"] > 0)
    & (df["Price"] >= 0)
)

df["Calculated_Total"] = pd.NA
df.loc[valid, "Calculated_Total"] = (
    df.loc[valid, "Quantity"] * df.loc[valid, "Price"]
)

print("\nTotal valid calculated sales:")
print(df.loc[valid, "Calculated_Total"].sum())

# 9. Orders by status
print("\nOrders by Status:")
print(df["Status"].value_counts())

# 10. Chart 1: Orders by status
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Status", order=df["Status"].value_counts().index)
plt.title("Number of Orders by Status")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("orders_by_status.png", dpi=150)
plt.show()

# 11. Chart 2: Average product price by category
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Category", y="Price", errorbar=None)
plt.title("Average Product Price by Category")
plt.xlabel("Category")
plt.ylabel("Average Price")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("average_price_by_category.png", dpi=150)
plt.show()

# 12. Chart 3: Missing values
missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)

if not missing.empty:
    plt.figure(figsize=(10, 5))
    sns.barplot(x=missing.index, y=missing.values)
    plt.title("Missing Values by Column")
    plt.xlabel("Column")
    plt.ylabel("Missing Value Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("missing_values.png", dpi=150)
    plt.show()
else:
    print("No missing values found.")

# 13. Chart 4: Correlation heatmap
numeric_data = df[
    ["ID", "Quantity", "Price", "Total", "Calculated_Total"]
].apply(pd.to_numeric, errors="coerce")

plt.figure(figsize=(8, 6))
sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Between Numeric Columns")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=150)
plt.show()

# 14. Save analysis-ready data
df.to_csv("ecommerce_analyzed.csv", index=False)

print("\nAnalysis completed.")
print("Analyzed data saved to ecommerce_analyzed.csv")
