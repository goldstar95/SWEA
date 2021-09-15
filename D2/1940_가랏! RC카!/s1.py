import sys
sys.stdin=open('input.txt')

T=int(input())
for tc in range(T):
    command=int(input())
    speed = 0
    distance = 0
    for i in range(command):
        time,speed= map(int,input().split())

