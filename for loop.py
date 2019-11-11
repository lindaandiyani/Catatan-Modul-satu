# kota = ['jakarta','bandung','surabaya']

# i= 0
# while i < len(kota):
#     print(kota[i])
#     i +=1

# for i in range(len(kota)):
#     print(kota[i])
# print(50*'=')
# for namaKota in kota:
#     print(namaKota)
# print(50*'=')
# x='purwadhika' #jika pada string maka akan di spell
# for i in x:
#     print(i)
# print(50*'=')
# for i in range(2,10,2):
#     print(i)
# else:
#     print('OK')


# for i in range(2,10):
#     print(i)
#     if i ==7:
#         break
#     print(i) 

# for i in range(2,10):
#     if i == 7:
#         continue
#     print(i)

# for i in range(1,11):
#     if i%2==0:
#         print('WOW')
#     print(i)

# def fizzBuzz(x):
#     for i in range (1,x+1):
#         if i%3==0 and i%5==0:
#             print('FizzBuzz')
#         elif i%5==0:
#             print('Buzz')
#         elif i%3==0:
#             print('Fizz')
#         else:
#             print(i)
# fizzBuzz(20)

# x=[1,2,3,4,5,6,7]
# # cara membalik list
# 1. x.reverse
# 2. print(x[::-1])
# 3. list(reversed(x))

y= ['Andi','Budi','Caca']
import math 
def balikan(y):
    for i in range(0,math.floor(len(y)/2)):
        x=y[i]
        y[i]=y[len(y)-1-i]
        y[len(y)-1-i]=x

print(balikan(y))

def balikan(y):
    for i in range(1):
        print(y[::-1])
        i-=1
balikan(y)

# def balikposisi(mylist):
#     hasil =[]
#     for i in range (len(mylist)):
#         hasil.insert(0,mylist[i])
#     return hasil
# print(balikposisi(y))

# print(60*'=')

# x= ['andi','budi','caca']
# y=[3,5,7,9]

# def balikPosisi (mylist):
#     for e in range(round(len(mylist)/2)):
#         asli = mylist[e]
#         mylist[e]= mylist[len(mylist)-1-e]
#         mylist[len(mylist)-1-e]=asli
#     return mylist
# print(balikPosisi(y))

# def ubahVokal(kata):
#     output=''
#     for huruf in kata:
#         if huruf in 'aiueo':
#             output=output+'o'
#         else:
#             output=output+huruf
#     return(output)
# print(ubahVokal('nama'))

# buat program cek poindrome
# kata= input('masukkan kata :').lower()
# kata2=kata[::-1]
# if kata == kata2:
#     print(True)
# else:
#     print(False)

# x= 'malam'
# def polindrome(kata):
#     if kata==kata[::-1]:
#         return True
#     else:
#         return False
# print(polindrome('kammbing'))

# def polindrome2(kata):
#     for i in range(round(len(kata)/2)):
#         polindromekah = False
#         if kata[i]==kata[len(kata)-1-i]:
#             polindromekah=True
#         else:
#             polimdromkah = False
#             break
#     return polindromekah
# print(polindrome2('katak'))
'''
TUGAS 
kalimat = 'hai aku simba'
dibalik per kata

translate kalimat => morse

Caesar Cipher positif
caesarCipher('lintang',2)=>Nkpvcpi
'''






