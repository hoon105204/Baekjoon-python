# https://www.acmicpc.net/problem/7568
n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

for i in range(n):
    tmp = 1
    for j in range(n):
        if i != j and arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            tmp += 1
    print(tmp, sep=" ")

