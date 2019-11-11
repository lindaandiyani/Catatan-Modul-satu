x = input('ketikkan huruf random: ')
def cekKapital(x):
    hasil =''
    for i in x:
        if i.islower() :
            hasil += i.upper()
        else:
            hasil+= i.lower()
    print (hasil)
    return hasil


cekKapital(x)

