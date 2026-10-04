import pandas as pd
import numpy as np

# Read dataset
file_name = "students.csv"

try:
    df = pd.read_csv(file_name)

    print("=" * 50)
    print("       DATA QUALITY REPORT")
    print("=" * 50)

    # Basic information
    print("\nTotal Rows:", len(df))
    print("Total Columns:", len(df.columns))

    # -------------------------------
    # 1. Missing Values
    # -------------------------------
    print("\n--- Missing Values ---")

    missing = df.isnull().sum()

    for column in df.columns:
        print(column, ":", missing[column])

    # Completeness
    total_cells = df.shape[0] * df.shape[1]
    missing_cells = df.isnull().sum().sum()

    completeness = ((total_cells - missing_cells) / total_cells) * 100

    print("\nCompleteness:", round(completeness, 2), "%")

    # -------------------------------
    # 2. Duplicate Records
    # -------------------------------
    print("\n--- Duplicate Records ---")

    duplicate_count = df.duplicated().sum()

    print("Duplicate Records:", duplicate_count)

    if duplicate_count > 0:
        print("\nDuplicate Data:")
        print(df[df.duplicated()])

    # -------------------------------
    # 3. Unique Values
    # -------------------------------
    print("\n--- Uniqueness ---")

    for column in df.columns:
        unique_count = df[column].nunique()
        print(column, ":", unique_count, "unique values")

    # -------------------------------
    # 4. Invalid / Suspicious Records
    # -------------------------------
    print("\n--- Suspicious Records ---")

    suspicious = pd.DataFrame()

    # Check negative values in numeric columns
    numeric_columns = df.select_dtypes(include=np.number).columns

    for column in numeric_columns:
        invalid = df[df[column] < 0]

        if not invalid.empty:
            suspicious = pd.concat([suspicious, invalid])

    if suspicious.empty:
        print("No suspicious records found.")
    else:
        suspicious = suspicious.drop_duplicates()
        print(suspicious)

        # Save invalid records
        suspicious.to_csv("invalid_records.csv", index=False)
        print("\nInvalid records saved to invalid_records.csv")

    # -------------------------------
    # 5. Data Types
    # -------------------------------
    print("\n--- Data Types ---")

    print(df.dtypes)

    # -------------------------------
    # 6. Summary Statistics
    # -------------------------------
    print("\n--- Summary Statistics ---")

    print(df.describe())

    # -------------------------------
    # Final Report
    # -------------------------------
    print("\n" + "=" * 50)
    print("QUALITY SUMMARY")
    print("=" * 50)

    print("Total Records :", len(df))
    print("Missing Cells :", missing_cells)
    print("Duplicates    :", duplicate_count)
    print("Completeness  :", round(completeness, 2), "%")

    if suspicious.empty:
        print("Invalid Data  : No")
    else:
        print("Invalid Data  : Yes")

    print("\nData quality report completed successfully!")

except FileNotFoundError:
    print("Error: students.csv file not found.")
    print("Please keep students.csv in the same folder as this program.")

except Exception as e:
    print("Error:", e)