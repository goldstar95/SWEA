import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    alpha = input()
    comp = []
    for i in alpha:
        if i not in comp :
            comp.append(i)
        elif i in comp :
            pass
    if len(comp) == 2:
        print('#{} {}'.format(tc,'Yes'))
    else:
        print('#{} {}'.format(tc, 'No'))

