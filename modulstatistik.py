# listX = [1,3,9,2,6,4,5,7,8,5]
from functools import reduce

class Statistik:
    def ratarata(self, x):
        total = reduce(lambda a,b: a+b,x)
        return total
    def nilaiTengah(self,x):
        x.sort()
        if len(x)%2 !=0:
            iTengah = list(int(len(x)/2))
        else:
            iTengah= [int(len(x)/2)-1,int(len(x)/2)]
        return iTengah
        aTengah = list(map(lambda a: x[a],iTengah))
        total = reduce(lambda x,y: x+y,aTengah)
        return total/len(aTengah)
    def seringMuncul(self,x):
        x.sort()
        y= list(set(x))
        out= list(map(lambda a: x.count(a),y))
        maksimum = max(out)
        indexMaximum = out.index(maksimum)
        modus = y[indexMaximum]
        return modus
objekA = Statistik()
print(objekA.ratarata([1,2,3,4,5,6,7,8,9,10]))
print(objekA.nilaiTengah([1,2,3,4,5,6,7,8,9,10]))
print(objekA.seringMuncul([1,2,3,4,5,6,7,8,9,10,5]))
# saya= (reduce(lambda a,b: a+b,listX))/len(listX)
# print(saya)
