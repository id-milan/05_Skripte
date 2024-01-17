"""
Brief Description: 
    This module is designed to scrape data from a specific webpage (https://search.bisnode.rs/search/).
    It queries the page for information about a company named and extracts relevant details 
    from the search results. 

    The script handles encoding issues by setting the default encoding to UTF-8 to ensure compatibility 
    with non-ASCII characters often found in company names and addresses.

Usage:
    import my_module
    data = my_module.scrape('https://example.com')

Dependencies:
    requests, BeautifulSoup

Author:
    Milan Bojovic

Version:
    1.2
    
Date:
    2024-01-05
"""

import requests
from bs4 import BeautifulSoup
import sys
import io
import os
import csv

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


import csv


def bisnode_search_to_csv(search_company, csv_file_path):
    """
    Searches for company information on Bisnode website, returns the data in a structured format,
    and appends it to a CSV file. If the file does not exist, it will be created.
    If no data is found for a company, it prints the company name and skips the iteration.

    Args:
    search_company (str): The company name to search for.
    csv_file_path (str): The file path for the CSV file where the data will be saved.

    Returns:
    str: A message indicating the success or failure of the operation.
    """
    try:
        # URL of the webpage
        url = f"https://search.bisnode.rs/search/?c=RS&q={search_company}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return "Failed to retrieve data: HTTP status code " + str(
                response.status_code
            )

        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        table = soup.find("table", class_="responsive personal fL results")

        all_data = []
        if table:
            rows = table.find_all("tr", class_="search-result")

            for row in rows:
                row_data = {
                    "Matični broj": row.find("td", class_="search-result-id").get_text(
                        strip=True
                    )
                    if row.find("td", class_="search-result-id")
                    else "",
                    "Naziv": row.find("td", class_="search-result-name").get_text(
                        strip=True
                    )
                    if row.find("td", class_="search-result-name")
                    else "",
                    "Adresa": row.find("td", class_="search-result-address").get_text(
                        strip=True
                    )
                    if row.find("td", class_="search-result-address")
                    else "",
                    "Poštanski broj": row.find(
                        "td", class_="search-result-postCode"
                    ).get_text(strip=True)
                    if row.find("td", class_="search-result-postCode")
                    else "",
                    "Pošta": row.find("td", class_="search-result-postName").get_text(
                        strip=True
                    )
                    if row.find("td", class_="search-result-postName")
                    else "",
                    "Link": row.find("a", class_="search-result-link").get("href", "")
                    if row.find("a", class_="search-result-link")
                    else "",
                }
                all_data.append(row_data)

        # Check if all_data is empty
        if not all_data:
            print(f"No data found for {search_company}. Skipping this iteration.")
            return f"No data found for {search_company}. Skipping this iteration."

        # Write or append data to CSV file
        write_header = not os.path.exists(csv_file_path)
        with open(csv_file_path, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=all_data[0].keys(), delimiter=";")
            if write_header:
                writer.writeheader()
            writer.writerows(all_data)

        return "Data successfully appended to " + csv_file_path
    except requests.RequestException as e:
        return f"An error occurred while fetching data: {e}"
    except IOError as e:
        return f"An error occurred while writing to CSV file: {e}"


# Note: This function is not executed here as it involves web scraping and file operations. You can test it by providing valid inputs.


# Specify the base directory
base_dir = os.path.dirname(__file__)

# File path for the CSV file
file_path = os.path.join(base_dir, "Teximp.csv")
csv_path = os.path.join(base_dir, "bisnode_search_results.csv")

# Check if the file exists and delete it if it does
if os.path.exists(csv_path):
    os.remove(csv_path)

# Function to read the CSV file and parse search data
with open(file_path, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        if row:  # Check if row is not empty
            bisnode_search_to_csv(row[0], csv_path)
