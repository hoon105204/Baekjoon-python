# https://www.acmicpc.net/problem/13305
n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr2.pop()

answer = 0
tmp = 0
val_min = arr2[0]
for i in range(len(arr1)):
    if val_min > arr2[i]:
        answer += val_min*tmp
        tmp = arr1[i]
        val_min = arr2[i]
    else:
        tmp += arr1[i]
if tmp != 0:
    answer += val_min*tmp

print(answer)