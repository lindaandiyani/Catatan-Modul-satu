import datetime as dt
x = dt.datetime.now()

print(x)
print(x.strftime('%d')) #tanggal
print(x.strftime('%A')) #hari
print(x.strftime('%m')) #bulan
print(x.strftime('%B')) #nama bulan
print(x.strftime('%Y')) #th

print(x.strftime('%H')) #24 jam
print(x.strftime('%I')) #12 jam
print(x.strftime('%p')) #am/pm
print(x.strftime('%M')) #min
print(x.strftime('%S')) #sec

print(x.strftime('%c'))
print(x.strftime('%x'))
print(x.strftime('%X'))

print(x.strftime('Sekarang jam %A'))
print(x.strftime('Sekarang jam %H:%M:%S WIB'))

'''
file py ==> class/objek

waktu... kalau diketik waktu.hari/tanggal,bulan,tahun,jam,menit,detik output
'''