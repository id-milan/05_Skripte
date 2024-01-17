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
    dates = lines[5:]

    return [ID, document_type, status, entity, amount] + dates


def read_and_parse_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()

    records = data.strip().split("\n\n")
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
            "Date 3",
        ]
        file.write("\t".join(column_names) + "\n")
        for record in parsed_data:
            file.write("\t".join(record) + "\n")


# Construct full file paths
file_path = os.path.join(base_dir, "data_rashod.txt")
output_file_path = os.path.join(base_dir, "parsed_data_rashod.txt")


# Read and parse the data
parsed_data = read_and_parse_file(file_path)

# Write the parsed data to a file
write_parsed_data_to_file(parsed_data, output_file_path)
