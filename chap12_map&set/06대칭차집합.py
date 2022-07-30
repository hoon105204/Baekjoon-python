# https://www.acmicpc.net/problem/1269
import sys

n, m = map(int, sys.stdin.readline().split())
set1 = set(map(int, sys.stdin.readline().split()))
set2 = set(map(int, sys.stdin.readline().split()))

print(len(set1 ^ set2))

