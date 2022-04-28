s = input()
myList = [-1]*26
for i in range(len(s)):
    indx=ord(s[i])-ord('a')
    if myList[indx]==-1:
        myList[indx]=i
        
for i in myList:
    print(i, end=" ")