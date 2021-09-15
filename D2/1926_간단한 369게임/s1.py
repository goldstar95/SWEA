import sys
sys.stdin = open('input.txt')


N = int(input())
for i in range(1, N + 1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        a = str(i).count('3')
        b = str(i).count('6')
        c = str(i).count('9')
        cnt = a + b + c
        print('-'*cnt, end = ' ' )
    else:
        print(i, end = ' ')








