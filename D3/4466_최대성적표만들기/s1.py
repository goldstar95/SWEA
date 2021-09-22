import sys
sys.stdin=open('sample_input.txt')
T = int(input())

for tc in range(1,T+1):
    N,K = input().split()
    num = list(map(int,input().split()))

    answer = 0
    for i in range(int(K)):
        answer += max(num)
        num.remove(max(num))
    print('#{} {}'.format(tc,answer))