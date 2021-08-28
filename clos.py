def wellbracketed(s):
    a=s.count('(')
    b=s.count(')')
    if a==b:return True
    else:return False

sr=input()
print(wellbracketed(sr))
