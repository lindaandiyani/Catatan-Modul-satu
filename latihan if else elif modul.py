# angka = int(input('masukkan angka berapapun disini :'))

# if angka % 2 == 0 :
#     print(angka, 'adalah bilangan Genap')
# else :
#     print(angka,'adalah bilangan Ganjil')



print(60*'=')
Massa = int(input('masukkan Berat Badan anda disini dalam kg :'))
Tinggi = int(input('masukkan Tinggi Badan anda disini dalam cm :'))
print ('massa ',Massa,'kg',' & tinggi anda ',Tinggi,'cm')
IMT = Massa / (Tinggi/100)**2

if IMT < 18.5 :
    print('IMT = ',IMT,', Berat Badan anda KURANG')
elif 18.5 <= IMT <= 24.9:
    print('IMT = ',IMT,', Berat Badan anda IDEAL')
elif 25.0 <= IMT <= 29.9:
    print('IMT = ',IMT,', Berat Badan anda BERLEBIH')
elif 30.0 <= IMT <= 39.9:
    print('IMT = ',IMT,', Berat Badan anda SANGAT BERLEBIH')
else:
    print('IMT = ',IMT,', anda OBESITAS')



