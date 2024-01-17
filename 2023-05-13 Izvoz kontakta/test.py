import pandas as pd
import csv


def parse_data(filename):
    # Read the data from the file
    df = pd.read_csv(filename, dtype=str)

    # Split the data into two tables: company and employees
    company_data = df.iloc[:, :14]
    employee_data = df.iloc[:, 14:]

    # Rename the columns for the employee data
    employee_data.columns = ["Position", "Name", "Linkedin", "Phone", "Email"] * 4

    # Initialize empty lists to hold the parsed data
    parsed_company_data = []
    parsed_employee_data = []

    # Iterate over each row in the dataframes
    for _, row in df.iterrows():
        company_row = row[:14]
        parsed_company_data.append(company_row)

        for i in range(4):
            employee_row = row[14 + 5 * i : 14 + 5 * (i + 1)]
            # Only append the employee row if it contains a name
            if pd.notnull(employee_row["Name"]):
                # Add the company's MATICNI_BROJ to the employee row
                employee_row["MATICNI_BROJ"] = company_row["MATICNI_BROJ"]
                parsed_employee_data.append(employee_row)

    # Convert the parsed data lists back into dataframes
    parsed_company_data = pd.DataFrame(parsed_company_data, columns=company_data.columns)
    parsed_employee_data = pd.DataFrame(parsed_employee_data, columns=employee_data.columns)

    # Write the parsed data to CSV files
    parsed_company_data.to_csv("parsed_company_data.csv", index=False, quoting=csv.QUOTE_NONNUMERIC)
    parsed_employee_data.to_csv("parsed_employee_data.csv", index=False, quoting=csv.QUOTE_NONNUMERIC)


# Call the function with the name of your file
parse_data("kontakti.csv")
