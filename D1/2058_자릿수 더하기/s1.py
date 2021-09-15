import sys
sys.stdin=open('input.txt')

T=list(map(str,(input())))


sum=0
for i in T:
    sum+=int(i)

print(sum)

