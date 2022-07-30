import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []


stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)


print(*answer)


# <시간초과>
# import sys
# from collections import deque
#
# inp_num = int(sys.stdin.readline())
# mylist = deque(map(int, sys.stdin.readline().split() ))
# res = []
#
# for _ in range(inp_num):
#     val = mylist.popleft()
#
#     if not mylist:
#         res.append(-1)
#         break
#
#     for i in mylist:
#         if i > val:
#             res.append(i)
#             break
#     else:
#         res.append(-1)
#
# print(*res)