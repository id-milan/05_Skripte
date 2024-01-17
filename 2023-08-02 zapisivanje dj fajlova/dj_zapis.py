# date 2023-08-01
import os

dirname = os.path.dirname(__file__)

dj_ulaz = os.path.join(dirname, "dj-NB-L15-07-09-MB.dat")
dj_izlaz = os.path.join(dirname, "dj-NB-L15-07-09-MB")


# Open the text file
with open(dj_ulaz, "r") as file:
    lines = file.readlines()


# Open the output file in write mode
with open(dj_izlaz, 'w') as out_file:
    for line in lines:
        # Write only the first 10 characters of each line
        out_file.write(line[:10] + '\n')
