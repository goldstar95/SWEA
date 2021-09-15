import sys
sys.stdin=open('input.txt')

alpha=list(map(ord,input()))
for i in alpha:
    print(i-64,end=' ')

