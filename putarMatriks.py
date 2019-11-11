list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def putarMmatriks(list):
    hasil = []  
    for i in range(len(list)):
        kecil = []
        for j in range(len(list)):
            print(list[len(list)-j-1][i] ,  end='')
            a =(list[len(list)-j-1][i])
            kecil.append(a)
        print('')
        print(kecil)
        hasil.append(kecil)
    print(hasil)

    
    
putarMmatriks(list)

# k= 123
# print