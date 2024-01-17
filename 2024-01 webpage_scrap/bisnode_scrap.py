import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import csv
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


# Function to scrape data from a given URL and append to a CSV file
def scrape_and_append_to_csv(url, file_path):
    # Fetch the webpage
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Function to safely extract text
    def safe_extract(soup, text_label):
        element = soup.find(string=text_label)
        if element:
            next_element = element.find_next()
            if next_element and next_element.string:
                return next_element.string.strip()
        return "Not Found"

    # Extract the required data
    data = {
        "Puni naziv": safe_extract(soup, "Puni naziv:"),
        "Skraćeni naziv": safe_extract(soup, "Skraćeni naziv:"),
        "Adresa": safe_extract(soup, "Adresa:"),
        "Pošta i mesto": safe_extract(soup, "Pošta i mesto:"),
        "Region": safe_extract(soup, "Region:"),
        "Matični broj": safe_extract(soup, "Matični broj:"),
        "Poreski br.": safe_extract(soup, "Poreski br.:"),
        "Pravni oblik:": safe_extract(soup, "Pravni oblik:"),
        "Datum osnivanja:": safe_extract(soup, "Datum osnivanja:"),
        "Delatnost:": safe_extract(soup, "Delatnost:"),
    }

    # Convert to DataFrame
    df = pd.DataFrame([data])

    # Check if file exists to append or write new
    if os.path.exists(file_path):
        df.to_csv(file_path, mode="a", header=False, sep=";", index=False)
    else:
        df.to_csv(file_path, sep=";", index=False)


# Specify the file path
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "bisnode_scrap_results.csv")


# Check if the file exists and delete it if it does
if os.path.exists(file_path):
    os.remove(file_path)


# Example usage
url = "https://search.bisnode.rs/rs/1316826/svoksen-doo/"
scrape_and_append_to_csv(url, file_path)


list_of_companies_path = os.path.join(base_dir, "bisnode_search_results.csv")

# Function to read the CSV file and parse company data do file
with open(list_of_companies_path, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        if row:  # Check if row is not empty
            scrape_and_append_to_csv("https://search.bisnode.rs" + row[5], file_path)
