# https://www.acmicpc.net/problem/11478
import sys

s = sys.stdin.readline().strip()
my_set = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        my_set.add(s[i:j+1])

print(len(my_set))
