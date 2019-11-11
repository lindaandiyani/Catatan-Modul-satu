# list
#dalam list bia dimasukkan macam macm tipe data, string, intt, bool dkk)
# penulisan list menggunakan []

x= ['andi','budi','suci',123, True]
print(type(x[-1]))

print(50*'=')

hari =['senin', 'selasa','rabu','kamis','jumat','sabtu','minggu']

now = 'senin'
x= int(hari.index(now))
brbhari= -1

# future = brbhari % 7
# a=future+x
# print(hari[a])

print(hari[((brbhari%len(hari))+x)%7]) #len adalah jumlah hari dalam list #COBA NNTI CARI TAHU LAGI URUTANNYA UNTUK DIKASIH %7 DIAKHIR

print('senin' in hari)
print(hari.index('senin'))
print(hari.count('senin'))

hari [0] = 'monday' #= seperti fungsi replace
hari.append("senin2") #menambah list dan otomatis berada diindex terakhir
hari.insert(6,'senin3') #menambahkan(menyisipkan) anggota list pada index ke 6, bbrtti anggota dibelakngnya akaan mundur
hari.remove('senin2') #menghilangkan elemen menggunakan value
hari.pop() #menghilangkan anggota list terakhir
hari.pop(0) #menghilangkan elemen menggunakan indeks
# hari.clear() #menghilangkan semua elemen dari list
hari.sort() #mengurutkan elemen list berdasarkan abjad by KONTEN /value
hari.sort(reverse = True) #---- jika tidak ada keterangan reverse true maka defaultnya False
hari.reverse() #sorting by index / ngebalik
hari= hari[:-1] #==ngebalik manual
print(hari)


print (60*'=')

a = 'ankhg'
print(list(a))

print(60*'=')

#mengCopy elemen list
angka = [1,2,3,4,5,6,7,8,9]
c=angka[0::2].copy() #mengkopi angka ganjil
print(angka)

print(angka+c)
d= (1,2,3,4)
# print(dir(angka))
# print(dir(d))

e=(1,2,3)
f=(1,) #kaalau tanpa koma type datanya jadi integer maka harus ada koma  
print(type(e))







