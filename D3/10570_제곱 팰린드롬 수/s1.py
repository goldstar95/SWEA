import sys
sys.stdin = open('input.txt')

T= int(input())

for tc in range(T):
    start,end = map(int,input().split())
    palindrome = []


    for num in range(start, end + 1):
        if str(num) == str(num)[::-1]:
            palindrome.append(num)


    cnt = 0
    for num in palindrome:
        sqrt_num = int(num ** (1 / 2))

        if num**(1/2) == sqrt_num and str(sqrt_num) == str(sqrt_num)[::-1]:
            cnt += 1


    print('#{} {}'.format(tc+1, cnt))
