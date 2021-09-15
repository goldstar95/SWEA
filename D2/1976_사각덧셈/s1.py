import sys
sys.stdin = open('input.txt')

T=int(input())
for tc in range(T):
    t1,m1,t2,m2 = map(int,input().split())

    result_t = t1 + t2
    result_m = m1 + m2

    if result_m > 59:
        result_m = result_m - 60
        result_t += 1

    else :
        pass

    if result_t > 12:
        result_t = result_t - 12

    else:
        pass

    print('#{} {} {}'.format(tc+1,result_t, result_m))


