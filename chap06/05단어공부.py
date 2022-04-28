def myFunc(inpStr):
    ansList = [0]*26

    for i in inpStr:
        i = i.upper()
        indx = ord(i)-ord('A')
        ansList[indx]+=1

    testList = ansList[:]
    testList.sort(reverse=True)

    if testList[0]==testList[1]:
        return "?"

        
    maxVal=testList[0]

    for i in range(len(ansList)):
        if ansList[i] == maxVal:
            ans = chr(i+ord('A'))
            return ans

inpS = input()
print(myFunc(inpS))