# https://www.acmicpc.net/problem/14425
import sys

my_set = {}

n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    string = sys.stdin.readline().strip()
    my_set[string] = 1

cnt = 0
for _ in range(m):
    val = sys.stdin.readline().strip()
    try:
        if my_set[val] == 1:
            cnt += 1
    except:
        continue

print(cnt)