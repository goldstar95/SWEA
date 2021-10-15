import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    hays=[]
    result = 0
    for _ in range(N):
         hays.append(int(input()))
    aver = sum(hays)/len(hays)
    for i in hays:
        if i < aver:
            result += abs(aver - i)
    print('#{} {}'.format(tc,int(result)))



