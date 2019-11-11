nama= ' Hari ini hari tidak masuk sekolah'

# jumlah huruf h
cari = 'H'
x = nama.upper().replace(cari.upper(),'')
print(x)

jumlahcari= len(nama)-len(x)
print('jumlah huruf a adalah',jumlahcari)

print(60*'=')
kalimat= 'Hari ini Hari tidak masuk sekolah'
found = 'hari'
y=kalimat.lower().replace(found.lower(),'')
print(y)
jmlfound= (len(kalimat) - len(y)) / len(found)

print(jmlfound)


# jmlcari= int((len(nama)-len(x))/len(cari))
# print('jumlah kata',cari, 'ada', jmlcari)

