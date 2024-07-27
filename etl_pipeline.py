import pandas as pd

"""Extract data from the CSV file."""

try:
    data = pd.read_csv("healthcare_dataset.csv")
    print(data.dtypes)
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    

"""Transform the data to fit the star schema."""
try:
        # Remove titles and commas, and correct name case
        data['Name'] = data['Name'].str.title().str.replace(r'^[Mr\.|Mrs\.|Ms\.|Dr\., ]+', '', regex=True)

        # Remove trailing commas from Hospital names
        data['Hospital'] = data['Hospital'].str.rstrip(',')

        # Convert dates
        data['Date of Admission'] = pd.to_datetime(data['Date of Admission'], format='%d-%m-%Y', errors='coerce')
        data['Discharge Date'] = pd.to_datetime(data['Discharge Date'], format='%d-%m-%Y', errors='coerce')

        # Fill missing billing amounts with 0
        data['Billing Amount'].fillna(0)
        data['Billing Amount'] = pd.to_numeric(data['Billing Amount'], errors='coerce')
        print(data)
        print(data.dtypes)
        
except Exception as e:
        print(f"Error during data transformation: {e}")
        
