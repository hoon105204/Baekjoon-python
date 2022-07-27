# https://www.acmicpc.net/problem/2581
m = int(input())
n = int(input())

val_sum = 0
val_min = 10001
for i in range(m, n+1):
    if i <= 1 or i == 4:
        continue
    for j in range(2,i//2):
        if i % j == 0:
            break
    else:
        val_sum += i
        val_min = min(val_min, i)

if val_sum == 0:
    print(-1)
else:
    print(val_sum)
    print(val_min)
