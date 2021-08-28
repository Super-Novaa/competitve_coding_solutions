n=int(raw_input())
mon=0
l=list(map(int,raw_input().split(' ')))

if n <=5:
    mon=sorted(l)[-1] + sorted(l)[-2]
    
else:
    c,m=l,max(l)
    ind=[]
    for i in range(2):
        ind.append(l.index(max(c)))
        mon+=l[ind[i]]
        l[ind[i]]=0
        del(c[c.index(max(c))])
    while(len(c)>0):
        m=max(c)
        if min([abs(l.index(m)-j) for j in ind ])>=4:
            mon+=m
            ind.append(l.index(m))
            del(c[c.index(m)])
        else:
            del(c[c.index(m)])
print mon
