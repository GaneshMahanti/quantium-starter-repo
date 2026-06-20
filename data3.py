import pandas as pd
from pathlib import Path

data_dir = Path("data")
files = [
    data_dir / "daily_sales_data_0.csv",
    data_dir / "daily_sales_data_1.csv",
    data_dir / "daily_sales_data_2.csv",
]

all_data = []

for file in files:
    df = pd.read_csv(file)

    # Clean text columns
    df["product"] = df["product"].astype(str).str.strip()
    df["region"] = df["region"].astype(str).str.strip()
    df["date"] = df["date"].astype(str).str.strip()

    # Keep only Pink Morsel rows
    df = df[df["product"].str.lower() == "pink morsel"]

    # Clean price column like "$2.50"
    df["price"] = df["price"].astype(str).str.replace("$", "", regex=False).str.strip()
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

    # Create sales column
    df["Sales"] = df["quantity"] * df["price"]

    # Keep only required columns
    df = df[["Sales", "date", "region"]]
    df.columns = ["Sales", "Date", "Region"]

    all_data.append(df)

result = pd.concat(all_data, ignore_index=True)

# Remove bad rows if any
result = result.dropna(subset=["Sales", "Date", "Region"])

# Save final output
result.to_csv("pink_morsel_sales.csv", index=False)

print(result.head())
print("Total rows:", len(result))
