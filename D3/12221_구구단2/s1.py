import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    a, b = map(int,input().split())
    if a < 10 and b < 10 :
        print('#{} {}'.format(tc,a*b))
    else:
        print('#{} {}'.format(tc,-1))