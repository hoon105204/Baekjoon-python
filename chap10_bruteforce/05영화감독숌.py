# https://www.acmicpc.net/problem/1436
tmp = {}
cnt = 1
num = 666
n = int(input())
while True:
    if cnt > n:
        break
    if "666" in str(num):
        tmp[cnt] = num
        cnt += 1
    num += 1

print(tmp[n])


