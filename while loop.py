# while loop (Selama kondisi terpenuhi jalankan program)

# i = 1
# while i<10:
#     print(i)
#     i+=1

# a =20
# while a >1:
#     print(a)
#     a-=1

# c =20
# while c >= 1:
#     print(c)
#     c -= 2 

# students = ['andi','budi','caca','deni']
# index = 0
# while index <=len(students)-1:
#     print(students[index])
#     index += 1

# x = [1,2,3,4,5,6,7,8,9,10]
# y= []
# index = 0
# while index <= len (x)-1:
#     if index == 4:
#         break #memotong looping sampai index ke 4
#     y.append(x[index]**2)
#     index += 1
# print(y)

# i = 1
# while i<10:
#     print(i)
#     if i == 5:
#         break #memotong looping
#     i +=1

# i=0
# while i<10:
#     i +=1
#     if i == 5:
#         continue #i == 5 diskip
#     print(i)

# password = '12345'
ketik =''
# while ketik != password:
#     ketik = input('ketikan password mu :')
#     if ketik != password:
#         print('password kamu salah !')
      
#     else:
#         print('password anda benar')

password = '12345'
inputuser = ''
jumlahinput = 0
batasinput= 5
lebih = False  

while inputuser != password and not lebih:
    if jumlahinput< batasinput:
        inputuser = input (f'input ke-  {jumlahinput +1} ketikkan password : ')
        jumlahinput +=1
    else:
        lebih = True
if lebih:
    print('kesempatan habis, tunggu 24 jam')
else:
    print('password anda benar')



        



    