# https://www.acmicpc.net/problem/2798
import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

answer = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if arr[i]+arr[j]+arr[k] <= m:
                answer = max(answer, arr[i]+arr[j]+arr[k])
print(answer)
