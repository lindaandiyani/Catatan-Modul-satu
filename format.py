# print(format(+123,'+9'))
# print(format(.6,'8.2%'))
# print(format(12345678.1234, '.2f')) #tidak ada penunjuk atau pembeda ribuan
# print(format(1234589.3456,',.2f'))

# print(24,25)
# print('%s'%'hai')

# print('%10d',567)
# print('%-5d',567)
# print('%+10d',567)
# import math
# jariJari= int(input('masukkan jari-jari :'))
# luasLingkaran = math.pi*(jariJari**2)
# print('luas lingkarang dengan jari- jari',jariJari,'adalah : ',format(luasLingkaran,'.2f'))

# daftarNama=['anwar Suadi','ahmad jazzuli','safitri','edi junaedi',
# 'dian anggraeni','rahmat anwari']
# dicari= input('penggalan nama yang ingin anda cari :')
# index = 0
# ditemukan= False
# while index <len(daftarNama):
#     if dicari in daftarNama[index]:
#         ditemukan = True
#         break
#     index +=1
# if ditemukan:
#     print('nama lengkap nya adalah',daftarNama[index])
# else:
#     print('nama yang anda cari tidak ditemukan')

# angka == 1
# for angka in range(12):
#     print( angka,' ',angka**2)
#     i+=1 
for i in range(2,14,2):
    i%2==0
    print(i,' ',i**2)
    
n = 100
while n>0:
    print(n)
    n-=10

m = 2
while m>10:
    print(m)
    m-=2
    if m ==5:
        break

# y = 6
# x= 8-y
# if  x>0:
#     pass
# else:
#     print('hai')

y= 6
while y<18:
    if (y>10) and (y<15):
        y=y+1
        print(y)
        continue
    print(y)
    y+=2

for i in range(2,40,2):
    print(i,' ',i+i)


    