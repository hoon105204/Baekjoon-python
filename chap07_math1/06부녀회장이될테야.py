# import sys
#
#
# def myfunc(k, n):
#     res = 0
#     for i in range(n):
#         if k == 1:
#             res += i + 1
#         elif k < 1:
#             return
#         else:
#             res += myfunc(k - 1, i + 1)
#     return res
#
#
# T = int(sys.stdin.readline())
# for _ in range(T):
#     k = int(sys.stdin.readline())
#     n = int(sys.stdin.readline())
#     print(myfunc(k, n))


t = int(input())

for _ in range(t):
    floor = int(input())
    num = int(input())
    f0 = [x for x in range(1, num+1)]
    for _ in range(floor):
        for i in range(1, num):
            f0[i] += f0[i-1]
        print(f0)  # 프린트문을 추가
    print(f0[-1])
