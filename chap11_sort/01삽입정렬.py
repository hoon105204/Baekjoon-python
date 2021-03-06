# 삽입정렬
# 데이터를 확인하여 적절한 위치에 삽입
# (0,i-1)까지 정렬된 리스트에서 i번째 원소는 어디에 삽입되면 좋을지 확인

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
