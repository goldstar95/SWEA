import sys
sys.stdin=open('input.txt')


T=int(input())


for i in range(1,T+1):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    N=int(input())
    while N > 2:

        if N%2==0:
            N = N//2
            a+=1
        elif N%3==0:
            b+=1
            N = N // 3
        elif N%5==0:
            c+=1
            N = N // 5
        elif N%7==0:
            d+=1
            N = N // 7
        elif N%11==0:
            e+=1
            N = N // 11


    print('#{} {} {} {} {} {}'.format(i,a,b,c,d,e))