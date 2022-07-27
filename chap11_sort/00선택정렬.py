# 선택정렬
# 가장 작은 데이터를 선택해 맨앞과 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두번째와 바꾸고 ....

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i
    for j in range(i+1,len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)