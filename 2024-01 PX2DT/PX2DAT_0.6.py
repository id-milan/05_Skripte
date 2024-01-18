"""
translator iz Plaxis-a u Femapov neu fajl
date 2022-03-21
verzija 0.4

dodato:
- kreiranje odgovarajucih materijala i propertija bez podataka
- zapisivanje elemenata
    - CTETRA
    - CROD
"""


import os
import logging
from data import blokovi
import json
from typing import Optional

dirname = os.path.dirname(__file__)  # file directory path


# config file with
class Config:
    def __init__(self, config_file):
        with open(config_file, "r") as file:
            self.settings = json.load(file)


config = Config(os.path.join(dirname, "config.json"))

# Used files ************************************************************
naziv_ulaznog_fajla = config.settings["naziv_ulaznog_fajla"]
naziv_izlaznog_fajla = config.settings["naziv_izlaznog_fajla"]


logging.basicConfig(
    level=logging.DEBUG, format="{asctime} {levelname} {message}", style="{"
)
logger = logging.getLogger(__name__)  # pravljenje instance loggera


izlaz_dat = os.path.join(dirname, naziv_izlaznog_fajla)

try:
    os.remove(izlaz_dat)
except OSError:
    pass

improoutput = os.path.join(dirname, f"data/{naziv_ulaznog_fajla}")
p3dlog_data = os.path.join(dirname, "data/datasuccess.p3dlog")

with open(improoutput) as plaxis_out:
    # uklanjanje praznih linija prilikom ucitavanja
    px_out = [line.strip() for line in plaxis_out if line.strip()]

with open(p3dlog_data, encoding="utf8") as p3dlog_out:
    # uklanjanje praznih linija prilikom ucitavanja
    p3dlog = [line.strip() for line in p3dlog_out if line.strip()]


# todo broj opterecenja i ogranicenja (dodat kao fiksan u blok1)
# todo $ Femap Load Set 1 : Opterecenje
# todo promeniti zapis u neu format
# todo dodati zapis medjucvora ya 1D element
# // todo $ Femap Property 1 : Property 1
# // todo $ Femap Material 1 : Materijal 1
# // todo GRID (cvorovi)
# // todo elementi
# //  - CTETRA
#   - CTRIA6
# //  - linijski element bez medjucvora CROD


def zapis_stringa(out: str) -> None:
    # dodavanje reda u fajl
    with open(izlaz_dat, "a") as the_file:
        the_file.write(out)


def zapis_liste(lista_out) -> None:
    # dodavanje liste u fajl
    with open(izlaz_dat, "a") as the_file:
        for red in lista_out:
            the_file.write(red)


def get_id(string: str) -> Optional[str]:
    """
    Parses a string and returns a new string composed of the digits in the original string, incremented by 1.

    Args:
    string (str): The input string to parse.

    Returns:
    Optional[str]: A string representation of the incremented number, or None if no digits are found.
    """
    # Extract digits from the string
    ID = "".join([i for i in string if i.isdigit()])

    # Check if the string contains digits
    if ID:
        # Return the incremented value as a string
        return str(int(ID) + 1)
    else:
        # Return None if no ID are found
        return None


def get_mat(lista_gm: list, id_elementa_gm: int) -> int:
    """
    Determines which material is defined for the element.

    Args:
    lista_gm (list): The list containing material information.
    id_elementa_gm (int): The ID of the element to find the material for.

    Returns:
    int: The index of the material, or -1 if not found.
    """
    for index, material_row in enumerate(lista_gm):
        if id_elementa_gm in material_row:
            return index + 1

    return -1


# liste za skladistenje parsovanih datoteka
lista_cvor: list[str] = []
lista_CROD: list[str] = []
lista_CTRIA6: list[str] = []
lista_CTETRA: list[str] = []
lista_C: list[str] = []
lista_V: list[str] = []
lista_C: list[str] = []


def format_V(s_reda: list[str]) -> None:
    # prikupljanje materijala 3D elemenata
    del s_reda[:3]
    lista_id_elemenata = []

    for _, clan in enumerate(s_reda):
        id_elementa = get_id(clan)
        if id_elementa is None:
            pass
        else:
            lista_id_elemenata.append(id_elementa)

    lista_V.append(lista_id_elemenata)
    return None


def format_C(s_reda: list[str]) -> None:
    # prikupljanje materijala 1D elemenata
    del s_reda[:3]
    lista_id_elemenata_C = []

    for _, clan in enumerate(s_reda):
        id_elementa = get_id(clan)
        if id_elementa is None:
            pass
        else:
            lista_id_elemenata_C.append(id_elementa)

    lista_C.append(lista_id_elemenata_C)
    return None


def format_cvora(s_reda: list[str]) -> str:
    # nd_id, x_vrednost, y_vrednost, z_vrednost
    f_out = f"GRID, {get_id(s_reda[0])}, 0, {str(s_reda[3])} {str(s_reda[4])} {str(s_reda[5])}, 0\n"
    return f_out


def format_CTRIA6(s_reda: list[str]) -> str:
    # zapis 2D elementa
    element_id = s_reda[0]
    nd1 = s_reda[3]
    nd2 = s_reda[5]
    nd3 = s_reda[7]
    nd4 = s_reda[4]
    nd5 = s_reda[6]
    nd6 = s_reda[8]

    f_out = f"CTRIA6, {get_id(element_id)}, {get_id(nd1)}, {get_id(nd2)},\
            {get_id(nd3)}, {get_id(nd4)}, {get_id(nd5)}, {get_id(nd6)}\n"
    return f_out


