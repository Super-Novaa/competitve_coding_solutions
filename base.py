def base(n):
    r=[]
    if n==0:return 0
    else:
        q=n/6
        while q!=0:
            q=n//6
            re=n%6
            r.append(re)
            n=q
    return sum(r)
t=int(input())
v=[]
l=list(map(int,input().split(',')))
for i in l:
    v.append(base(i))
c=0
for j in range(len(v)-1):
    for k in range(j+1,len(v)):
        if v[j]>v[k]:c+=1
print(c)
