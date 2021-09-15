import sys
sys.stdin=open('input.txt')

T=int(input())

day_list=[0,31,28,31,30,31,30,31,31,30,31,30,31]

for tc in range(T):
    m1,d1,m2,d2=list(map(int,input().split()))
    result=0

    # 같은 달 인 경우
    if m1 == m2:
        result = d2 - d1 + 1

    # 다른 달 인 경우
    else:
        #시작하는 달
        result = day_list[m1]-d1+1
        #중간에 있는 달
        for i in range(m1+1,m2):
            result += day_list[i]
        #마지막 달
        result += d2
    print('#{} {}'.format(tc+1,result))


