# dodati da direktno ucitava .csv i da sa oznakom p-broj zapise .neu i dalje tacke zapise u drugi .neu
# vreme izvrsenja programa
import time
import os
start_time = time.time()

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'tacke.neu')

dat_out = os.path.join(dirname, 't-izlaz.neu')

# tacke.neu fajl sa koordinatama tacaka
fp1 = open(filename)
data = []


# vektor koji treba da se menjea
id_tacke = [1,0,0,0,1,24,0.,0,0,0,]

n = 1
for i, line in enumerate(fp1, start=0):
    # pravi listu od linije
    niz = line.split(',')

    # menja id tacke
    id_tacke[0] = i+1
    lista_u1 = ','.join(map(str, id_tacke)) # pravi string od liste
    lista_u2 = ','.join(map(str, niz)) # pravi string od liste
    data.append(lista_u1)
    data.append('\n')
    data.append(lista_u2)

fp1.close()
print("kraj zamene ID --- %.2fs ---" % (time.time() - start_time))

# zapisuje izmenjeni data u fajl t-izlaz.neu
with open(dat_out, 'w') as file:
    file.writelines(data)

print("kraj zapisa datoteke --- %.2fs ---" % (time.time() - start_time))
