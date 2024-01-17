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
    1.0.1
    
Date:
    2024-01-05
"""

import requests
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def bisnode_search(search_company):
    # URL of the webpage
    url = f"https://search.bisnode.rs/search/?c=RS&q={search_company}"

    # Fetch the webpage
    response = requests.get(url)
    html_content = response.content

    # Parse HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the table
    # Note: Adjust the selector based on the actual table structure and class
    table = soup.find("table", class_="responsive personal fL results")

    # Extract data from the table
    data = []
    if table:
        rows = table.find_all("tr", class_="search-result")

        all_data = []

        # Iterate over each row and extract data
        for row in rows:
            data = {
                "Matični broj": row.find("td", class_="search-result-id").text.strip()
                if row.find("td", class_="search-result-id")
                else None,
                "Naziv": row.find("td", class_="search-result-name").text.strip()
                if row.find("td", class_="search-result-name")
                else None,
                "Adresa": row.find("td", class_="search-result-address").text.strip()
                if row.find("td", class_="search-result-address")
                else None,
                "Poštanski broj": row.find(
                    "td", class_="search-result-postCode"
                ).text.strip()
                if row.find("td", class_="search-result-postCode")
                else None,
                "Pošta": row.find("td", class_="search-result-postName").text.strip()
                if row.find("td", class_="search-result-postName")
                else None,
                "Link": row.find("a", class_="search-result-link")["href"]
                if row.find("a", class_="search-result-link")
                else None,
            }
            all_data.append(data)
    return all_data


bisnode_search("solfins")
# Print the extracted data for each row
for data in all_data:
    print(data)
