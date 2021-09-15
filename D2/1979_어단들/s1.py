import sys
sys.stdin=open('input.txt')

T=int(input())

for tc in range(T):
    # N -> 퍼즐크기 K -> 회문길이
    N,K=map(int,input().split())

    #어디든 01110 이 나오면 cnt 할수 있게끔.

    # 배열의 상하좌우 0을 둘러쌈
    base = [[0] * (N+2)] + [[0] + list(map(int,input().split())) + [0] for _ in range(N)] + [[0] * (N+2)]

    # 전치행렬 만들기
    axis_base = [[0] * (N+2) for _ in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            axis_base[i][j]=base[j][i]

    # 찾을 단어 양 옆에 0 넣기
    word = [0] + [1] * K + [0]

    cnt = 0


    for i in range(N + 2):
        # 양쪽에 0 2개 추가이기 때문에 +2 됨.
        for j in range(N + 2):
            if base[i][j:j + K + 2] == word:
                cnt += 1
            if axis_base[i][j:j + K + 2] == word:
                cnt += 1

    print('#{} {}'.format(tc+1, cnt))