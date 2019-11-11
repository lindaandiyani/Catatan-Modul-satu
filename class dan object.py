# class = cetakan objectc
'''
class mobil:
    Warna = 'merah'
    tahun = 2010

# create object mobil1
mobil1= mobil()
print(mobil1)
print(mobil1.Warna)
print(mobil1.tahun)

# mobil2= mobil()
# print(mobil2.Warna)


class mobilCustome():
    def __init__(self,warna,tahun,model):
        self.colour = warna
        self.year = tahun
        self.model = model
mobil1 = mobilCustome('pink', 2018, ['A','B'])
mobil2 = mobilCustome('blue', 2010,['B','C'])

print(mobil1.colour)
print(mobil2.model)

class mobilCustome():
    def __init__(self,warna,tahun,model):
        self.colour = warna
        self.year = tahun
        self.model = model
        # method
    def jadul (self):
        if int(self.year) < 2010:
            return True
        else:
            return False
    def tes(self):
        print(self.colour,self.year,self.model,self.jadul())
mobilA = mobilCustome('merah','1998','X')
mobilB = mobilCustome('merah','2018','Z')
print(mobilA.year)
print(mobilB.tes())
print(mobilB.jadul())

class mobil:
    def __init__(self,warna,seat):
        self.warna = warna
        self.seat = seat
class car(mobil): #inheritance
    # pass #inheritance sama persis
    gps = True #kalau seperti ini brrti semua gps di class car bernilai true. tidak bisa custom

mobil1 = mobil('pink',4)
car1 = car('black',8)

print(mobil1.warna,mobil1.seat)
print(car1.warna,car1.gps)
'''
# class mobil:
#     def __init__(self,warna,seat):
#         self.warna = warna
#         self.seat = seat
# class car(mobil): #inheritance
#     def __init__(self, soundSys):
#         self.soundSys= soundSys

# mobil1 = mobil('pink',4)
# car1 = car('black',8)

# print(mobil1.warna,mobil1.seat)
# print(car1.warna,car1.gps)
'''
#CARA CARA PEWARISAN SIFAT/INHERITANCE
class x:
    def __init__(self,nama,gelar):
        self.nama =nama
        self.gelar = gelar
# class y(x):
#     def __init__(self,nama,gelar):
#         x.__init__(self,nama,gelar)
# class y(x):
#     pass
class y(x):
    def __init__(self,nama,gelar):
        super().__init__(nama,gelar) #super untuk mengembalikan ke parents
objx= x('andi','prof')
objy = y('caca','Dr')
print(objx.nama)
print(objy.gelar)
'''
'''
class x:
    def __init__(self,nama,gelar):
        self.nama =nama
        self.gelar = gelar
class y(x):
    def __init__(self,nama,gelar,univ):
        super().__init__(nama,gelar)
        self.kampus = univ

objx= x('andi','prof')
objy = y('caca','Dr','UNDIP')
objz = y('simba','S.T','UGM')
print(objx.nama)
print(objy.kampus)

objy.warna ='merah' #hanya untuk menammbahkan/modif objek nya saja. bukan di class parent nya
objz.usia = 23
setattr(objz,'alamat','BSD') #untuk menambahkan/modif objek juga
delattr(objz,'alamat') #hanya untuk menghapus objek tambahan bukan yang di class parent nya

print(hasattr(objy,'warna'))
print(hasattr(objy,'usia'))

# print(getattr(objy,'nama')) #cara lain pemanggilan objek
from pprint import pprint
pprint(vars(objy)) #outputnya berupa dictionary
print(vars(objy))
print(vars(objz))
'''

# class Z:
#     nama = 'Z'
#     usia = '22'

# objZ= Z()
# print(objZ.nama)
# del Z.nama #menghapus nama yang ada di class
# print(objZ.usia)
'''
class student:
    def __init__(self,nama,usia):
        self.nama = nama
        self.usia = usia
data= [{'nama':'Andi','usia':'21'},
{'nama':'Budi','usia':'21'},
{'nama':'Caca','usia':'21'},
{'nama':'Deni','usia':'21'},
]

def createObj(x):
    nama=x['nama']
    vars()[nama] = student(x['nama'],x['usia'])
    return vars()[nama]
def createObj(x):
    return student(x['nama'],x['usia'])

dataNew = list(map(lambda x:student(x['nama'],x['usia']),data))
print(dataNew[0].nama)
print(dataNew[0].usia)


nama = 'ultraman'
vars()[nama]=12345
# ultraman = 12345
print(ultraman)
'''
'''
# untuk persegi, luas persegi => sisi

class persegi:
    def __init__(self,sisi):
        self.sisi = sisi
        self.keliling= self.sisi *4
        self.luas = self.sisi **2

persegiA= persegi(4)
persegiB= persegi(5)
persegiC= persegi(6)

print(vars(persegiA))
print(vars(persegiB))
print(vars(persegiC))
'''

# class keRomawi():
#     .....

# hasil berupa 
# keRomawi(1) = I
# keRomawi(2) =II

# dibatasi 3000