# https://www.acmicpc.net/problem/11399
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
answer = 0
for i in range(len(arr)):
    answer += arr[i]*(len(arr)-i)

print(answer)