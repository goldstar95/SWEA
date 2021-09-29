import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    a,b,c = map(int,input().split())
    if a < b :
        print('#{} {}'.format(tc,c//a))
    else:
        print('#{} {}'.format(tc, c // b))