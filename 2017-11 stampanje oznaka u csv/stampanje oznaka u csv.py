import csv


with open('oznake.csv', 'r') as f:
  reader = csv.reader(f)
  lst1 = list(reader)


lst2=[]
lst3=[]


# formatiranje stringa
def formatiranje(a1,a2):
    return ('{:>10}'.format(a1[a2])+',')


# pravi listu od clanova prvog elementa lst1
for r in range(len(lst1[0])):
    # provera broja karaktera u stringu
    if len(lst1[0][r])<11:
        # print('manje od 10 karaktera')
        lst2.append(lst1[0][r])
    # prva korekcija
    else:
        in_s = lst1[0][r]
        out_s = in_s.replace("-", "")
        if len(out_s) < 11:
            lst2.append(out_s)
        # druga korekcija
        else:
            in_s=out_s
            out_s1 = in_s.replace("/", "")
            out_s = out_s1.replace(".", "")
            if len(out_s) < 11:
                lst2.append(out_s)
            # treca korekcija
            else:
                if len(out_s) < 11:
                    lst2.append(out_s)
                else:
                    # brisanje prvih n-10 oznaka stringa
                    print('Oznaka', r, '(',out_s,')','vise od 10 clanova nakon druge korekcije')
                    print('Nakon trece korekcije oznaka',r,'(',out_s[len(out_s)-10:],')')
                    lst2.append(out_s[len(out_s)-10:])


for rr in range(len(lst2)):
    lst3.append(formatiranje(lst2,rr))

print('-- pre formatiranja --\n',lst2)
print('-- nakon formatiranja --\n', lst3)


# zapisivanje oznaka u .dat fajl
with open('formatirane-oznake.dat', 'w') as file:
    file.writelines(lst3)







