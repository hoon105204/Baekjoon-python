# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 다섯 가지이다.

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys

num = int(sys.stdin.readline())
my_list = []

for _ in range(num):
    
    # 값 받아오기
    inp = sys.stdin.readline().split()
    # 만약 push N 이라면 쪼갬
    command = inp[0]
    if command == 'push':
        val = int(inp[1])
    
    if command == 'push':
        my_list.append(val)
        
    if command == 'pop':
        if len(my_list)==0:
            print(-1)
        else:
            print(my_list.pop())
            
    if command == 'size':
        print(len(my_list))
        
    if command == 'empty':
        if len(my_list)==0:
            print(1)
        else:
            print(0)
            
    if command == 'top':
        if len(my_list)!=0:
            print(my_list[-1])
        else:
            print(-1)