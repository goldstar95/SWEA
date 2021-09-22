import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    p,q = map(float,input().split())


    # s1
    # 올바르지 않은 면이라서 1번 뒤집고, 정상적으로 꼽힐때
    s1 = (1 - p) * q

    # s2
    # 올바른 면인데 제대로 꼽히지 않아서, 다시 꼽기 시도함.
    s2 = p * (1 - q) * p

    if s1 > s2 :
        print('#{} {}'.format(tc,'NO'))
    else:
        print('#{} {}'.format(tc, 'YES'))