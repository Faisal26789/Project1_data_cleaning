"""
Project 1: Data Cleaning & Preparation
----------------------------------------
Goal: Clean a raw e-commerce "Online Store Orders" dataset by handling
missing values, duplicates, and incorrect/inconsistent data.

Author: [Your Name]
Dataset: Online-Store-Orders.xlsx
"""

import pandas as pd

# -------------------------------------------------------------------
# STEP 1: Load the raw data
# -------------------------------------------------------------------
RAW_FILE = "Online-Store-Orders.xlsx"
df = pd.read_excel(RAW_FILE)

print("STEP 1: Data loaded")
print(f"  Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print()

# Keep a copy of the original row count so we can report what changed
original_rows = len(df)

# -------------------------------------------------------------------
# STEP 2: Explore the data (first look for problems)
# -------------------------------------------------------------------
print("STEP 2: Initial data check")
print(df.info())
print()
missing_before = df.isnull().sum()
print("Missing values per column (before cleaning):")
print(missing_before[missing_before > 0])
print()

# -------------------------------------------------------------------
# STEP 3: Handle missing values
# -------------------------------------------------------------------
# CouponCode is blank whenever a customer did NOT use a coupon.
# A blank here is not "bad data" - it is a real business state, so
# instead of deleting these rows we clearly label them.
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

print("STEP 3: Missing values handled")
print("  - Filled empty CouponCode cells with 'No Coupon'")
print(f"  - Remaining missing values: {df.isnull().sum().sum()}")
print()

# -------------------------------------------------------------------
# STEP 4: Remove duplicate records
# -------------------------------------------------------------------
# Check for fully duplicated rows AND duplicate OrderIDs
# (an OrderID should always be unique - it identifies one order).
full_duplicates = df.duplicated().sum()
duplicate_ids = df.duplicated(subset=["OrderID"]).sum()

df = df.drop_duplicates()
df = df.drop_duplicates(subset=["OrderID"], keep="first")

print("STEP 4: Duplicate check")
print(f"  - Fully duplicated rows found & removed: {full_duplicates}")
print(f"  - Duplicate OrderIDs found & removed: {duplicate_ids}")
print(f"  - Rows remaining: {len(df)}")
print()

# -------------------------------------------------------------------
# STEP 5: Fix data formats and types
# -------------------------------------------------------------------
# Make sure Date is a proper date type (not text) and standardize
# text columns (remove stray spaces, keep consistent capitalization).
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

text_cols = ["Product", "PaymentMethod", "OrderStatus",
             "ReferralSource", "CouponCode", "ShippingAddress"]
for col in text_cols:
    df[col] = df[col].astype(str).str.strip()

# Numbers should be whole numbers where they represent counts
df["Quantity"] = df["Quantity"].astype(int)
df["ItemsInCart"] = df["ItemsInCart"].astype(int)

print("STEP 5: Data formats standardized")
print("  - Date column converted to proper datetime format")
print("  - Text columns stripped of extra spaces")
print("  - Quantity / ItemsInCart confirmed as whole numbers")
print()

# -------------------------------------------------------------------
# STEP 6: Validate the numbers make sense (logic check)
# -------------------------------------------------------------------
# TotalPrice should always equal Quantity x UnitPrice.
# Flag any row where that is not true (incorrect data).
expected_total = (df["Quantity"] * df["UnitPrice"]).round(2)
mismatch = (expected_total - df["TotalPrice"]).abs() > 0.01
num_mismatches = mismatch.sum()

if num_mismatches > 0:
    df.loc[mismatch, "TotalPrice"] = expected_total[mismatch]

invalid_qty = (df["Quantity"] <= 0).sum()
invalid_price = (df["UnitPrice"] <= 0).sum()

print("STEP 6: Data validation")
print(f"  - TotalPrice mismatches found & corrected: {num_mismatches}")
print(f"  - Invalid (zero/negative) Quantity rows: {invalid_qty}")
print(f"  - Invalid (zero/negative) UnitPrice rows: {invalid_price}")
print()

# -------------------------------------------------------------------
# STEP 7: Save the cleaned dataset
# -------------------------------------------------------------------
CLEAN_FILE = "Online-Store-Orders-Cleaned.xlsx"
df.to_excel(CLEAN_FILE, index=False)

print("STEP 7: Cleaned file saved")
print(f"  - Saved as: {CLEAN_FILE}")
print()

# -------------------------------------------------------------------
# Summary
# -------------------------------------------------------------------
print("=" * 50)
print("CLEANING SUMMARY")
print("=" * 50)
print(f"Original rows:      {original_rows}")
print(f"Final rows:         {len(df)}")
print(f"Missing values fixed: {missing_before.sum()}")
print(f"Duplicates removed:   {full_duplicates + duplicate_ids}")
print(f"TotalPrice corrections: {num_mismatches}")
