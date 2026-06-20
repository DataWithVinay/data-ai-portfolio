# DataWithVinay — Day 01 Dataset Generator
# Topic: Excel Interface, Navigation & Workbook Structure
# Purpose: Generate synthetic retail CSV datasets and save them to Google Drive.

from google.colab import drive
drive.mount('/content/drive')

from pathlib import Path
import pandas as pd
import numpy as np
import random

# 1. Set output folder inside Google Drive.
BASE_DIR = Path("/content/drive/MyDrive/DataWithVinay_Content_Factory/07_Datasets/day01_excel_interface_navigation")
BASE_DIR.mkdir(parents=True, exist_ok=True)

# 2. Set seeds so the generated data is reproducible.
random.seed(42)
np.random.seed(42)

# 3. Create store lookup data.
stores = pd.DataFrame({
    "store_id": [f"STR{i:03d}" for i in range(1, 11)],
    "store_name": [f"Metro Retail Store {i}" for i in range(1, 11)],
    "city": np.random.choice(["Hyderabad", "Bengaluru", "Chennai", "Mumbai", "Pune"], 10),
    "region": np.random.choice(["South", "West"], 10),
    "manager": [f"Manager_{i}" for i in range(1, 11)],
    "store_format": np.random.choice(["Mall", "High Street", "Express", "Superstore"], 10),
})

# 4. Create product lookup data.
products = pd.DataFrame({
    "product_id": [f"PRD{i:04d}" for i in range(1, 31)],
    "category": np.random.choice(["Grocery", "Electronics", "Fashion", "Home", "Beauty"], 30),
    "product_name": [f"Product {i}" for i in range(1, 31)],
    "unit_price": np.round(np.random.uniform(49, 4999, 30), 2),
    "target_margin_pct": np.random.choice([12, 18, 22, 28, 35], 30),
})

# 5. Create sales transactions.
sales = []
for i in range(1, 301):
    store = stores.sample(1).iloc[0]
    product = products.sample(1).iloc[0]
    quantity = np.random.randint(1, 8)
    discount_pct = np.random.choice([0, 5, 10, 15, 20], p=[0.45, 0.20, 0.18, 0.12, 0.05])
    unit_price = float(product["unit_price"])

    sales.append({
        "order_id": f"ORD{i:05d}",
        "order_date": pd.Timestamp("2026-05-01") + pd.Timedelta(days=int(np.random.randint(0, 31))),
        "store_id": store["store_id"],
        "product_id": product["product_id"],
        "quantity": quantity,
        "unit_price": round(unit_price, 2),
        "discount_pct": int(discount_pct),
        "gross_sales": round(quantity * unit_price, 2),
        "net_sales": round(quantity * unit_price * (1 - discount_pct / 100), 2),
        "payment_mode": np.random.choice(["UPI", "Card", "Cash", "Wallet"]),
        "order_status": np.random.choice(["Completed", "Returned", "Cancelled"], p=[0.86, 0.09, 0.05]),
    })

sales_orders = pd.DataFrame(sales)

# 6. Create inventory audit records.
inventory = []
for _, row in products.iterrows():
    sampled_stores = stores["store_id"].sample(3, random_state=int(row["product_id"][3:])).tolist()
    for store_id in sampled_stores:
        system_stock = np.random.randint(5, 120)
        physical_stock = np.random.randint(5, 120)
        inventory.append({
            "audit_id": f"AUD{len(inventory)+1:05d}",
            "audit_date": pd.Timestamp("2026-06-01"),
            "store_id": store_id,
            "product_id": row["product_id"],
            "system_stock": system_stock,
            "physical_stock": physical_stock,
            "status": np.random.choice(["Pending Review", "Validated", "Mismatch"], p=[0.25, 0.55, 0.20]),
            "stock_variance": physical_stock - system_stock,
        })

inventory_audit = pd.DataFrame(inventory)

# 7. Save CSV files to Drive.
stores.to_csv(BASE_DIR / "stores.csv", index=False)
products.to_csv(BASE_DIR / "products.csv", index=False)
sales_orders.to_csv(BASE_DIR / "sales_orders.csv", index=False)
inventory_audit.to_csv(BASE_DIR / "inventory_audit.csv", index=False)

# 8. Optional: Save a single Excel workbook with multiple sheets.
excel_path = BASE_DIR / "retail_operations_navigation_lab.xlsx"
with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
    stores.to_excel(writer, sheet_name="Stores", index=False)
    products.to_excel(writer, sheet_name="Products", index=False)
    sales_orders.to_excel(writer, sheet_name="Sales_Orders", index=False)
    inventory_audit.to_excel(writer, sheet_name="Inventory_Audit", index=False)

# 9. Create a data dictionary markdown file.
data_dictionary = """# Data Dictionary

This synthetic dataset is created for Excel navigation and workbook-structure practice.

Files:
- stores.csv
- products.csv
- sales_orders.csv
- inventory_audit.csv
- retail_operations_navigation_lab.xlsx
"""

(BASE_DIR / "data_dictionary.md").write_text(data_dictionary, encoding="utf-8")

# 10. Print output location and previews.
print(f"Files saved to: {BASE_DIR}")
print("\nStores preview:")
display(stores.head())

print("\nSales orders preview:")
display(sales_orders.head())

print("\nInventory audit preview:")
display(inventory_audit.head())
