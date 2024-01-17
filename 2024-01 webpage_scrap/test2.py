import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import csv
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "customer_data.csv")


# Check if the file exists and delete it if it does
if os.path.exists(file_path):
    os.remove(file_path)


list_of_companies_path = os.path.join(base_dir, "test.csv")
with open(list_of_companies_path, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        # Check if row has at least 6 elements
        if len(row) >= 6:
            company_url = "https://search.bisnode.rs" + str(row[5])
            print(company_url, file_path)

        else:
            print(f"Skipping row due to insufficient data: {row}")
