# 삽입정렬

import sys

N = int(sys.stdin.readline())
mylist = []

for _ in range(N):
    mylist.append(int(sys.stdin.readline()))
print('mylist', '/', mylist)

for i in range(1, N):
    for j in range(i, 0, -1):
        if mylist[j] < mylist[j - 1]:
            mylist[j], mylist[j - 1] = mylist[j - 1], mylist[j]
        else:
            break
    print(i, '/', mylist)
