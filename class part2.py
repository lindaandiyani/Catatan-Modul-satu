'''
# penamaan class sebaiknya diawali dengan huruf kapital
# class orang :
#     nama ='budi'

class manusia:
    def __init__(self,nama):
        self.nama = nama
class Pria(manusia):
    def __init__(self,nama):
        manusia.__init__(self,nama)
        self.gender = 'laki-laki'
class Wanita(manusia):
    def __init__(self,nama):
        self.gender = 'perempuan'

objA = manusia('andi')
objB = Pria('andi')
objC = Wanita('Andi')
print(vars(objA))
print(vars(objB))
print(vars(objC))

# multilevel inheritance

class X: 
    def __init__(self,x):
        self.x = x
class Y(X):
    def __init__(self,x,y):
        X.__init__(self,x)
        self.y = y
class Z(Y):
    def __init__(self,x,y,z):
        Y.__init__(self,x,y)
        self.z = z

objZ = Z('andi','PNS',True)
print(vars(objZ))

# Multiple inheritance

class Karnivora:
    def __init__(self):
        self.daging= True

class Herbivora:
    def __init__(self):
        self.tumbuhan = True
class Omnivora(Karnivora,Herbivora):
    def __init__(self):
        Karnivora.__init__(self)
        Herbivora.__init__(self)
        self.mcD = True

objectA= Omnivora()
print(vars(objectA))
'''
class Karnivora:
    def __init__(self):
        self.daging= True
        self.nama = 'Karnivora'

class Herbivora:
    def __init__(self):
        self.tumbuhan = True
        self.nama = 'Herbivora'
class Omnivora(Karnivora,Herbivora):
    def __init__(self):
        Karnivora.__init__(self)
        Herbivora.__init__(self)
        self.mcD = True
        self.nama = 'Omnivora'
# ada dua parameter nama di karnivora dan omnivora,
#  yang muncul yang di herebivora karna yang dipanggil terakhir di class omnivora 
# tapi misal diclass omnivora dipanggil lagi nama brrti yang muncul yaa omnivora
objectA= Omnivora()
print(vars(objectA))