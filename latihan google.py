# # def pangkatDua(angka):
# #     return str(angka**2)

# # print(pangkatDua(5))

# n=int(input('input angka:'))
# if n%2 ==0 and 2<= n <=5:
#     print('not weird')
# elif n%2==0 and 6 <= n <=20:
#     print('Weird')
# elif n%2 ==0 and n >20:
#     print('not weird')
# else:
#     print('Weird')



# print(fibonacci(9))
# a=0
# b= 1
# c=0
# for i in range(10):
#     print(a)
#     c=a+b
#     a=b
#     b=c
    
angka = int(input('masukkan angka :'))

if angka>1 :
    for i in range(2,angka):
        if angka % i ==0:
            print(f'{angka} bukan biangan prima')
            print(f'{i}/ dengan{angka/i} = {angka}' )
            break
        else:
            print('bilangan prima')
            break
else:
    print('bukan bilangan prima')

# fibonacci = int(input('ketikkan angka disini :'))
# a= 0 #angka pertama
# b= 1 #angka kedua
# c=0 #hasil Awal
# for i in range(fibonacci):
#     print(a)
#     c=b+a
#     a=b
#     b=c


# import time;
# localtime = time.asctime(time.localtime(time.time()))
# print('waktu local saat ini :',localtime)

