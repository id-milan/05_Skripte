# date 2021-08-05
# verzija 1.1
# dodato 
# - zapisivanje oznake konture
# - zapisivanje ID propertija

import os

try:
    os.remove('konture-izlaz.txt')
except OSError:
    pass

with open('konture-ulaz.txt') as kon:
    konture = kon.readlines()

deo1="""C Data about flux contour in a table form"""

deo1_0="""\nC KKONT,NSUR
"""
deo1_1='    1'

deo2="""
C c) BOUNDARY CONDITIONS FOR ONE-DIMENSIONAL ELEMENT
C NN,NPV1,NPV2,NPV3,NPV4"""+'\n'

deo3='         0         0         0         0         0         0         0'


def zapisi(kon_ID, prop_ID, kon_OZ, el, nd):
    # formatiranje stringa
    izl=deo1+'     Oznaka - '+str(kon_OZ)+deo1_0+'{:>5}'.format(kon_ID)+deo1_1+deo2+'{:>10}'.format(el)+'{:>10}'.format(nd)+deo3+'{:>5}'.format(prop_ID)+'\n'

    with open('konture-izlaz.txt', 'a') as the_file:
        the_file.write(izl)


for linija, sadrzaj in enumerate(konture):
    #pravljenje niza od ucitane linije kao stringa
    sadrzaj_raz=sadrzaj.split()
    zapisi(sadrzaj_raz[0], sadrzaj_raz[1], sadrzaj_raz[2], sadrzaj_raz[3], sadrzaj_raz[4])

