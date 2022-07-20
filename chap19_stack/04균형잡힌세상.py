import sys


def VPS(string):
    text = string.rstrip()
    while True:
        if '()' not in text and '[]' not in text:
            break
        text = text.replace('()', '')
        text = text.replace('[]', '')
    if bool(text):
        print('no')
    else:
        print('yes')


while True:
    text = sys.stdin.readline()
    if text == '.\n':
        break

    new_text = ''

    for s in text:
        if s in ['(',')','[',']']:
            new_text += s

    VPS(new_text)