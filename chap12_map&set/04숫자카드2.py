# https://www.acmicpc.net/problem/10816
import sys

n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

my_dict = {}

for val in arr1:
    if my_dict.get(val) is None:
        my_dict[val] = 1
    else:
        my_dict[val] = my_dict.get(val) + 1

for val in arr2:
    ans = my_dict.get(val)
    if ans is not None:
        print(ans, end=" ")
    else:
        print(0, end=" ")


# from collections import Counter
# from sys import stdin
# _ = stdin.readline()
# N = stdin.readline().split()
#
# _ = stdin.readline()
# M = stdin.readline().split()
#
# C = Counter(N)
#
# print(' '.join(f'{C[m]}'if m in C else '0' for m in M))