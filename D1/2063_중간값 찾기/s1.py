import sys
sys.stdin=open('input.txt')

N=int(input())
numbers=list(map(int,input().split()))
center_count=N//2

for i in range(len(numbers)-1,0,-1):
    for j in range(i):
        if numbers[j] > numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1],numbers[j]

print(numbers[center_count])





