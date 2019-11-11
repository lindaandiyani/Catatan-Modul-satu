angka = list(range(101))
# print(angka)

genap= list(filter(lambda x: x % 2==0,angka))
# print(genap)

def dikalikanDua(a):
    return a*2
kaliDua= list(map(dikalikanDua,genap))
print(kaliDua)

from functools import reduce
jumlahSemua= reduce (lambda a,y: a+y,kaliDua)
print(jumlahSemua)