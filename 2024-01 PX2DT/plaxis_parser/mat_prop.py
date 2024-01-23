from typing import Tuple, List

lista_prop = []
lista_mat = []


def mat_prop_list(lista_v, lista_c) -> Tuple[List[str], List[str]]:
    # zapisivanje materijala i propertija 3D elemenata
    for linija_3d, sadrzaj_V in enumerate(lista_v):
        lista_prop.append(
            f"$ Femap Property {str(linija_3d+1)}: SOLID_{str(linija_3d+1)}\n\
            PSOLID{str(linija_3d+1):>10}{str(linija_3d+1):>8}       0        \n"
        )
        lista_mat.append(
            f"$ Femap Material {str(linija_3d+1)} : mat_{str(linija_3d+1)}\n\
            MAT1{str(linija_3d+1):>12}                              0.      0.      0.        \n"
        )

    # zapisivanje materijala i propertija 1D elemenata
    for linija_1d, sadrzaj_C in enumerate(lista_c):
        sledeci_id_1d = len(lista_v) + linija_1d + 1
        lista_prop.append(
            f"$ Femap Property {str(sledeci_id_1d)} : ROD_{str(linija_1d+1)}\n\
            PROD{str(sledeci_id_1d):>12}{str(sledeci_id_1d):>8}      .1      0.      0.      0.        \n"
        )
        lista_mat.append(
            f"$ Femap Material {str(sledeci_id_1d)} : mat_{str(sledeci_id_1d)}\n\
            MAT1{str(sledeci_id_1d):>12}                              0.      0.      0.        \n"
        )
    return lista_prop, lista_mat
