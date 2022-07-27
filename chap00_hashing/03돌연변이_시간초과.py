# https://www.acmicpc.net/problem/10256
def hashing(val):
    mod = 1234567891
    res = 0
    for k in range(len(val)):
        a_k = ord(val[k]) - ord("A") + 1
        r_k = 31 ** k
        res += (a_k * r_k)

    return res % mod

DNA = "ATGGAT"
marker = "AGGT"
dict1 = {}
answer = 0
for i in range(len(marker)):
    for j in range(i+1, len(marker)):
        tmp = marker[:i] + "".join(sorted(marker[i:j+1], reverse=True)) + marker[j+1:]
        dict1[hashing(tmp)] = 1

for i in range(len(DNA)):
    try:
        if dict1[hashing(DNA[i:i+len(marker)])] == 1:
            answer += 1
    except:
        continue

print(answer)



