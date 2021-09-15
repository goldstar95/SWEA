import sys
sys.stdin=open('input.txt')

T=int(input())
for tc in range(T):
    strings=input()

    # 마디의 최대 길이는 10 이기때문에
    for i in range(1,10):
        # 만약 i까지의 문자와 i ~ i*2 까지의 문자가 같다면 print
        if strings[:i]==strings[i:i*2]:
            print('#{} {}'.format(tc + 1, i ))
            # 그 뒤로도 같은 경우가 생길 수 있으므로 한번 나오면 break 걸음.
            break