import os

# Specify the base directory
base_dir = os.path.dirname(__file__)


def parse_record(record):
    lines = record.split("\n")
    ID = lines[0]
    document_type = lines[1]
    status = lines[2]
    entity = lines[3]
    amount = lines[4]
    dates = lines[5:-1]

    return [ID, document_type, status, entity, amount] + dates


def read_and_parse_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Split data every 7 lines
    records = ["".join(lines[i : i + 7]) for i in range(0, len(lines), 7)]

    return [parse_record(record) for record in records]


def write_parsed_data_to_file(parsed_data, output_file_path):
    with open(output_file_path, "w", encoding="utf-8") as file:
        column_names = [
            "ID",
            "Document Type",
            "Status",
            "Entity",
            "Amount",
            "Date 1",
            "Date 2",
        ]
        file.write("\t".join(column_names) + "\n")
        for record in parsed_data:
            file.write("\t".join(record) + "\n")


# Construct full file paths
file_path = os.path.join(base_dir, "data_prihod.txt")
output_file_path = os.path.join(base_dir, "parsed_data_prihod.txt")

# Check if file exists and delete it if it does
if os.path.exists(output_file_path):
    os.remove(output_file_path)

# Read and parse the data
parsed_data = read_and_parse_file(file_path)

# Write the parsed data to a file
write_parsed_data_to_file(parsed_data, output_file_path)
