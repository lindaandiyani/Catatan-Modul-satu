listnum = [1,2,3,4,5,6]
listnum = [item * 2 for item in listnum]
print(listnum) 

newlist =[1,2,3,'a','b',3, 4,'f']
s = set(newlist)
print(s)
# a = list(s)[2]
# print(type(a))
print(type(list(s)[2]))

print (60*'=')

def times2 (num) :
    return num *2