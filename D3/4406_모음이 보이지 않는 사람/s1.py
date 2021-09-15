import sys
sys.stdin = open('1_input_sample.txt')

T=int(input())

vowels = ['a','e','i','o','u']

for tc in range(T):
    text = input()
    result = ''
    for word in text:
        if word not in vowels:
            result += word

    print('#{} {}'.format(tc+1,result))