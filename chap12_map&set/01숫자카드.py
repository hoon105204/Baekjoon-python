# https://www.acmicpc.net/problem/10815
import sys

my_map = {}

num1 = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))

for val in arr1:
    my_map[val] = 1

num2 = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

for val in arr2:
    try:
        print(my_map[val])
    except:
        print(0)
