import csv
import re
import os

# Specify the base directory
base_dir = os.path.dirname(__file__)


def parse_csv(file_path):
    data = []
    current_company = None

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if "POINT" in line:
                parts = line.split(",")
                # Extract coordinates
                coords_part = parts[0].split("(")[1].split(")")[0].split(" ")
                lon, lat = coords_part[0], coords_part[1]
                # Extract company and product
                company = parts[-2] if len(parts) > 2 else "Unknown"
                product = parts[-1].strip()
                current_company = {
                    "company": company,
                    "longitude": lon,
                    "latitude": lat,
                    "products": [product],
                }
                data.append(current_company)
            else:
                # Line with only product code; add it to the current company
                if current_company is not None:
                    current_company["products"].append(line.strip())

    return data


def write_to_txt(data, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        # Write the header row
        file.write("Company, Latitude, Longitude, Products\n")

        for entry in data:
            # Combine all products into a single string, separated by semicolons
            products_combined = "; ".join(entry["products"])
            # Write the data row
            file.write(
                f"{entry['company']}, {entry['latitude']}, {entry['longitude']}, {products_combined}\n"
            )


# Construct full file paths
file_path = os.path.join(base_dir, "Teximp_Srbija_Kupci.csv")
output_file = os.path.join(base_dir, "parsed_data.txt")
parsed_data = parse_csv(file_path)
write_to_txt(parsed_data, output_file)
