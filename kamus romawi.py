# angkaInput = 498

def cekSatuan(angkaInput):
    if angkaInput <= 3:
        hasil ='I'* angkaInput
    elif angkaInput == 4:
        hasil='IV'
    elif angkaInput == 5:
        hasil='V'
    elif 6 <= angkaInput <= 8:
        hasil='V'+('I'*(angkaInput-5))
    else:
        hasil='IX'
    return hasil
 
def cekPuluhan(angkaInput):
    pangkat = angkaInput//10
    if angkaInput <= 30:
        hasil = 'X'* pangkat
    elif angkaInput== 40:
        hasil = 'XL'
    elif angkaInput== 50:
        hasil= 'L'
    elif 60 <= angkaInput <= 80:
        hasil='L'+('X'*((angkaInput-50)//10))
    else:
        hasil='XC'
    return hasil
def cekRatusan(angkaInput):
    pangkat = angkaInput//100
    if angkaInput <= 300:
        hasil = 'C'* pangkat
    elif angkaInput== 400:
        hasil = 'CD'
    elif angkaInput== 500:
        hasil= 'D'
    elif 600 <= angkaInput <= 800:
        hasil='D'+('C'*((angkaInput-500)//100))
    else:
        hasil='CM'
    return hasil
def cekRibuan(angkaInput):
    pangkat = angkaInput//1000
    if angkaInput < 4000:
        hasil = 'M'* pangkat
    return hasil
def semuaPuluhan(angkaInput):
    definAngka = angkaInput%10
    satuanpuluhan = cekSatuan(definAngka)
    selisih = (angkaInput-definAngka)
    hasil =cekPuluhan(selisih) + satuanpuluhan
    return hasil 
def semuaRatusan(angkaInput):
    definangka = angkaInput%100
    puluhanratusan = semuaPuluhan(definangka)
    selisih = (angkaInput-definangka)
    hasil = cekRatusan(selisih)+puluhanratusan
    return hasil
def semuaRibuan(angkaInput):
    definAngka = angkaInput%1000
    ratusanribuan = semuaRatusan(definAngka)
    selisih = (angkaInput-definAngka)
    hasil = cekRibuan(selisih)+ratusanribuan
    return hasil

    
def cekRomawi(angkaInput):
    panjangAngka = len(str(angkaInput))
    hasil=''
    if panjangAngka == 1:
        hasil = cekSatuan(angkaInput)
    elif panjangAngka ==2:
        hasil = semuaPuluhan(angkaInput) 
    elif panjangAngka ==3:
        hasil = semuaRatusan(angkaInput)
    elif panjangAngka ==4:
        hasil = semuaRibuan(angkaInput)
    else:
        hasil= 'angka belum bisa terdefinisi'
    return hasil
        
            
print(cekRomawi(3879))
     

        