def format_CROD(s_reda: list[str]) -> str:
    # zapis liniskog elementa
    element_id = s_reda[0]
    nd1 = s_reda[3]
    nd2 = s_reda[5]

    mat_id = get_mat(lista_C, get_id(element_id)) + len(lista_V)

    f_out = f"CROD, {get_id(element_id)}, {mat_id}, {get_id(nd1)}, {get_id(nd2)}\n"
    return f_out


def format_CTETRA(s_reda: list[str]) -> str:
    # zapis 3D elementa
    element_id = s_reda[0]
    nd1 = s_reda[3]
    nd2 = s_reda[5]
    nd3 = s_reda[7]
    nd4 = s_reda[12]
    nd5 = s_reda[4]
    nd6 = s_reda[6]
    nd7 = s_reda[8]
    nd8 = s_reda[9]
    nd9 = s_reda[10]
    nd10 = s_reda[11]

    mat_id = get_mat(lista_V, get_id(element_id))

    f_out = f"CTETRA, {get_id(element_id)}, {mat_id}, {get_id(nd1)}, {get_id(nd2)}, {get_id(nd3)}, {get_id(nd4)}, {get_id(nd5)}, \
                {get_id(nd6)}, {get_id(nd7)}, {get_id(nd8)}, {get_id(nd9)}, {get_id(nd10)}\n"

    return f_out


for linija, sadrzaj in enumerate(px_out):
    # pravljenje niza od ucitane linije kao stringa
    # odredjivanje materijala za zapisivanje elemenata
    s_reda = sadrzaj.split()
    # izbacivanje brojeva iz prvog clana niza
    prvi_clan = "".join([i for i in s_reda[0] if not i.isdigit()])
    match prvi_clan:
        case "V":  # spisak razlicitih zapremina
            format_V(s_reda)
        case "C":  # spisak razlicitih zapremina
            format_C(s_reda)


for linija, sadrzaj in enumerate(px_out):
    # pravljenje niza od ucitane linije kao stringa
    s_reda = sadrzaj.split()

    # algoritam:
    # iz prvog clana u redu se izbacuje broj da bi se odredio CASE,
    # ceo red se stavlja u odgovarajuci format, red se zapis_stringauje u fajl

    # izbacivanje brojeva iz prvog clana niza
    prvi_clan = "".join([i for i in s_reda[0] if not i.isdigit()])

    # todo, izmeniti funkcije da odmah dodaju u listu da ne vracaju string pa apendujue
    # grupisanje ulaznog fajla u blokove
    match prvi_clan:
        case "P":  # cvorovi
            lista_cvor.append(s_reda)
        case "LE":  # linijski elementi
            lista_CROD.append(s_reda)
        case "SE":  # povrsinski elementi
            lista_CTRIA6.append(s_reda)
        case "VE":  # zapreminski elementi
            lista_CTETRA.append(s_reda)
        case "C":
            pass
        case "V":
            pass
        case "S":
            pass
        case "UP":
            pass
        case "UC":
            pass
        case "UV":
            pass
        case "MV":
            pass


# liste za skladistenje parsovanih podataka iz p3dlog
lista_set: list[str] = []

for linija, sadrzaj in enumerate(p3dlog):
    # pravljenje niza od ucitane linije kao stringa
    s_point1 = sadrzaj.split()

    match s_point1[0]:
        case "_set":
            s_point2 = sadrzaj.split("_")
            # print(s_point)
            if s_point2[1] == "set Point":
                lista_set.append(s_point1)
                # logger.debug(f": linija {linija}:>>>{sadrzaj}")


lista_prop = []
lista_mat = []


# zapisivanje materijala i propertija 3D elemenata
for linija_3d, sadrzaj_V in enumerate(lista_V):
    lista_prop.append(
        f"$ Femap Property {str(linija_3d+1)}: SOLID_{str(linija_3d+1)}\n\
        PSOLID{str(linija_3d+1):>10}{str(linija_3d+1):>8}       0        \n"
    )
    lista_mat.append(
        f"$ Femap Material {str(linija_3d+1)} : mat_{str(linija_3d+1)}\n\
        MAT1{str(linija_3d+1):>12}                              0.      0.      0.        \n"
    )


# zapisivanje materijala i propertija 1D elemenata
for linija_1d, sadrzaj_C in enumerate(lista_C):
    sledeci_id_1d = len(lista_V) + linija_1d + 1
    lista_prop.append(
        f"$ Femap Property {str(sledeci_id_1d)} : ROD_{str(linija_1d+1)}\n\
        PROD{str(sledeci_id_1d):>12}{str(sledeci_id_1d):>8}      .1      0.      0.      0.        \n"
    )
    lista_mat.append(
        f"$ Femap Material {str(sledeci_id_1d)} : mat_{str(sledeci_id_1d)}\n\
        MAT1{str(sledeci_id_1d):>12}                              0.      0.      0.        \n"
    )


# zapisivanje u datoteku
zapis_stringa(blokovi.b_pocetak)
zapis_liste(lista_prop)
zapis_liste(lista_mat)
zapis_liste(lista_cvor)
zapis_liste(lista_CTETRA)
zapis_liste(lista_CROD)
zapis_stringa(blokovi.b_kraj)


logger.info("Zavrseno zapisivanje")
