# https://www.acmicpc.net/problem/1920
arr1 = [4, 1, 5, 2, 3]
arr2 = [1, 3, 7, 9, 5]
dic1 = {}
for i in arr1:
    dic1[i] = 1

for j in arr2:
    try:
        print(dic1[j])
    except:
        print(0)