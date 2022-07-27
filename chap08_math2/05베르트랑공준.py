# https://www.acmicpc.net/problem/4948
import sys


def prime_list(n):
    sieve = [True] * (2*n + 1)
    sieve[0] = False
    sieve[1] = False

    m = int((2*n) ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:  # i가 소수인 경우
            for j in range(i + i, 2*n + 1, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    return [i for i in range(n+1, 2*n+1) if sieve[i]]


while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break
    else:
        print(len(prime_list(num)))
