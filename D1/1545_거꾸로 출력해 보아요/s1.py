import sys
sys.stdin=open('Sampleinput.txt')

N=int(input())
for i in range(0,N+1):
    print(N-i,end=' ')