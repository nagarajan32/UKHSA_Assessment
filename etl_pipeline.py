import pandas as pd

"""Extract data from the CSV file."""

try:
    data = pd.read_csv("healthcare_dataset.csv")
    data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    

"""Transform the data to fit the star schema."""
try:
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
        

# Create Dimension Tables
dim_patient = data[['name', 'age', 'gender', 'blood_type', 'medical_condition', 'date_of_admission']].drop_duplicates().reset_index(drop=True)
dim_patient.rename(columns={'name': 'patient_name', 'date_of_admission': 'date_of_admission'}, inplace=True)
dim_patient['patient_id'] = range(1, len(dim_patient) + 1)
dim_patient = dim_patient[['patient_id', 'patient_name', 'age', 'gender', 'blood_type', 'medical_condition', 'date_of_admission']]
print("Dimension Patient Table:")
print(dim_patient.head())
        
dim_doctor = pd.DataFrame(data['doctor'].unique(), columns=['doctor_name'])
dim_doctor['doctor_id'] = range(1, len(dim_doctor) + 1)
print("Dimension Doctor Table:")
print(dim_doctor.head())
        
dim_hospital = pd.DataFrame(data['hospital'].unique(), columns=['hospital_name'])
dim_hospital['hospital_id'] = range(1, len(dim_hospital) + 1)
print("Dimension Hospital Table:")
print(dim_hospital.head())
        
dim_insurance = pd.DataFrame(data['insurance_provider'].unique(), columns=['insurance_provider'])
dim_insurance['insurance_id'] = range(1, len(dim_insurance) + 1)
print("Dimension Insurance Table:")
print(dim_insurance.head())

# Create Fact Table
data = data.merge(dim_patient, how='left', left_on=['name', 'date_of_admission'], right_on=['patient_name', 'date_of_admission'])
data = data.merge(dim_doctor, how='left', left_on='doctor', right_on='doctor_name')
data = data.merge(dim_hospital, how='left', left_on='hospital', right_on='hospital_name')
data = data.merge(dim_insurance, how='left', left_on='insurance_provider', right_on='insurance_provider')
        
fact_healthcare = data[['patient_id', 'doctor_id', 'hospital_id', 'insurance_id', 'billing_amount', 'room_number', 'admission_type', 'discharge_date', 'medication', 'test_results']].copy()
fact_healthcare['admission_id'] = range(1, len(fact_healthcare) + 1)
fact_healthcare = fact_healthcare[['admission_id', 'patient_id', 'doctor_id', 'hospital_id', 'insurance_id', 'billing_amount', 'room_number', 'admission_type', 'discharge_date', 'medication', 'test_results']]
print("Fact Healthcare Table:")
print(fact_healthcare.head())      
        
        
