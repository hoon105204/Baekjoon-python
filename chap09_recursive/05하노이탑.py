def hanoi(n, start, end, via):
    if n == 1:
        return [start, end]
    else:
        return hanoi(n-1, start, via, end) + hanoi(1, start, end, via) + hanoi(n-1, via, end, start)

num = int(input())
array = hanoi(num, 1, 3, 2)
ans = int(len(array)/2)
print(ans)
for i in range(0,len(array),2):
    print('{} {}'.format(array[i],array[i+1]))