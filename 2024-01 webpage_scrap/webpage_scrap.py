import requests
from bs4 import BeautifulSoup
import time


def scrape_data(url, max_attempts=5, delay=5):
    attempts = 0
    while attempts < max_attempts:
        try:
            # Send a GET request to the webpage
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the content of the webpage
                soup = BeautifulSoup(response.content, "html.parser")

                # Extract the desired data
                data = {
                    "Naziv kompanije": soup.find(text="Naziv kompanije:")
                    .find_next()
                    .text.strip(),
                    "Registarski broj": soup.find(text="Registarski broj:")
                    .find_next()
                    .text.strip(),
                    "Poreski broj": soup.find(text="Poreski broj:")
                    .find_next()
                    .text.strip(),
                    "Datum osnivanja": soup.find(text="Datum osnivanja:")
                    .find_next()
                    .text.strip(),
                    "Matična kompanija": soup.find(text="Matična kompanija:")
                    .find_next()
                    .text.strip(),
                    "Zemlja porekla": soup.find(text="Zemlja porekla:")
                    .find_next()
                    .text.strip(),
                }
                return data

        except Exception as e:
            print(f"Attempt {attempts + 1} failed: {e}")

        attempts += 1
        time.sleep(delay)  # Wait for 'delay' seconds before next attempt

    return "Failed to retrieve data after maximum attempts."


# URL of the webpage to scrape
url = "http://crm.siepa.gov.rs/suppliers-srb/supplier.php?ID=1813"

# Scrape the data
scraped_data = scrape_data(url)
print(scraped_data)
