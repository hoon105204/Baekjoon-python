# https://www.acmicpc.net/problem/1764
import sys

n, m = map(int, sys.stdin.readline().split())
set1 = set(sys.stdin.readline().strip() for _ in range(n))
set2 = set(sys.stdin.readline().strip() for _ in range(m))

arr = []
for val in set1 & set2:
    arr.append(val)

arr.sort()
print(len(arr))
for val in arr:
    print(val)
