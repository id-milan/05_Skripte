# vreme izvrsenja programa
import time
start_time = time.time()

# p2o.neu fajl sa originalnim neu podacima
import linecache
fp1 = open("p2o.neu")

with open('p2o.neu', 'r') as file:
    # cita listu linija u data
    data = file.readlines()

# p2dm.neu fajl odakle cita properti
with open('p2dm.neu', 'r') as file:
    # cita listu linija u data
    data_e = file.readlines()

# odredjuje vrednost novog ID propertija iz p2dm.neu
def n_id(n):
    line_p = linecache.getline("p2dm.neu", n)
    # pravi listu od linije
    niz_p=line_p.split(',')
    return niz_p[2]

n=1
for i, line in enumerate(fp1, start=1):
    if i == n:
        # pravi listu od linije
        niz=line.split(',')
        # zamenjuje treci clan u nizu
        for redni, clan in enumerate(niz):
            if redni==2:
                stari_ID = niz[2]
                niz[2] = n_id(n)
                print('linija', n,'  stari ID:', stari_ID, '  novi ID:', niz[2])
        # pravi string od liste
        lista_u = ','.join(map(str, niz))
        data[i-1] = lista_u
        n+=7
fp1.close()
print("kraj zamene ID --- %.2fs ---" % (time.time() - start_time))

# zapisuje izmenjeni data u fajl p2.neu
with open('p2.neu', 'w') as file:
    file.writelines(data)


print("kraj zapisa datoteke --- %.2fs ---" % (time.time() - start_time))
