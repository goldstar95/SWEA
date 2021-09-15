import sys
sys.stdin=open('input.txt')

a,b=map(int,input().split())

if a>b:
    print('A')
elif a==b:
    print('비김')
else:
    print('B')