import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    income = list(map(int,input().split()))
    total = 0
    for i in income:
        total += i
    ever = total//len(income)

    cnt = 0

    for i in income:
        if i <= ever:
            cnt += 1

    print('#{} {}'.format(tc+1,cnt))
