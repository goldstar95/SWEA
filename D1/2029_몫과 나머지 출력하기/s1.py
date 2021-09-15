import sys
sys.stdin=open('input.txt')

T=int(input())
for i in range(T):
    a,b=map(int,input().split())
    print('#{} {} {}'.format(i+1,int(a/b),a%b))
