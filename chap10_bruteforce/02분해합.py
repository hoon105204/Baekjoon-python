# https://www.acmicpc.net/problem/2231
import sys

n = int(sys.stdin.readline())

answer = 1000001
for i in range(n, max(0, n-100), -1):
    val = sum(map(int, list(str(i)))) + i
    if val == n:
        answer = min(answer, i)

if answer == 1000001:
    print(0)
else:
    print(answer)
