from fajl_sa_blokovima import *
import os

dirname = os.path.dirname(__file__)
neu_fajl = os.path.join(dirname, 'neu_fajl_4m.neu')

try:
    os.remove(neu_fajl)
except OSError:
    pass

sadrzaj_neu_fajla: list = []


def zapis_1red_mat(id_materijala):
    # formatiranje stringa za novi blok i prvu liniju elementa
    izl = str(id_materijala) + ',-601,55,0,0,1,0,'
    return izl


def zapis_1red_prop(id_prop):
    # formatiranje stringa za novi blok i prvu liniju elementa
    izl = str(id_prop) + ',110,1,25,1,0,0,'
    return izl


broj_materijala: int = 4000000


sadrzaj_neu_fajla.append(blok_do_materijala)

for n in range(broj_materijala):
    sadrzaj_neu_fajla.append(zapis_1red_mat(n + 1))
    sadrzaj_neu_fajla.append(blok_materijal)

sadrzaj_neu_fajla.append(blok_kraj_mat)

for n in range(broj_materijala):

    sadrzaj_neu_fajla.append(zapis_1red_prop(n + 1))
    sadrzaj_neu_fajla.append(blok_properti)

sadrzaj_neu_fajla.append(blok_ostatak_fajla)

with open(neu_fajl, 'a') as the_file:
    for item in sadrzaj_neu_fajla:
        the_file.write(item)
