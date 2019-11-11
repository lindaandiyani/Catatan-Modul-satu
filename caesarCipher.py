alpabet = 'abcdefghijklmnopqrstuvwxyz'
inputan= input('masukkan pesanmu :')
loncatan = int(input('masukkan jumlah loncatan :'))
outputan =''
for i in range(len(inputan)):
    karakter = inputan[i]
    # print(karakter)
    location = alpabet.find(karakter)
    newLocation= (location+loncatan)%26
    outputan += alpabet[newLocation]
print(outputan)