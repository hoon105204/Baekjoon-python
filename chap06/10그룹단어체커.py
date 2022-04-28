# 함수 작성
def groupWord(givenStr):
    myList = [0]*26
    conti = False
    preWord =""

    for i in givenStr:
        if preWord == i:
            conti = True
        if myList[ord(i)-97]==0:
            myList[ord(i)-97]=1
        elif myList[ord(i)-97]==1 & conti:
            myList[ord(i)-97]=1
        else:
            return False

        preWord = i
        conti=False

    return True

# 실행
N = int(input())
ans=0
for i in range(N):
    givenWord = input()
    if groupWord(givenWord):
        ans+=1
print(ans)