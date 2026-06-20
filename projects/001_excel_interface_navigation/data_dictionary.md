# Data Dictionary — Retail Operations Navigation Dataset

## stores.csv

| Column | Type | Description |
|---|---|---|
| store_id | string | Unique store identifier |
| store_name | string | Store display name |
| city | string | Store city |
| region | string | Business region |
| manager | string | Store manager name |
| store_format | string | Store type/format |

## products.csv

| Column | Type | Description |
|---|---|---|
| product_id | string | Unique product identifier |
| category | string | Product category |
| product_name | string | Product display name |
| unit_price | decimal | Product selling price |
| target_margin_pct | integer | Target margin percentage |

## sales_orders.csv

| Column | Type | Description |
|---|---|---|
| order_id | string | Unique order ID |
| order_date | date | Date of transaction |
| store_id | string | Store where order happened |
| product_id | string | Product sold |
| quantity | integer | Units sold |
| unit_price | decimal | Price per unit |
| discount_pct | integer | Discount applied |
| gross_sales | decimal | Quantity × unit price |
| net_sales | decimal | Sales after discount |
| payment_mode | string | UPI/Card/Cash/Wallet |
| order_status | string | Completed/Returned/Cancelled |

## inventory_audit.csv

| Column | Type | Description |
|---|---|---|
| audit_id | string | Unique audit record |
| audit_date | date | Stock audit date |
| store_id | string | Store being audited |
| product_id | string | Product being audited |
| system_stock | integer | Stock in system |
| physical_stock | integer | Physical stock count |
| status | string | Audit status |
| stock_variance | integer | physical_stock - system_stock |
