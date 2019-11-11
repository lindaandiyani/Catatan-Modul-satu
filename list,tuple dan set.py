x =[(1,['a','b','c'],3),
    (4,5,6)

]
x[0][1][2] ='andi' #semua yang ada di list bisa di ubah/diedit untuk tuple hanya bisa di count sama index
x[0][1].append('d')
print(x)

y=(1,2,3,)
# print(dir(y))

a= [1,2,3,1,2,3]
b= (1,2,3,1,2,3)
print(60*'=')

# SET/HIMPUNAN
# 1. no indexing
#  2. duplicate element not allowed
#  3. set mutable, tapi elemen2nya immutable

c = {1,2,3,1,2,3}
# c['2'] = 'budi' #ini tidak bisa
c.add('a') #menambahkan satu elemen saja. coba lihat beda outputnya
c.add(('c','d','e')) #ketika diprint set c urutannya akan acak karena indexing tidak berpeagruh
c.update('andi')
c.update([6,7,8])
c.update({'z','budi'})

print('budi' in c) #cek apakah ada didalama element
c.remove('budi') #menghilangkan budi
c.discard('linda') #jika men-discard sesuatu yang tidak ada diset tidak akan eror, berbeda dgn remove

print(c)
c.pop() #sepertinya menghilangkan elemen paling depan
# c.clear() #set masih ada tapi elemennya ksong
# del.c #menghilangan set
print(c)
# print(list(set(a))) #untuk mengubah list/tuple kedalam set bisa begtupun sebaliknya

print (60*'-')
a= list('abcdef')
b= list('bcdfgh')

a=set(a)
b=set(b)

print(a.intersection(b)) #irisan
print(b.intersection(a))
print(a & b) #irisan juga
print(b & a)

print(a.union(b)) #gabungan
print(b.union(a))
print(a | b) #gabungan
print(b|a)

print(a.difference(b)) #selisih anggota set A yang tidak ada di B
print(b.difference(a))
print(a - b )
print(b - a)


print(a.symmetric_difference(b)) #kebalikan dari irisan. anggotanya semua anggota a dan b kecuali irisan
print(b.symmetric_difference(a))
print(a^b) 
print(b^a)

# FROZEN SET
x = set([1,2,3])
y = frozenset([1,2,3])

x.remove(2)
# y.add(2)
print(x)
print(y)
