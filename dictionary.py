# dictionary 
#bisa mengubah value didalam dictionary

andi = {
    'name' : 'andi',
    'age' : '22',
    'is_married' : False,
    'cars' : ['alphard', 'xpander','innova'],
    'address' : {
        'street' : 'mawar',
        'RT' : 5, 'RW' : 123, 'kecamatan' : 'x',
        'zipcode' : 12345,
        'geo' :{
            'lat' : 111.11,
            'lng' : 123.45
        }
    }

}


# print(andi['name']) #dalam dictionry yang disearch value bukan index
# print(andi['age'])
# print(andi['is_married'])

print(andi.get('name'))
print(andi.get('age'))

# print(andi.get('job', 'maaf andi belum memiliki pekerjaan')) #keluarnya none bukan eror jadi bisa diganti
# print(andi['job']) #keluarnya bakalan eror

andi ['name'] = 'budi'


andi['salary'] = 23000000
andi.update({'no_ktp':123456789})

print(60*'=')
x = {1:True, 2: False}
print(list)


# print(list(andi)) #tapi  hanya key nya saja value tidak tersertakan
# print(andi.keys()) #untuk mengeluarkan keys/properi/atribut
# print (andi.values()) #untuk menngeluarkan values... ini bisa diubah kedalam list


# print(andi['address']['geo'])
# print(andi)

days = {
    'senin' : 'monday', 'selasa' : 'Tuesday','rabu' : 'wednesday',
    'kamis':'Thursday','jumat':'Friday','sabtu':'saturday','minggu':'sunday'
}

# hari = (input('ketik nama hari :'))
# inggris = list(andi.values())
# print('bahasa inggrisnya',hari.upper(),'=', days.get(hari.lower(), 'ga ada!'))
# print(inggris)
# print('bahasa indonesianya',hari.lower(),'=', days.values()[hari.lower()])

hari = list(days)
day = list(days.values())
x = input('ketikan nama hari (ENG/IDN):')

if x.lower() in hari :
    engHari = day[hari.index(x.lower())]
    print('bahasas inggrisnya',x,'adalah',engHari)
else:
    idDay = hari[day.index(x.lower())]
    print('bahasa indonesia',x.lower(),'adalah',idDay)





