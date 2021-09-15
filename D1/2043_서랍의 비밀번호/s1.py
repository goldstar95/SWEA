import sys
sys.stdin=open('input.txt')

pw,num=map(int,input().split())

count=0
for check_num in range(num,1000):
    count += 1
    if pw==check_num:
        print(count)
    else:
        continue
