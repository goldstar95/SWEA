import sys
sys.stdin = open('input.txt')

T=int(input())

for tc in range(T):
    numbers = list(map(int,input().split()))

    # 버블정렬
    for i in range(len(numbers)-1,0,-1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]



    numbers.remove(numbers[0])
    numbers.remove(numbers[-1])
    n_sum=0
    for num in numbers:
        n_sum += num

    print('#{} {}'.format(tc+1,round(n_sum/len(numbers))))
