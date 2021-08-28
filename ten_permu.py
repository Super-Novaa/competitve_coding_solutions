from itertools import permutations
a,l,s='0123456789',[],0
m=[''.join(p) for p in permutations(a)]
m=list(map(int,m))
for i in range(0,int(input())):l.append(int(input()))
for j in l:s+=m[j-1]
print(s)