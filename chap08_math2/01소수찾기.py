# https://www.acmicpc.net/problem/1978
prime = {}
for i in range(1001):
    prime[i] = 0
    if i % 2 != 0 and i >= 7:
        for j in range(3, i//2, 2):
            if i % j == 0:
                break
        else:
            prime[i] = 1
prime[2] = 1
prime[3] = 1
prime[5] = 1

arr = [1, 3, 5, 7]
answer = 0
for i in arr:
    if prime[i] == 1:
        answer += 1

print(answer)
