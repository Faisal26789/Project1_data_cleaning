# Project 1: Data Cleaning & Preparation 🧹

## Overview
This project cleans a raw **Online Store Orders** dataset (1,200 e-commerce orders) by identifying and fixing missing values, duplicate records, and inconsistent data formats — turning a messy raw export into an analysis-ready dataset.

## Goal
Clean a raw dataset by handling missing values, duplicates, and incorrect data, following standard data cleaning practices used in real analytics workflows.

## Dataset
`Online-Store-Orders.xlsx` — 1,200 rows × 14 columns, including order details, customer ID, product, pricing, payment method, order status, and referral source.

## Tools Used
- Python 3
- pandas
- openpyxl

## Steps Performed

| Step | Action | Result |
|------|--------|--------|
| 1 | Loaded raw data and reviewed structure (`.info()`, `.isnull()`) | 1,200 rows, 14 columns confirmed |
| 2 | Identified missing values | 309 blank cells in `CouponCode` |
| 3 | Handled missing values | Filled blanks with `"No Coupon"` (a blank here means no coupon was used — a real business case, not an error) |
| 4 | Checked for duplicate rows and duplicate Order IDs | 0 found — dataset had no duplicate orders |
| 5 | Standardized formats | Converted `Date` to proper datetime type; trimmed extra spaces from text columns; confirmed `Quantity`/`ItemsInCart` are whole numbers |
| 6 | Validated calculated fields | Checked that `TotalPrice = Quantity × UnitPrice` for every row — 0 mismatches found |
| 7 | Exported cleaned file | Saved as `Online-Store-Orders-Cleaned.xlsx` |

## Before vs. After

| Metric | Before | After |
|---|---|---|
| Total rows | 1,200 | 1,200 |
| Missing values | 309 | 0 |
| Duplicate rows | 0 | 0 |
| Invalid pricing rows | 0 | 0 |

## Key Findings
- The only data quality issue in this dataset was missing `CouponCode` values (~26% of rows), which represent customers who did not use a coupon rather than a data error.
- No duplicate orders, no formatting errors in dates or text fields, and all pricing calculations were internally consistent.
- This shows that even a "clean-looking" dataset should always be verified with explicit checks rather than assumed to be correct.

## Files in this Repository
- `Online-Store-Orders.xlsx` — original raw dataset
- `clean_data.py` — Python script that performs the cleaning
- `Online-Store-Orders-Cleaned.xlsx` — final cleaned dataset
- `README.md` — this report

## How to Run
```bash
pip install pandas openpyxl
python clean_data.py
```

## Author
Md. Faisal Siddiqui— Data Analytics Intern Project 1
