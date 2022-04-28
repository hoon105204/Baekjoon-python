N = float(input())
myList=list(map(float,input().split()))
maxNumb = max(myList)

ans=0
for i in myList:
    ans+=i/maxNumb*100/N
    
print(ans)
    
