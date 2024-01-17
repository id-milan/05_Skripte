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
    1.1
    
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


def bisnode_search(search_company):
    """
    Searches for company information on Bisnode website and returns the data in a structured format.

    Args:
    search_company (str): The company name to search for.

    Returns:
    list: A list of dictionaries containing company data.
    """
    try:
        # URL of the webpage
        url = f"https://search.bisnode.rs/search/?c=RS&q={search_company}"

        # Headers to mimic a real browser request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        # Fetch the webpage
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code != 200:
            return "Failed to retrieve data: HTTP status code " + str(
                response.status_code
            )

        html_content = response.content

        # Parse HTML content
        soup = BeautifulSoup(html_content, "html.parser")

        # Find the table
        table = soup.find("table", class_="responsive personal fL results")

        # Extract data from the table
        all_data = []
        if table:
            rows = table.find_all("tr", class_="search-result")

            # Iterate over each row and extract data
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
        return all_data
    except requests.RequestException as e:
        return f"An error occurred while fetching data: {e}"


# Specify the base directory
base_dir = os.path.dirname(__file__)

# File path for the CSV file
file_path = os.path.join(base_dir, "test.csv")


# Function to read the CSV file and print the first element of each row
with open(file_path, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        if row:  # Check if row is not empty
            all_data = bisnode_search(row[0])
            # Print the extracted data for each row
            for data in all_data:
                print(data)
