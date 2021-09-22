import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N,A,B =map(int,input().split())
    if N > A+B:
        if A > B :
            print('#{} {} {}'.format(tc,B,'0'))
        else:
            print('#{} {} {}'.format(tc, A, '0'))


    elif N < A+B:
        if A > B:
            print('#{} {} {}'.format(tc, B, (A+B)-N))
        else:
            print('#{} {} {}'.format(tc, A, (A+B)-N))

    elif N == A == B :
        print('#{} {} {}'.format(tc, A, A))