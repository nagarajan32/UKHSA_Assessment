import pandas as pd
import pyodbc
import os
from dotenv import load_dotenv

def load_env():
    """Load environment variables from .env file."""
    try:
        load_dotenv()
        
    except Exception as e:
        print(f"Error loading environment variables: {e}")
        raise

def extract_data(file_path):
    """Extract data from the CSV file."""
    try:
        data = pd.read_csv(file_path)
        print("Data extraction completed successfully.")
        return data  
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        raise

def transform_data(data):
    """Transform data to the required format."""
    try:
        # Standardize column names
        data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')

        # Remove titles and commas, and correct name case
        data['name'] = data['name'].str.title().str.replace(r'^(Mr\.|Mrs\.|Ms\.|Dr\.)\s+', '', regex=True)
        
        # Remove trailing commas from hospital names
        data['hospital'] = data['hospital'].str.rstrip(',')

        # Convert dates
        data['date_of_admission'] = pd.to_datetime(data['date_of_admission'], errors='coerce')
        data['discharge_date'] = pd.to_datetime(data['discharge_date'], errors='coerce')

        print("Data transformation completed successfully.")
        return data
    except Exception as e:
        print(f"Error during data transformation: {e}")
        raise

def get_connection_string():
    """Build and return the connection string for SQL Server."""
    try:
        connection_string = (
            f"DRIVER={os.getenv('DRIVER')};"
            f"SERVER={os.getenv('SERVER_NAME')};"
            f"DATABASE={os.getenv('DATABASE')};"
            f"UID={os.getenv('USER')};"
            f"PWD={os.getenv('PASSWORD')}"
        )
        return connection_string
    except Exception as e:
        print(f"Error building connection string: {e}")
        raise

def create_schema(cursor, schema_name):
    """Create schema if it doesn't exist."""
    try:
        cursor.execute(f"IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = '{schema_name}') EXEC('CREATE SCHEMA {schema_name}')")
        cursor.commit()
        print(f"Schema '{schema_name}' created successfully.")
    except pyodbc.Error as e:
        print(f"Error creating schema: {e}")
        raise

def create_table(cursor, schema_name, table_name):
    """Create table in the specified schema."""
    create_table_query = f"""
    IF OBJECT_ID('{schema_name}.{table_name}', 'U') IS NOT NULL DROP TABLE {schema_name}.{table_name};
    CREATE TABLE {schema_name}.{table_name} (
        name VARCHAR(255),
        age INT,
        gender VARCHAR(10),
        blood_type VARCHAR(10),
        medical_condition VARCHAR(255),
        date_of_admission DATE,
        doctor VARCHAR(255),
        hospital VARCHAR(255),
        insurance_provider VARCHAR(255),
        billing_amount FLOAT,
        room_number INT,
        admission_type VARCHAR(50),
        discharge_date DATE,
        medication VARCHAR(255),
        test_results VARCHAR(255)
    );
    """
    try:
        cursor.execute(create_table_query)
        cursor.commit()
        print(f"Table '{schema_name}.{table_name}' created successfully.")
    except pyodbc.Error as e:
        print(f"Error creating table: {e}")
        raise

def insert_data(cursor, schema_name, table_name, data):
    """Insert data into the specified table."""
    insert_query = f"""
    INSERT INTO {schema_name}.{table_name} (name, age, gender, blood_type, medical_condition, date_of_admission, doctor, hospital, insurance_provider, billing_amount, room_number, admission_type, discharge_date, medication, test_results)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    try:
        cursor.fast_executemany = True
        cursor.executemany(insert_query, data.values.tolist())
        cursor.commit()
    except pyodbc.Error as e:
        print(f"Error inserting data: {e}")
        raise

def main():
    try:
        load_env()

        print("Extracting data...")
        data = extract_data('healthcare_dataset.csv')

        print("Transforming data...")
        data = transform_data(data)

        schema_name = 'healthcare'
        table_name = 'healthcare_data'

        connection_string = get_connection_string()

        print("Connecting to the database...")
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        print("Connection successful.")

        print(f"Creating schema '{schema_name}'...")
        create_schema(cursor, schema_name)

        print(f"Creating table '{schema_name}.{table_name}'...")
        create_table(cursor, schema_name, table_name)

        print("Inserting data into the table...")
        insert_data(cursor, schema_name, table_name, data)

        cursor.close()
        conn.close()

        print("Data loaded into SQL Server successfully.")
    except Exception as e:
        print(f"Error in ETL process: {e}")

if __name__ == "__main__":
    main()
