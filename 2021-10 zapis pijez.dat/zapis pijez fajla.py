# date 2021-10-13
# verzija 1.0
# dodato
# - zapisivanje reda u pijez dat formatu


import os

izlaz_putanja='D:/OneDrive/02_Arhiva razno/05_Skripte/2021-10 zapis pijez.dat/izlaz.dat'

try:
    os.remove(izlaz_putanja)
except OSError:
    pass

ulaz_putanja="D:/OneDrive/02_Arhiva razno/05_Skripte/2021-10 zapis pijez.dat/ulaz.dat"

with open(ulaz_putanja) as kon:
    konture = kon.readlines()

# odredjivanje broja redova
broj_ne_praznih_redova = [line.strip("\n") for line in konture if line != "\n"]
broj_redova = str(len(broj_ne_praznih_redova)-1)


def zapis_reda(Oznaka, Element, X, Y, Z, R, S, T, ID_mat):
    # formatiranje stringa za novi blok i prvu liniju elementa
    izl = '{:>15}'.format(Oznaka)+'{:>10}'.format(Element)+'{:>10}'.format(X)+'{:>10}'.format(
        Y)+'{:>10}'.format(Z)+'{:>10}'.format(R)+'{:>10}'.format(S)+'{:>10}'.format(T)+'{:>10}'.format(ID_mat)+'\n'

    with open(izlaz_putanja, 'a') as the_file:
        the_file.write(izl)


def prvi_red(n_redova):
    # formatiranje stringa za novi blok i prvu liniju elementa
    izl = '{:>10}'.format(n_redova)+'\n'

    with open(izlaz_putanja, 'a') as the_file:
        the_file.write(izl)


for linija, sadrzaj in enumerate(konture):
    # pravljenje niza od ucitane linije kao stringa
    sadrzaj_raz = sadrzaj.split()
    if linija == 0:
        prvi_red(broj_redova)
    else:
        zapis_reda(sadrzaj_raz[0], sadrzaj_raz[1], sadrzaj_raz[2], sadrzaj_raz[3],
                   sadrzaj_raz[4], sadrzaj_raz[5], sadrzaj_raz[6], sadrzaj_raz[7], sadrzaj_raz[8])

print("Zavrseno zapisivanje")
