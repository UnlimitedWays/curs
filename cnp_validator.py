from typing import Any

cnp = input("Care este CNP-ul pe care trebuie sa-l verificam?\n")
while cnp.isdigit() is False or len(cnp) != 13:
    cnp = input("CNP-ul nu este valid. Introdu un CNP valid:\n")

#if not len(cnp) == 13:
 #   print ("CNP-ul nu este valid")
  #  exit()
val=[2,7,9,1,4,6,3,5,8,2,7,9]
lista_nr = str(cnp)
s= int(lista_nr[0])
aa = int(lista_nr[1:3])
ll = int(lista_nr[3:5])
zz=int(lista_nr[5:7])
jj=int(lista_nr[7:9])
nnn=int(lista_nr[9:12])
c=int(lista_nr[-1])

lista_nr = lista_nr[:-1]

if ll>12:
    print("CNP-ul nu este valid, ll")
    exit()

if jj>46 and jj !=51 and jj !=52:
    print("CNP-ul nu este valid, jj")
    exit()

if nnn == 0:
    print("CNP-ul nu este valid, nn")
    exit()

if s == 0:
    print("CNP-ul nu este valid, s")
    exit()

if zz > 31:
    print("CNP-ul nu este valid, zi")
    exit()

if not ll == 2:
    pass
elif zz > 29:
    print("CNP-ul nu este valid, ziua peste 29")
    exit()
elif aa%4 != 0:
    print("CNP-ul nu este valid, anul nu este bisect")
    exit()
elif s != 5 or s != 6:
    print("CNP-ul nu este valid")
    exit()


#validator
sumator = 0
for i in range(len(lista_nr)):
        rezultat = int(lista_nr[i]) * int(val[i])
        sumator = sumator + rezultat


rest=sumator%11
print (rest)

if rest == c:
    print("CNP-ul este valid - rest 1")
else:
    if rest == 10 and c==1:
        print("CNP-ul este valid - rest 2")

    else:
        print("CNP-ul este valid - final")

#2990231080069