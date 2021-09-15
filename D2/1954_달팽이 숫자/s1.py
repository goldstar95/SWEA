import sys

sys.stdin=open('input.txt')

T=int(input())

for tc in range(1,T+1):
    N=int(input())
    #달팽이 만들기
    snail=[[0]*N for _ in range(N)]
    #횟수
    count = 1


    di=[0,1,0,-1]
    dj=[1,0,-1,0]

    # 처음 시작 위치 ( 처음 이동했을 경우 0,0 이 되도록 설정하였음.)
    i,j = 0,-1

    # 이동하고자 하는 방향
    dir = 0

    # N*N 횟수 만큼(달팽이크기만큼) while 문 돈다.
    while count <= N*N:
        #dir은 처음 0으로 들어온다.
        # -> dir[0]은 di[0],dj[1] 이기 때문에 오른쪽으로 움직인다.
        ni,nj = i+di[dir],j+dj[dir]

        #이동하기전에 (ni,nj)가 배열 범위(N)에 있는지 확인하고
        #한바퀴돌았을 경우 이미 값이 있는 배열과 만날 수 있는데 이때 해당 배열이 비어있는지 확인해야 한다.
        if 0<=ni<N and 0<=nj<N and snail[ni][nj]==0:
            # 달팽이배열에 count를 넣어준다. (즉, 1부터 넘버링을 넣어준다.)
            # i,j 의 시작위치도 새로 바뀌기 때문에 ni, nj를 i,j에 넣어줍니다.
            snail[ni][nj] = count
            count += 1
            i,j = ni,nj

        #만약 한 방향이 끝났을 경우 방향을 돌려준다.
        #0~3까지 돌아가기 때문에 %4로 값을 얻어준다.
        else:
            dir= (dir+1) % 4

    print('#{}'.format(tc))
    for i in range(N):
        print(*snail[i])