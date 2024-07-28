# UKHSA Assessment ETL Pipeline

This repository contains an ETL pipeline that extracts data from a CSV file, transforms it, and loads it into a SQL Server database.

## Table of Contents

- [Setup Instructions](#setup-instructions)
  - [Step 1: Clone the Repository](#step-1-clone-the-repository)
  - [Step 2: Create a Virtual Environment](#step-2-create-a-virtual-environment)
  - [Step 3: Activate the Virtual Environment](#step-3-activate-the-virtual-environment)
  - [Step 4: Install Dependencies](#step-4-install-dependencies)
  - [Step 5: Test the Database Connection](#step-5-test-the-database-connection)
  - [Step 6: Run the ETL Pipeline](#step-6-run-the-etl-pipeline)
  - [Step 7: Deactivate the Virtual Environment](#step-7-deactivate-the-virtual-environment)
- [Conclusion](#conclusion)
- [Note](#note)

## Setup Instructions

Follow the steps below to set up and run the ETL pipeline on your local machine.

### Step 1: Clone the Repository

Open a command prompt and navigate to the directory where you want to clone the repository.

```cmd
C:\Users\nagar>cd C:\Users\nagar\OneDrive\Documents\GitHub
```

Clone the repository using `git clone`.

```cmd
C:\Users\nagar\OneDrive\Documents\GitHub>git clone https://github.com/nagarajan32/UKHSA_Assessment.git
```

Change to the cloned repository directory.

```cmd
C:\Users\nagar\OneDrive\Documents\GitHub>cd UKHSA_Assessment
```

### Step 2: Create a Virtual Environment

Create a virtual environment to manage project dependencies.

```cmd
C:\Users\nagar\OneDrive\Documents\GitHub\UKHSA_Assessment>python -m venv venv
```

### Step 3: Activate the Virtual Environment

Activate the virtual environment. On Windows, use the following command:

```cmd
C:\Users\nagar\OneDrive\Documents\GitHub\UKHSA_Assessment>venv\Scripts\activate
```

### Step 4: Install Dependencies

Install the required dependencies using `pip`.

```cmd
(venv) C:\Users\nagar\OneDrive\Documents\GitHub\UKHSA_Assessment>pip install -r requirements.txt
```

### Step 5: Test the Database Connection

Run the `test_connection.py` script to test the connection to the SQL Server.

```cmd
(venv) C:\Users\nagar\OneDrive\Documents\GitHub\UKHSA_Assessment>python test_connection.py
```

You should see a message indicating that the connection to the SQL Server is successful.

### Step 6: Run the ETL Pipeline

Run the `etl_pipeline.py` script to execute the ETL process.

```cmd
(venv) C:\Users\nagar\OneDrive\Documents\GitHub\UKHSA_Assessment>python etl_pipeline.py
```

You should see the following output indicating the progress and success of the ETL process:

```
Extracting data...
Data extraction completed successfully.
Transforming data...
Data transformation completed successfully.
Connecting to the database...
Connection successful.
Creating schema 'healthcare'...
Schema 'healthcare' created successfully.
Creating table 'healthcare.healthcare_data'...
Table 'healthcare.healthcare_data' created successfully.
Inserting data into the table...
Data loaded into SQL Server successfully.
```

### Step 7: Deactivate the Virtual Environment

Once you have completed the ETL process, deactivate the virtual environment.

```cmd
(venv) C:\Users\nagar\OneDrive\Documents\GitHub\UKHSA_Assessment>venv\Scripts\deactivate
```

## Conclusion

You have successfully set up and run the ETL pipeline. The data has been extracted from the CSV file, transformed, and loaded into the SQL Server database.

## Note

The above steps and paths are provided as an example. Adjust the paths and commands as necessary based on your environment and directory structure.


