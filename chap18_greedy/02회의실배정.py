# https://www.acmicpc.net/problem/1931
arr = [(1, 4), (3, 5), (0, 6), (5, 7),  (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
arr.sort(key=lambda x: (x[1], x[0]))
print(arr)
ans_arr = []
for i in arr:
    if not ans_arr:
        ans_arr.append(i)
        continue
    if i[0] >= ans_arr[-1][1]:
        ans_arr.append(i)
print(len(ans_arr))
