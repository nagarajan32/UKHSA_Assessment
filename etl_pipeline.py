import pandas as pd

"""Extract data from the CSV file."""

try:
    data = pd.read_csv("healthcare_dataset.csv")
    data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')
    print(data.dtypes)
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    

"""Transform the data to fit the star schema."""
try:
        # Remove titles and commas, and correct name case
        data['name'] = data['name'].str.title().str.replace(r'^[Mr\.|Mrs\.|Ms\.|Dr\., ]+', '', regex=True)

        # Remove trailing commas from Hospital names
        data['hospital'] = data['hospital'].str.rstrip(',')

        # Convert dates
        data['date_of_admission'] = pd.to_datetime(data['date_of_admission'], format='%d-%m-%Y', errors='coerce')
        data['discharge_date'] = pd.to_datetime(data['discharge_date'], format='%d-%m-%Y', errors='coerce')

        # Fill missing billing amounts with 0
        data['billing_amount'].fillna(0)
        data['billing_amount'] = pd.to_numeric(data['billing_amount'], errors='coerce')
        print(data)
        print(data.dtypes)
        
except Exception as e:
        print(f"Error during data transformation: {e}")
        
