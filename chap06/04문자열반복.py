n=int(input())

for i in range(n):
    a,b = map(str,input().split())
    a=int(a)
    for i in b:
        print(i*a,end="")
    print()