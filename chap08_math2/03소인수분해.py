# https://www.acmicpc.net/problem/11653
n = int(input())

arr = []
if n != 1:
    while True:
        for i in range(2, n//2+1):
            if n % i == 0:
                arr.append(i)
                n = n // i
                break
        else:
            arr.append(n)
            n = 1
        if n == 1:
            break
    arr.sort()
    for j in arr:
        print(j)

