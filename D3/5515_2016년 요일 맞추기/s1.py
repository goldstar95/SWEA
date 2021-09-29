import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T+1):
    m, d = map(int, input().split())
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    today = 4
    result = (sum(month[:m]) + d + (today-1)) % 7
    print('#{} {}'.format(tc, result))