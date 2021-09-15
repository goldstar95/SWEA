import sys
sys.stdin=open('input.txt')

T=int(input())

for tc in range(T):
    numbers=list(map(int,input().split()))
    sum=0
    for i in numbers:
        sum+=i
    print('#{} {}'.format(tc+1,round(sum/len(numbers))))