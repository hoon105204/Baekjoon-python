i,j,k = map(int,input().split())
lis = [i,j,k]
lis.sort()
ans=0
if i==j==k:
    ans = 10000+(i*1000)
elif (i==j)or(i==k)or(j==k):
    ans = 1000+lis[1]*100
else:
    ans = lis[2]*100
    
print(ans)