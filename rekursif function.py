# def pangkatB(x,y):
#     if (y==1):
#         return x
#         else:
#             return x * pangkatB(x,y-1)
# print(pangkatB(2,3))

'''
pangkatB(2,3) = 2*pangkatB(2,2)      2*4 =8
pangkatB(2,3) = 2*pangkatB(2,1)      2*2 =4
pangkatB(2,3) = 2*pangkatB(2,0)      2*1 =2
'''

# rekursif adalah memanggil fungsi didalam fungsi

def faktorial(x):
    angka =1
    for i in range(1,x+1):
        angka *= i
    return angka

    
print(faktorial(3))

def faktorial2(x):
    if x <=2:
        return x
    else:
        return x*faktorial2(x-1)
print(faktorial2(5))