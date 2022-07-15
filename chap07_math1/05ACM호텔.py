import math
import sys

T = int(sys.stdin.readline())
for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    y = math.ceil(N / H)
    if N % H == 0:
        x = H
    else:
        x = N % H
    print(str(x) + str(y).zfill(2))
