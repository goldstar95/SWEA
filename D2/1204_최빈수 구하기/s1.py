import sys
sys.stdin = open('input.txt')

T= int(input())
for i in range(T):
    tc=int(input())
    num_list=list(map(int,input().split()))

    num_count=[]
    for num in range(100):
        num_count.append(num_list.count(num))

    # 만약 최빈수가 중복된 숫자가 있을 경우
    if num_count.count(max(num_count)) > 1:
        # 처음 나오는 최빈수를 제거 ( 가장 큰 점수를 출력하라고 함 )
        num_count.remove(max(num_count))
        # 갯수가 1개 줄어들었기 때문에 +1을 해야 원래 위치가 출력됨.
        print('#{} {}'.format(tc, num_count.index(max(num_count))+1))
    else:
        print('#{} {}'.format(tc, num_count.index(max(num_count))))



