import sys


def VPS(string):
    text = string.strip()
    while True:
        if '()' not in text:
            break
        text = text.replace('()', '')
    if bool(text):
        print('NO')
    else:
        print('YES')


T = int(sys.stdin.readline())

for _ in range(T):
    string = sys.stdin.readline()
    VPS(string)
