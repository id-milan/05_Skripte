# date 2023-08-01
import os

dirname = os.path.dirname(__file__)

konture_ulaz = os.path.join(dirname, "konture-F04.dat")
konture_izlaz = os.path.join(dirname, "konture-F04.txt")


# Open the text file
with open(konture_ulaz, "r") as file:
    lines = file.readlines()

# Open the output file in write mode
with open(konture_izlaz, "w") as out_file:
    # Flag to track whether the next line should be written to the file
    write_next_line = False
    for line in lines:
        # If the flag is true, write the current line to the file
        if write_next_line:
            out_file.write(line)
            # Reset the flag
            write_next_line = False
        # If the line contains the specified text, set the flag to true
        if "C KKONT,NSUR" in line:
            write_next_line = True
