# skripta za zapisivanje mernih mesta u M fajl
# date 2020-03-25
# version 1.2

import os

dirname = os.path.dirname(__file__)

# fajl sa mernim mestima
merna_mesta = os.path.join(dirname, "L10_merna_mesta.dat")

# naziv izlaznog fajla
izlazni_fajl = os.path.join(dirname, "L10_M_MESTA.M")
out_file = open(izlazni_fajl, "a")


# funkcija koja ubacuje novu liniju na pocetak fajla
def insert_l(nova_linija):
    # citanje podataka iz fajla
    with open(izlazni_fajl, "r+") as f:
        a = f.read()
        # zapisivanje u fajl nove linije + stari podaci
        with open(izlazni_fajl, "w+") as f:
            f.write(nova_linija + "\n" + a)


blokovi_pocinju = []
with open(merna_mesta) as f:
    for n_linija, l in enumerate(f):
        sadrzaj = l.split("\t")

        if len(sadrzaj) > 0 and len(sadrzaj) < 10:
            blokovi_pocinju.append(n_linija)
        else:
            pass
blokovi_pocinju.append(n_linija + 1)
print(blokovi_pocinju)

blok = 0
broj_tacaka_2 = []
with open(merna_mesta) as file:
    for line_id, line_content in enumerate(file):
        line_c = line_content.rstrip()
        line_el = line_c.split("\t")

        if len(line_el) < 5:
            broj_tacaka = blokovi_pocinju[1 + blok] - blokovi_pocinju[0 + blok] - 1
            broj_tacaka_2.append(broj_tacaka)
            out_file.write(
                f"{broj_tacaka:>5}{'Oznaka':>15}{'ElementID':>10}\
                {'Point X':>10}{'Point Y':>10}{'Point Z':>10}\
                {'R':>10}{'S':>10}{'T':>10}{'Prop':>5} - {line_el[0]}\n"
            )
            blok += 1
        else:
            out_file.write(
                f"{line_el[0]:>5}{line_el[1]:>15.15}{line_el[2]:>10.10}\
                {line_el[3]:>10.10}{line_el[4]:>10.10}{line_el[5]:>10.10}\
                {line_el[6]:>10.10}{line_el[7]:>10.10}\
                {line_el[8]:>10.10}{line_el[9]:>5.5}\n"
            )


out_file.close()

lin_2 = []
for n1, n2 in enumerate(broj_tacaka_2):
    lin_2.append(f"{str(broj_tacaka_2[n1]):>10}")

# ubacuje liniju sa broje tacaka prema tipu
insert_l("".join(lin_2))
# ubacuje liniju sa brojem razlicitih instrumenata mernih mesta
insert_l(f"{str(len(blokovi_pocinju)-1):>10}")
