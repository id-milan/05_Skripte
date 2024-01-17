import os

# Specify the base directory
base_dir = os.path.dirname(__file__)

# Construct full file paths
input_file_path = os.path.join(base_dir, "transakcije.txt")
output_file_path = os.path.join(base_dir, "parsed_data.csv")


def read_and_write_15_rows(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        lines = infile.readlines()
        num_lines = len(lines)

        # Write the headers to the output file
        headers = [
            "Broj transakcije",
            "Poslovno ime i sedište platioca - primaoca plaćanja",
            "Broj računa",
            "Poreklo naloga",
            "Datum izvršenja",
            "Datum prijema",
            "Zaduženje",
            "Visina naknade",
            "Odobrenje",
            "Šifra",
            "Svrha plaćanja",
            "(Model) poziv na broj (zaduženja)",
            "(Model) poziv na broj (odobrenja)",
            "Referentna oznaka transakcije",
            "Izvod br",
        ]
        header_row = ",".join(headers)
        outfile.write(header_row + "\n")

        for i in range(0, num_lines, 15):
            chunk = [line.strip() for line in lines[i : i + 15]]  # Strip newline characters
            comma_separated_values = ",".join(chunk)
            outfile.write(comma_separated_values)

            if i + 15 < num_lines:
                outfile.write("\n")  # Add a new line unless it's the last chunk


read_and_write_15_rows(input_file_path, output_file_path)
