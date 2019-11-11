# string
print("jum'at")
print('jum\'at')
print('Simba kocheng \n manis') #enter
print('simba kocheng  \t manis') #tab
print(50*'=')
nama = 'simba'
usia=13
# bentuk penulisan lain fungsi print
print('saya %s usia %d'%(nama,usia)) #%s menunjukkan type string , %d menunjukkan type decimal
print('saya {} usia {}'.format(nama, usia))
print(f'saya {nama} usia {usia}')

print(60*'=')
nama = 'nalas binti simba'
print(nama.lower())
print(nama.upper())

print(60*'=')
x ='wkwkwkw'
print(x.islower()) #perintah boolean untuk mengecek apakah variable x  lower/upper, capital/tidaks
print(x.isupper())

print(60*'=')
print(nama.lower().isupper())
print(nama.upper().islower())
print(len(nama)) #menghitung jumlah karakter pada nama, spassi dihitung
print(len(nama)+7)
print(nama[0:16])
print(nama[6:])
# [start : stop : step]
print(nama[9 : len(nama) :2])
print(nama.index('s')) #untuk cek huruf S index ke berapa
print(60*'=')
# menghitung jumlah huruf tanpa spasi
print(len(nama.replace(' ',''))) #'(spasi)' di replace dengan '(tanpa spasi)'
print(len(nama))
print(60*'=')
# jumlah huruf c
print(nama.count('s'))

# jumlah kata Simba
print(nama.count('simba'))