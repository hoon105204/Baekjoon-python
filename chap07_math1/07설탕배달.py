import sys

N = int(sys.stdin.readline())

# 4,7은 만들 수 없음
if N in [4, 7]:
    print(-1)
elif N in [3, 5]:
    print(1)
else:
    # 5로 나눴을 때 나머지에 따라 갯수
    res = N//5
    tmp = N%5
    if tmp == 0:
        print(res)
    elif tmp in [1,3]:
        print(res+1)
    else:
        print(res+2)

