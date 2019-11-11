p = {1,2,4,7,9,19}
q = {5,12,16,17,7,9,19,6}
r = {3,8,6,19}

print (p.intersection(q))
print(p.intersection(q).intersection(r))

print(60*'=')

p = {-4,-3,-2,-1,0,1,2,3,4}
q = {-7,-6,-5,-4,-3,-2,-1,0,1}
r ={-1,0,1,2,3,4,5,6,7}
# s = {-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9}

print (p.union(q))
print(p.union(r))
print(q.union(r))

print(list(p.union(q)))
# print((p.union(q).sort)) ini tidak bisa. kebacanya massih yang set

print(60*'=')

S = {0,1,2,3,4,5,6,7,8,9,10}
A = {3,5,7}
B = {5,7,9} 

print ('irisan dari A dan B :',A.intersection(B))
print ('gabungan dari A dan B :', A.union(B))
print(' A irisan  A gabungan B ', A.intersection(A.union(B)))
print('B irisan  A gabungan B',B.intersection(A.union(B)))
print ((A.union(B).intersection(A.union(B))))
print ((A.intersection(B)).union(A.union(B)))