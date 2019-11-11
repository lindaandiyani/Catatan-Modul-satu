# if 

# if (condition) :
    # (program ) ;

# = assign value
# == sama dengan

x= 60
if x < 80 :
    print('anda lulus !')
elif x < 40 :
    print('anda tidak lulus')
else :
    print('anda remidial')

# jomblo = False
# # if jomblo == False #karena ini boolean maka bisa ditulis seperti dibawah ini
# if jomblo :
#     print('anda jomblo')

# else :
#     print('Anda taken')



jomblo = True; nganggur = True

if jomblo == True and nganggur == True:
    print('anda jmblo pengangguran')
elif jomblo == True and nganggur == False:
    print('anda kurang piknik')
elif jomblo == False and nganggur == True:
    print('anda bucin')
else:
    print('Anda OK')

# bisa disingkat seperti
jomblo = True; nganggur = True

if jomblo and nganggur :
    print('anda jmblo pengangguran')
elif jomblo and not nganggur:
    print('anda kurang piknik')
elif not jomblo and nganggur :
    print('anda bucin')
else:
    print('Anda OK')


# condition
x = True; y = False
print ( x and y) #and bernilai true 2 2 nya harus bernilai true
print (x or y) #berniali true jika salah satu kondisi terpenuhi


# equation

# comparision