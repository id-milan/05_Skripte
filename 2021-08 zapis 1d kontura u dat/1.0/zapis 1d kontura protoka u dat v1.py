import os

try:
    os.remove('konture-izlaz.txt')
except OSError:
    pass


with open('konture-ulaz.txt') as kon:
    konture = kon.readlines()

deo1="""C Data about flux contour in a table form
C KKONT,NSUR
"""
deo11='    1'

deo2="""
C c) BOUNDARY CONDITIONS FOR THREE-DIMENSIONAL ELEMENT
C NN,NPV1,NPV2,NPV3,NPV4"""+'\n'

deo3='         0         0         0         0         0         0         0'


def zapisi(kon, el, nd):
    # formatiranje stringa
    izl=deo1+'{:>5}'.format(kon)+deo11+deo2+'{:>10}'.format(el)+'{:>10}'.format(nd)+deo3+'\n'

    with open('konture-izlaz.txt', 'a') as the_file:
        the_file.write(izl)


for linija, sadrzaj in enumerate(konture):
    #pravljenje niza od ucitane linije kao stringa
    sadrzaj_raz=sadrzaj.split()
    zapisi(sadrzaj_raz[0], sadrzaj_raz[2], sadrzaj_raz[3])

