import sys
sys.stdin=open('input.txt')

T=int(input())
for i in range(T):
    a,b=map(int,input().split())
    if a>b:
        print('#{} {}'.format(i+1,'>'))
    elif a<b:
        print('#{} {}'.format(i+1,'<'))
    else :
        print('#{} {}'.format(i + 1, '='))