def sumofSquares(n):
    import math
    r=int(math.sqrt(n))
    for i in range(r,-1,-1):
        l=[(i**2 + (x)**2) for x in  range(r-1,-1,-1)]
        if n in l:return True
    return False  


s=int(input())
print(sumofSquares(s))
