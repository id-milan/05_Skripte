"""
Skripta za parsovanje podataka iz word dokumenta
date: 2023-05-13
version: 1.2
 - dodata iteracija po svim podfolderima
"""


from docx import Document
import csv
import glob


def split_clean(val: str, splt_v: str, b_num: int) -> str:
    """Razdvajanje stringa i vracanje odgovarajuceg clana"""
    c_value = val.replace("\n", "").replace("  ", " ")
    cs_value = c_value.split(splt_v)
    try:
        return cs_value[b_num]

    except IndexError:
        return ""


def extract_data(path: str) -> list:
    """Parsovanje podataka iz word dokumenta u niz"""
    try:
        document = Document(path)

        # Assuming the table is the first one in the document
        table = document.tables[0]

        # Extract data from each cell in the table
        word_data = []
        for row in table.rows:
            row_data = []
            for cell in row.cells:
                cell_text = cell.text.strip()
                clean_data = cell_text.replace("\t", "").replace("\n", "").replace(",", " ").replace("  ", " ")
                row_data.append(clean_data)
            word_data.append(row_data)
        return word_data

    except FileNotFoundError:
        print(f"File '{path}' not found.")

        return None


def write_csv(FILE_PATH):
    data = extract_data(FILE_PATH)

    data_dic = {
        "PUN NAZIV": data[0][1],
        "SKRACENI NAZIV": data[1][1],
        "ADRESA": data[2][1],
        "MATICNI BROJ": data[3][1],
        "PORESKI BROJ": data[4][1],
        "TEKUCI RACUN": data[5][1],
        "PRAVNI OBLIK": data[6][1],
        "DATUM OSNIVANJA": data[7][1],
        "DELATNOST": data[8][1],
        "Telefon": data[9][1],
        "Web": split_clean(data[10][1], "/", 0),
        "E-mail": split_clean(data[10][1], "/", 1),
        "OPIS DELATNOSTI": data[11][1],
        "Folder": os.path.basename(os.path.dirname(FILE_PATH)),
        "Pozicija 1": split_clean(data[12][0], ":", 0),
        "Pozicija 1 Ime": split_clean(data[12][0], ":", 1),
        "Pozicija 1 Linkedin": data[12][2],
        "Pozicija 1 Telefon": data[13][2],
        "Pozicija 1 Mail": data[14][2],
        "Pozicija 2": split_clean(data[15][0], ":", 0),
        "Pozicija 2 Ime": split_clean(data[15][0], ":", 1),
        "Pozicija 2 Linkedin": data[15][2],
        "Pozicija 2 Telefon": data[16][2],
        "Pozicija 2 Mail": data[17][2],
        "Pozicija 3": split_clean(data[18][0], ":", 0),
        "Pozicija 3 Ime": split_clean(data[18][0], ":", 1),
        "Pozicija 3 Linkedin": data[18][2],
        "Pozicija 3 Telefon": data[19][2],
        "Pozicija 3 Mail": data[20][2],
        "Pozicija 4": split_clean(data[21][0], ":", 0),
        "Pozicija 4 Ime": split_clean(data[21][0], ":", 1),
        "Pozicija 4 Linkedin": data[21][2],
        "Pozicija 4 Telefon": data[22][2],
        "Pozicija 4 Mail": data[23][2],
        "Beleske": data[24][1],
    }

    out_path = "kontakti.csv"  # Replace with the desired output file path
    # Write dictionary keys as header and values as a new row
    with open(out_path, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        if n_zapisa == 0:
            writer.writerow(data_dic.keys())  # Write header row
            writer.writerow(data_dic.values())  # Write values as a new row
        else:
            writer.writerow(data_dic.values())  # Write values as a new row

    print(f"Broj zapisanih fajlova: {n_zapisa+1}")


import os
from docx import Document

folder_path = "./kontakti_word"  # Replace with the actual folder path


# Function to recursively find all .docx files in a folder and its subfolders
def find_docx_files(folder_path):
    docx_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".docx"):
                docx_files.append(os.path.join(root, file))
    return docx_files


# Find all .docx files in the folder and its subfolders
docx_files = find_docx_files(folder_path)
n_zapisa = 0
# Process each .docx file
for file_path in docx_files:
    try:
        write_csv(file_path[2:])
        n_zapisa += 1

    except Exception as e:
        print(f"Error processing file: {file_path}\n{str(e)}")
