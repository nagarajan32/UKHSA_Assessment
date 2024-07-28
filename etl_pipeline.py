import pandas as pd

"""Extract data from the CSV file."""

try:
    data = pd.read_csv("healthcare_dataset.csv")
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    

"""Transform the data to fit the star schema."""
try:
        # Standardize column names
        data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')
    
        # Remove titles and commas, and correct name case
        data['name'] = data['name'].str.title().str.replace(r'^[Mr\.|Mrs\.|Ms\.|Dr\., ]+', '', regex=True)
        
        # Remove trailing commas from hospital names
        data['hospital'] = data['hospital'].str.rstrip(',')
        
        # Convert dates to date format
        data['date_of_admission'] = pd.to_datetime(data['date_of_admission'], format='%d-%m-%Y', errors='coerce').dt.date
        data['discharge_date'] = pd.to_datetime(data['discharge_date'], format='%d-%m-%Y', errors='coerce').dt.date
        
        # Fill missing billing amounts with 0 and ensure numerical format
        data['billing_amount'].fillna(0)
        data['billing_amount'] = pd.to_numeric(data['billing_amount'], errors='coerce')
except Exception as e:
        print(f"Error during data transformation: {e}")
        
        
