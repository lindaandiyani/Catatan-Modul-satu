fibonacci = int(input('ketikkan angka disini :'))
a= 0 #angka pertama
b= 1 #angka kedua
c=0 #hasil Awal
for i in range(fibonacci+1):
    print(a)
    c=b+a
    a=b
    b=c
print(60*'=')
class Fibo:
    def Cek (self,fibo):  
        a=0
        b=1
        c=0
        for i in range(fibo-1):
            # print( a)
            c= a+b
            a=b
            b=c
            hasil= c
        return hasil
objX = Fibo()
# print('output')
print(objX.Cek(10))
# print(Fibo.Cek(4))



