import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N=int(input())
    pascal=[[1]]
    for i in range(1,N):

        pascal += [[1] + [0] * (i-1) + [1]]
        for j in range(1, i):
            if pascal[i][j] == 0:
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

    print('#{}'.format(tc+1))
    for i in range(N):
        print(*pascal[i])

