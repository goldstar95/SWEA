import sys
sys.stdin=open('input.txt')

T=int(input())
#1~12월까지 월별 일수 리스트에 넣어놓음.
day_list=[31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(1,T+1):
    #연,월,일 값 받음
    ymd=input()
    #연 월 일 값 슬라이싱으로 분할에서 넣어 놓음
    y,m,d=ymd[:4],ymd[4:6],ymd[6:8]

    # 월: 1~12사이 일: 1~월별 일값 사이
    if 1<=int(m)<=12 and 1<= int(d)<=day_list[int(m)-1]:
        print('#{} {}/{}/{}'.format(i,y,m,d))
    else:
        print('#{} -1'.format(i))