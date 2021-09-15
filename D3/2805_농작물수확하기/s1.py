import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1):
    N = int(input())
    land = [list(map(int, input())) for _ in range(N)]
    result = 0

    mid = N//2



    for i in range(N):
        for j in range(N):
    # 0~4가 있을 때
    # 0~2
    # 왼쪽 => mid값 , 오른쪽 => 2i+2
    # 0 : 2 <= i+j <= 2
    # 1 : 2 <= i+j <= 4
    # 2 : 2 <= i+j <= 6
    # 3~4
    # 왼쪽 => 2i-2 , 오른쪽 => mid + (N-1)값
    # 3 : 4 <= i+j <= 6
    # 4 : 6 <= i+j <= 6



