import sys
sys.stdin=open('input.txt')

T=int(input())
for i in range(T):
    numbers=list(map(int,input().split()))
    max_number=numbers[0]

    for j in range(len(numbers)):
        if max_number <= numbers[j]:
            max_number = numbers[j]
    print('#{} {}'.format(i+1,max_number))


# 내장함수 사용
# T = int(input())
# for i in range(T):
#     numbers = list(map(int, input().split()))
#     print('#{} {}'.format(i+1,max(numbers)))