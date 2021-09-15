import sys
sys.stdin = open('input.txt')
T=int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())
    scores=[]
    scores_new=[]
    grade=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    for _ in range(N):
        middle,final,homework=map(int,input().split())
        total=(middle*0.35)+(final*0.45)+(homework*0.20)
        scores.append(total)
    score_k = scores[K - 1]
    cnt = 1
    for score in scores:
        if score > score_k:
            cnt += 1
    if cnt % (N / 10):
        result = grade[int(cnt // (N / 10))]
    else:
        result = grade[int(cnt // (N / 10)) - 1]
    print('#{} {}'.format(tc, result))





