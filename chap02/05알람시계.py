a,b = map(int,input().split())
if b<45:
    if a==0:
        b=60-(45-b)
        print("%d %d"%(23,b))
    else:
        a-=1
        b=60-(45-b)
        print("%d %d"%(a,b))
else:
    b=b-45
    print("%d %d"%(a,b))