def sarray(num):
    num_list = [x for x in range(1, num + 1)]

    tmp = []
    res = []
    for _ in range(num):
        my_int = int(input())

        while True:
            # num_list가 비었다면 스킵
            if not num_list:
                break
            # num_list에서 선택한 값이 나올때까지 팝
            if num_list[0] <= my_int:
                tmp.append(num_list.pop(0))
                res.append('+')
            else:
                break
        # 선택한 값이랑 tmp에 마지막 값이 같으면 계속 진행
        if my_int == tmp[-1]:
            tmp.pop()
            res.append('-')
        else:
            print('NO')
            return

    for i in res:
        print(i)


sarray(int(input()))
