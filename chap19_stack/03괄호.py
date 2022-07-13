import sys

def VPS(string):
    mystack=[]
    
    for _ in range(len(string)):
        # if not string:
        #     if string[0] == ')' and mystack[-1]:
        
        mystack.append(string.pop(0))
        

T = int(sys.stdin.readline())

for _ in range(T):
    val = sys.stdin.readline()
    VPS(val)