class X:
    def __init__(self,name,age):
        self.nama = name
        self.usia = age
    def pensiun(self):
        return 55-self.usia

class Y(X): #inheritance
    def __init__(self,name,age,city):
        X.__init__(self,name,age)
        self.kota= city



objX = X('Andi',22)
print(objX.pensiun())
objY = Y('Budi',23,'jakarta')
print(objY.kota)

