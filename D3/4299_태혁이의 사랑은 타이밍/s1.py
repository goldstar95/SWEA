import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    date = [11,11,11]
    D, H, M = map(int,(input().split()))

    if D - date[0] == 0 and H <= date[1] and M < date[2]:
        result = -1
    elif D - date[0] == 0 and H < date[0]:
        result = -1
    else:
        day = (int(D) - date[0]) * 60 * 24
        hour = (int(H) - date[1]) * 60
        minite = int(M) - date[2]
        result = day+hour+minite
    print('#{}'.format(tc), result)