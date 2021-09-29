import sys
sys.stdin = open('sample_input.txt')

T = int(input())



for tc in range(1,T+1):
    N,M = map(int,input().split())
    vote = [0] * N
    Ai = list(map(int,input().split()))
    Bi = list(map(int,input().split()))

    for b in range(M):
        for a in range(N):
            if Ai[a] <= Bi[b] :
                vote[a]+=1
                break;


    print('#{} {}'.format(tc,vote.index(max(vote))+1))
