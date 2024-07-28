# UKHSA Assessment ETL Pipeline

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Approach and Methodologies](#approach-and-methodologies)
- [Setup Instructions](#setup-instructions)
- [Execution](#execution)
- [Deactivation](#deactivation)
- [Conclusion](#conclusion)

## Introduction
This repository includes an ETL pipeline for processing healthcare data. It features a Python script for extracting, transforming, and loading data from a CSV into a SQL Server database, along with environment configuration (`.env`), dependencies (`requirements.txt`), and sample data (`healthcare_dataset.csv`).

## Prerequisites

Before setting up and running the ETL pipeline, ensure that you have the following prerequisites:

### **1. Software**

- **Python 3.x**: The pipeline requires Python 3.x to run. Make sure Python is installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

- **pip**: Python's package installer, `pip`, is required to install the necessary dependencies. It is included with Python 3.x.

- **Git**: Required for cloning the repository. You can download and install Git from [Git's official website](https://git-scm.com/downloads).

### **2. SQL Server**

- **MS SQL Server**: A running instance of SQL Server is required. This can be a local or remote SQL Server. The script requires SQL Server 2016 or later version. (Note: This script is designed to use SQL Server Authentication (username and password) and does not support Windows Authentication)

- **ODBC Driver for SQL Server**: The appropriate ODBC driver must be installed to enable connectivity between Python and SQL Server. For example, [ODBC Driver 17 for SQL Server](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server) is commonly used.

### **3. Environment**

- **.env File Configuration**: Make sure to configure the `.env` file with the appropriate database connection settings.

### **4. Optional**

- **Notepad or Text Editor**: Required to edit the `.env` file. You can use any text editor of your choice, such as Notepad or VSCode.

### **5. Access Permissions**

- **Permissions to SQL Server**: This script is designed to use SQL Server Authentication (username and password) and does not support Windows Authentication. Ensure that the user under which the script is running has the necessary permissions to create schemas and tables and insert data into the SQL Server database.

## Approach and Methodologies
### Repository Setup and Organization
- The repository is organized with a clear structure, including scripts for ETL processes and a requirements file for dependencies.
- Usage of a virtual environment to manage dependencies ensures that the project environment is isolated and reproducible.

### Environment Configuration
- The `.env` file is used to securely manage and access sensitive information such as database credentials. This ensures that credentials are not hard-coded into the script, enhancing security and flexibility.

### ETL Pipeline Implementation
- **Extraction:**
    - The data extraction process involves reading data from a CSV file using `pandas`. The extraction function includes error handling to manage potential issues during file reading.
- **Transformation:**
    - Data transformation includes standardizing column names, cleaning data (e.g., removing titles and correcting name cases), and converting date fields to the appropriate format. This ensures that the data is consistent and ready for loading into the database.
- **Loading:**
    - Data loading involves connecting to a SQL Server database using `pyodbc`. The script includes creating schemas and tables if they do not exist and inserting the transformed data into the specified table. Error handling is implemented to manage issues during database operations.

### Error Handling
- Comprehensive error handling is included in each step of the ETL process (extraction, transformation, loading). This ensures that any issues encountered during the process are captured and reported, facilitating easier debugging and maintenance.

### Modular Design
- The ETL pipeline is implemented in a modular fashion with distinct functions for each step of the process (loading environment variables, extracting data, transforming data, building connection strings, creating schemas, creating tables, inserting data). This improves code readability, maintainability, and reusability.

### Logging and Progress Indicators
- The script includes print statements to indicate the progress of the ETL process, such as successful completion of data extraction, transformation, schema creation, table creation, and data insertion. This provides visibility into the pipeline's execution and helps identify where issues may occur.

### Database Connection Management
- The script manages database connections efficiently, ensuring connections are opened before database operations and closed after operations are completed. This helps in maintaining the integrity and performance of the database.

### Data Validation and Cleaning
- Data transformation includes specific steps for cleaning and validating the data, such as correcting name cases, stripping unnecessary characters, and handling date conversions. This ensures the data loaded into the database is accurate and consistent.

### Documentation
- The README file provides comprehensive setup instructions, including commands to clone the repository, set up the virtual environment, install dependencies, configure environment variables, test the database connection, run the ETL pipeline, and deactivate the virtual environment. This makes it easy for others to understand and replicate the setup.

### Version Control
- The use of Git for version control ensures that the project history is tracked, changes are documented, and collaboration is facilitated. The repository link can be shared for review and further development.

## Setup Instructions

1. **Open Command Prompt:**
    ```cmd
    C:\Users\YourUsername>
    ```
    Example:
    ```cmd
    C:\Users\nagar>
    ```

2. **Change the directory to where you want to clone the repository:**
    ```cmd
    cd path\to\your\desired\directory
    ```
    Example:
    ```cmd
    C:\Users\nagar> cd C:\Users\nagar\OneDrive\Documents\GitHub
    ```

3. **Clone the repository:**
    ```cmd
    git clone https://github.com/nagarajan32/UKHSA_Assessment.git
    ```
    Example:
    ```cmd
    C:\Users\nagar\OneDrive\Documents\GitHub> git clone https://github.com/nagarajan32/UKHSA_Assessment.git
    ```

4. **Navigate to the repository directory:**
    ```cmd
    cd path\to\the\cloned\repository
    ```
    Example:
    ```cmd
    C:\Users\nagar\OneDrive\Documents\GitHub> cd C:\Users\nagar\OneDrive\Documents\GitHub\UKHSA_Assessment
    ```

5. **Create a virtual environment:**
    ```cmd
    python -m venv venv
    ```
    Example:
    ```cmd
    C:\Users\nagar\OneDrive\Documents\GitHub\UKHSA_Assessment>python -m venv venv
    ```

6. **Activate the virtual environment on Windows:**
    ```cmd
    venv\Scripts\activate
    ```
    Example:
    ```cmd
    C:\Users\nagar\OneDrive\Documents\GitHub\UKHSA_Assessment>venv\Scripts\activate
    ```

7. **Install the required dependencies:**
    ```cmd
    pip install -r requirements.txt
    ```
    Example:
    ```cmd
    (venv) C:\Users\nagar\OneDrive\Documents\GitHub\UKHSA_Assessment>pip install -r requirements.txt
    ```

8. **Edit the .env file**

    The `.env` file contains sensitive information such as database credentials. You need to edit this file to include the correct details for your SQL Server setup.

    **To open and edit the `.env` file:**
    ```cmd
    notepad .env
    ```
    Example:
    ```cmd
    (venv) C:\Users\nagar\OneDrive\Documents\GitHub\UKHSA_Assessment> notepad .env
    ```

    **Update the following contents in the `.env` file:**
   ```
    DRIVER=<Enter the Driver name>
    SERVER_NAME=<Your Server Name>
    DATABASE=<Enter the database name>
    USER=<Your UserNmae>
    PASSWORD=<Your Password>
    ```

    **Example:**

    If you open the `.env` file in Notepad, it should look like this:

    ```plaintext
    DRIVER=ODBC DRIVER 17 FOR SQL SERVER
    SERVER_NAME=NAGARAJAN
    DATABASE=UKHSA
    USER=User1
    PASSWORD=User@1
    ```
    After making the changes, save the file and close Notepad.

## Execution

1. **Test the database connection:**
    ```cmd
    python test_connection.py
    ```
    Example:
    ```cmd
    (venv) C:\Users\nagar\OneDrive\Documents\GitHub\UKHSA_Assessment>python test_connection.py
    ```
    Output should be:
    ```cmd
    Connection to SQL Server is successful.
    ```

2. **Run the ETL pipeline:**
    ```cmd
    python etl_pipeline.py
    ```
    Example:
    ```cmd
    (venv) C:\Users\nagar\OneDrive\Documents\GitHub\UKHSA_Assessment>python etl_pipeline.py
    ```
    Expected output:
    ```cmd
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

## Deactivation

1. **Deactivate the virtual environment:**
    ```cmd
    venv\Scripts\deactivate
    ```
    Example:
    ```cmd
    (venv) C:\Users\nagar\OneDrive\Documents\GitHub\UKHSA_Assessment>venv\Scripts\deactivate
    ```

## Conclusion

You have successfully set up and run the ETL pipeline. The data has been extracted from the CSV file, transformed, and loaded into the SQL Server database.
