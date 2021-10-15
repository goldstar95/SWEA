import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    p_list = list(map(int,input().split()))
    cnt = 0
    for i in range(1,N-1):
        if p_list[i] > p_list[i-1] and p_list[i] > p_list[i+1]:
            pass
        elif p_list[i] < p_list[i-1] and p_list[i] < p_list[i+1]:
            pass
        else:
            cnt+=1
    print('#{} {}'.format(tc,cnt))
