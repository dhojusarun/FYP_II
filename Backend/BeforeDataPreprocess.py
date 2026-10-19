# ==========================================
# FAKE SMS DETECTION - BEFORE PREPROCESSING
# ==========================================

# Import pandas for handling the dataset
import pandas as pd

# Load the CSV dataset
# df = pd.read_csv("fake_sms_100k.csv", encoding="latin-1")
# Provide the complete disk path to the file
df = pd.read_csv("../fake_sms_100k.csv", encoding="latin-1")


# Display the first 5 records
print("First 5 records:")
print(df.head())

# Display the number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Display all column names
print("\nColumn Names:")
print(df.columns.tolist())

# Display information about the dataset
print("\nDataset Information:")
print(df.info())

# Check the data types of each column
print("\nData Types:")
print(df.dtypes)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check the number of duplicate records
print("\nNumber of Duplicate Records:")
print(df.duplicated().sum())

# Display the number of legitimate and spam SMS
print("\nSMS Label Distribution:")
print(df["label"].value_counts())

# Display the binary label distribution
print("\nBinary Label Distribution:")
print(df["binary_label"].value_counts())

# Display some sample SMS messages
print("\nSample Messages:")
print(df[["message", "label", "binary_label"]].head(10))