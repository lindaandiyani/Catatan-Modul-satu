# fungsi --- embungkus sebuah program

def hello():
    print('hai Simba')

hello();

# f(x) = x^2
def kuadrat(angka):
    print(angka**2)

kuadrat(2);
kuadrat(4); 

# function dengan banyak variable
# def kuadrat1(angka1, angka2):
#     print(angka1**angka2)

# kuadrat1(
#     float(input('ketik angka pertama :')),
#     float(input('ketik angka kedua : '))
# )

def gangen(x):
    if x % 2 ==0 : #sama dengannya dua karena ini kondisi
        print(x,'bilangan Genap')
    else:
        print(x,'bilangan Ganjil')
gangen(99);



# def calc():
#     angka1 = int(input('masukkan angka pertama : '))
#     arit = input('masukkan operator aritmatika :')
#     angka2= int(input('masukkan angka kedua : '))
#     if arit == '/':
#         print(angka1/angka12 )
#     elif arit == '+':
#         print(angka1+angka2)
#     elif arit == '-':
#         print(angka1-angka2)
#     elif arit == '*':
#         print(angka1*angka2)
#     else:
#         print('operator belum diketahui')
# calc()
# memanggil variable diluar function BISA, jika ada variable didalam function dipanggil diluar. tidak bisa

students = ['andi','budi','caca']

# def tes(x):
#     print('caca' in x) #nama parameter bebas
#     print(x[0])
# tes(students);

def vokal (kalimat):
    kalimat= kalimat.lower().replace('a','o')
    kalimat= kalimat.lower().replace('i','o')
    kalimat= kalimat.lower().replace('u','o')
    kalimat= kalimat.lower().replace('e','o')
    print(kalimat)
vokal('nama')

def luaspersegi(sisi):
    print('Luas=',sisi*sisi)
def luaspersegireturn(sisi):
    return sisi*sisi
 #luaspersegireturn(5)= return ?
luaspersegi(4)
print(luaspersegireturn(5))

print(60*'=')
def ganjilgenap(angka):
    if angka % 2==0:
        return'Genap'
    else:
        return 'Ganjil'
print(ganjilgenap(30))

