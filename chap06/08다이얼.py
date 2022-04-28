def findNum(str):
    AbcList = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
    indx = 0
    for i in AbcList:
        if str in i:
            break
        indx+=1
    return indx+3

x = input()
sum=0
for i in x:
    sum+=findNum(i)
print(sum)