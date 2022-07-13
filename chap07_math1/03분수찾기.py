# 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 
# 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

x = int(input())
i = 0
while True:
    i += 1
    if i*(i-1)/2 < x <= i*(i+1)/2 :
        head = int(i*(i+1)/2)-x+1
        foot = x - int(i*(i-1)/2)
        if i % 2 != 0:
            print('{}/{}'.format(head,foot))
            break
        else:
            print('{}/{}'.format(foot,head))
            break