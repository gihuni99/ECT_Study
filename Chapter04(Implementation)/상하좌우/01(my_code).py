
x=1;y=1 #좌표 시작 지점/ 시작위치가 0,0이 아닌 1,1인 것에 유의!

dx=[-1,1,0,0] #U, D, L, R순으로 설정
dy=[0,0,-1,1] #U, D, L, R순으로 설정  / 기준이 실제 좌표 축이 아닌 문제에서 제시된 방향으로 하였다.
# ex) U으로 이동한다면 dx=-1,dy=0이다.

N=int(input()) #NxN의 공간을 나타낸다.
t_sch=list(input().split()) #여행 스케줄을 의미한다.

for i in range(len(t_sch)): #여행 스케줄의 길이만큼 for문 반복
    if t_sch[i]=='U':
        if x==1: # x좌표가 1, 즉 좌표가 맨위에 존재한다면 위로 올라갈 수 없으므로 무시
            continue
        x=x+dx[0]
        y=y+dy[0]
    elif t_sch[i]=='D':
        if x==N:
            continue
        x=x+dx[1]
        y=y+dy[1]

    elif t_sch[i]=='L':
        if y==1:
            continue
        x=x+dx[2]
        y=y+dy[2]
    elif t_sch[i]=='R':
        if y==N:
            continue
        x=x+dx[3]
        y=y+dy[3]

print(x,y)

