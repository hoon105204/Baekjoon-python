# 카운트 정렬
import sys

N = int(sys.stdin.readline())
ans = [0]*10001

for _ in range(N):
    ans[int(sys.stdin.readline())] += 1

for i in range(10001):
    for j in range(ans[i]):
        print(i)

# 메모리 많이 먹음
# for i in range(10001):
#     sys.stdout.write(('{}\n'.format(i))*ans[i])
