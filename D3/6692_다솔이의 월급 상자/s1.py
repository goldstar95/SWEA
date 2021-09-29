import sys
sys.stdin = open('s_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = 0

    for _ in range(N):
        p, x = map(float, input().split())
        result += p * x
    print('#{} {}'.format(test_case, result))


