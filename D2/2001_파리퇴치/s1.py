import sys
sys.stdin = open('input.txt')

T=int(input())
for tc in range(T):
    N,M = map(int,input().split())
    base=[list(map(int,input().split())) for _ in range(N)]

    max_fly = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0
            for r in range(M):
                for c in range(M):
                    fly += base[r+i][c+j]

            if max_fly < fly:
                max_fly = fly
    print('#{} {}'.format(tc+1,max_fly))
