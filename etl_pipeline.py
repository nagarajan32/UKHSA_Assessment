import pandas as pd

"""Extract data from the CSV file."""

try:
    data = pd.read_csv("healthcare_dataset.csv")
    print(data)
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    

