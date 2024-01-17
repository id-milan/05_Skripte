import pandas as pd


# Define a function to clean the data
def clean_data(df):
    # Here you can add any data cleaning steps you need
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
    return df


# Read the data from the CSV file
try:
    df = pd.read_csv("kontakti.csv", dtype=str)
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")
    exit()

# Clean the data
df = clean_data(df)

# Define the column sets for the two separate tables
company_columns = [
    "PUN NAZIV",
    "SKRACENI NAZIV",
    "ADRESA",
    "MATICNI BROJ",
    "PORESKI BROJ",
    "TEKUCI RACUN",
    "PRAVNI OBLIK",
    "DATUM OSNIVANJA",
    "DELATNOST",
    "Telefon",
    "Web",
    "E-mail",
    "OPIS DELATNOSTI",
    "Folder",
    "Beleske",
]

# Validate the columns
missing_company_columns = [col for col in company_columns if col not in df.columns]
if missing_company_columns:
    print(f"The following company columns are missing from the data: {missing_company_columns}")
    exit()

# Extract the company data
company_data = df[company_columns]

# Write the company DataFrame to a CSV file
company_data.to_csv("company_data.csv", index=False)

# Prepare employee data
employee_data = pd.DataFrame()
for i in range(1, 5):
    employee_columns = ["MATICNI BROJ", f"Pozicija {i}", f"Pozicija {i} Ime", f"Pozicija {i} Linkedin", f"Pozicija {i} Telefon", f"Pozicija {i} Mail"]
    missing_employee_columns = [col for col in employee_columns if col not in df.columns]
    if missing_employee_columns:
        print(f"The following employee columns are missing from the data: {missing_employee_columns}")
        continue
    temp_data = df[employee_columns]
    temp_data.columns = ["MATICNI BROJ", "Pozicija", "Ime", "Linkedin", "Telefon", "Mail"]
    employee_data = pd.concat([employee_data, temp_data])

# Write the employee DataFrame to a CSV file
employee_data.to_csv("employee_data.csv", index=False)
