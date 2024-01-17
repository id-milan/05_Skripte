# date 2021-08-05
# verzija 1.2
# dodato
# - zapisivanje oznake konture
# - zapisivanje ID propertija
# - zapisivanje vise 1D elemenata u jednu kontru

import os

dirname = os.path.dirname(__file__)

konture_ulaz = os.path.join(dirname, "konture-ulaz_1.2.txt")
konture_izlaz = os.path.join(dirname, "konture-izlaz_1.2.txt")

try:
    os.remove(konture_izlaz)
except OSError:
    pass

with open(konture_ulaz) as kon:
    konture = kon.readlines()

deo1 = """C Data about flux contour in a table form"""

deo1_0 = """\nC KKONT,NSUR
"""
deo1_1 = '    1'

deo2 = """
C c) BOUNDARY CONDITIONS FOR ONE-DIMENSIONAL ELEMENT
C NN,NPV1,NPV2,NPV3,NPV4"""+'\n'

deo3 = '         0         0         0         0         0         0         0'


def zapis_bloka(kon_ID, prop_ID, kon_OZ, el, nd, n_kontura):
    # formatiranje stringa za novi blok i prvu liniju elementa
    izl = deo1+'     Oznaka - '+str(kon_OZ)+deo1_0+'{:>5}'.format(kon_ID)+'{:>5}'.format(n_kontura)+deo2+'{:>10}'.format(el)+'{:>10}'.format(nd)+deo3+'{:>5}'.format(prop_ID)+'\n'

    with open('konture-izlaz_1.2.txt', 'a') as the_file:
        the_file.write(izl)


def zapis_elementa(prop_ID, el, nd):
    # formatiranje stringa za zapis elemenata
    izl = '{:>10}'.format(el)+'{:>10}'.format(nd)+deo3+'{:>5}'.format(prop_ID)+'\n'

    with open('konture-izlaz_1.2.txt', 'a') as the_file:
        the_file.write(izl)


sadrzaj_raz_prethodni = 0

for linija, sadrzaj in enumerate(konture):
    # pravljenje niza od ucitane linije kao stringa
    sadrzaj_raz = sadrzaj.split()

    if sadrzaj_raz[0] == sadrzaj_raz_prethodni:
        zapis_elementa(sadrzaj_raz[1], sadrzaj_raz[3], sadrzaj_raz[4])
    else:
        zapis_bloka(sadrzaj_raz[0], sadrzaj_raz[1], sadrzaj_raz[2], sadrzaj_raz[3], sadrzaj_raz[4], sadrzaj_raz[5])

    sadrzaj_raz_prethodni = sadrzaj_raz[0]

print("Zavrseno zapisivanje")
