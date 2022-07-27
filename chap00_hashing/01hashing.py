# https://www.acmicpc.net/problem/15829
val = "z"
mod = 1234567891
answer = 0
for i in range(len(val)):
    a_i = ord(val[i]) - ord("a") + 1
    r_i = 31**(i)
    answer += (a_i * r_i)

print(answer % mod)
