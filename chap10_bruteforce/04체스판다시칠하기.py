# https://www.acmicpc.net/problem/1018
m, n = map(int,input().split())
arr = []
for i in range(m):
    arr.append(input())

answer = 65
for i in range(m-7):
    for j in range(n-7):
        tmp = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x + y) % 2 == 0 and arr[x][y] != "B":
                    tmp += 1
                elif (x + y) % 2 == 1 and arr[x][y] != "W":
                    tmp += 1
        answer = min(tmp, 64-tmp, answer)

print(answer)
