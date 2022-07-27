# https://www.acmicpc.net/problem/11047

n, k = 10, 4790
arr = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
arr.sort(reverse=True)
answer = 0

for i in arr:
    answer += k//i
    k -= (k//i)*i

print(answer)