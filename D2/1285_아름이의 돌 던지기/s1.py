import sys
sys.stdin = open('input.txt')

T=int(input())

def min_n(move_m):
    for i in range(len(move_m) - 1, 0, -1):
        for j in range(i):
            if move_m[j] > move_m[j + 1]:
                move_m[j], move_m[j + 1] = move_m[j + 1], move_m[j]
    return move_m[0]


def max_n(move_p):
    for i in range(len(move_p) - 1, 0, -1):
        for j in range(i):
            if move_p[j] > move_p[j + 1]:
                move_p[j], move_p[j + 1] = move_p[j + 1], move_p[j]
    return move_p[-1]

for tc in range(T):
    N=int(input())
    move=list(map(int,input().split()))
    move_p=[]
    move_m=[]
    result=[]
    for i in range(len(move)):
        if move[i]<0:
            move_m.append(move[i])
        elif move[i]>0:
            move_p.append((move[i]))
        else:
            result.append((move[i]))


    if -min_n(move_m) < max_n((move_p)):
        print('#{} {} {}'.format(tc+1, max_n(move_p), move.count(max_n((move_p)))))
    elif  -min_n(move_m) > max_n((move_p)):
        print('#{} {} {}'.format(tc + 1, -min_n(move_m), move.count(min_n((move_m)))))
    else:
        print('#{} {} {}'.format(tc + 1, max_n(move_p), move.count(max_n((move_p))) + move.count(min_n((move_m)))))
