# lambda ==  digunakan didalam function, ekspresion nya pasti return
'''
x= lambda a:a
def y(a):
    return a

print(x(2))

x = lambda a,b,c :a+b+c
def z (a,b,c):
    return a+b+c

print(x(2,3,4))
print(z(2,3,4))

def myFunction(x):
    return lambda a:a**x

pangkat2 = myFunction(2) #2 adalah x
pangkat3 = myFunction(3)
pangkat4 = myFunction(4)

print(pangkat2(3)) #3 adalah a

x = lambda a: True if a % 2 == 0 else False
x= lambda a: 'Angka Genap' if a % 2 == 0 else 'angka Ganjil'

print(x(2))

# map python fungsi mengeksekusi function tertentu untuk setiap elemen dalam variable yang iterable

def y(a):
    return len(a)
a =['andi','caca','budi']

x = map(y,a)
# x= map(y, 'purwadhika')
print(x)
print(list(x))

a= ['coklat','melon','Nangka']
b= ['Apel','jeruk','Nanas']

def combi (a,b):
    return a+ ' '+b
x = map(combi,a,b)
print(x)
print(list(x)) 

x= [2,4,6,8,10]

def pangkat(a):
    return a**2
y = map(pangkat,x)
print(y)
print(list(y))

z= map(lambda a:a**2,x)
print(list(z))

def kurangLima(x):
    if x < 5:
        return False
    else: 
        return True
y = filter(kurangLima,x) #pada filter expression function nya harus berupa boolean
z= filter(lambda a: True if a>=5 else False,x)
print(list(z))
print(list(y))

a= pow(2,3)
b= pow (3,3)

print(a)
print(b)

z= list(map(pow,[2,3],[3,3]))
print(list(z))

x= [1,2,3,4,5]
y=[1,2,6,7,8]

z = list(filter(lambda a:a in x,y))
print(z)   

z= list(filter(lambda x: True if x<3 else False,x))
print(z)

z= list(filter(lambda x: x<3,x))
print(z)

angka = [1,2,3,4,5]
from functools import reduce
z = reduce(lambda x,y: x*y,angka)
print(z)

kata = ['ini','kucing','saya']
print(''.join(kata))

from functools import reduce #reduce seperti join
z= reduce(lambda x,y: x+y,kata)
print(z)

from math import pi #menginput bebarapa tools yang ada di math tanpa men import semua tools
print(pi)

angka = [1,2,3,4]

z= list(map(lambda x: x*2,filter(lambda x: x>3,angka)))
print(z)

z= list(filter(lambda x: x>3, map(lambda x: x*2,angka)))
print(z)
'''

def prima(x):
    a= False
    if x > 1:
        if x == 2:
            a= True
        else :
            for i in range(2,x):
                if x %i == 0:
                    a= False
                    break
                else:
                    a= True
    else:
        a= False
    return a
print(prima(2))

z = list (filter(prima,range(101)))
print(z)



# angka = list(range(101))
# # print(angka)

# genap= list(filter(lambda x: x % 2==0,angka))
# # print(genap)

# def dikalikanDua(a):
#     return a*2
# kaliDua= list(map(dikalikanDua,genap))
# print(kaliDua)

# from functools import reduce
# jumlahSemua= reduce (lambda a,y: a+y,kaliDua)
# print(jumlahSemua)