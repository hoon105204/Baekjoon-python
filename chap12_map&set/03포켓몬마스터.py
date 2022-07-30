# https://www.acmicpc.net/problem/1620
import sys

my_dict = {}

n, m = map(int, sys.stdin.readline().split())
for i in range(n):
    val = sys.stdin.readline().strip()
    my_dict[str(i+1)] = val
    my_dict[val] = str(i + 1)

for _ in range(m):
    q = sys.stdin.readline().strip()
    print(my_dict[q])


