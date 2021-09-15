import sys
sys.stdin = open('input.txt')

T=int(input())
for tc in range(T):
    N=int(input())
    alpha_list = ''

    for i in range(N):
        alpha,count=input().split()
        for j in range(int(count)):
            alpha_list += alpha

    print('#{}'.format(tc+1))
    while alpha_list:
        print(alpha_list[:10])
        alpha_list = alpha_list[10:]
