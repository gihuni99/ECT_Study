# -*- coding: cp949 -*-
#문제) N x M 크기의 직사각형 미로, 동빈의 위치는 (1,1) 미로의 출구는 (N,M)에 존재
#괴물이 있는 부분은 0, 없는 부분은 1
from collections import deque

n, m = map(int,input().split())

my_map=[]

for i in range(n):
    my_map.append(list(map(int,input())))

# 이동할 네 방향 정의(상하좌우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        #현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            #벽인 경우 무시
            if my_map[nx][ny]==0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if my_map[nx][ny]==1: #1은 가보지 않은 안전한 길
                my_map[nx][ny]=my_map[x][y]+1 #각 위치에 얼만큼 많은 노드를 지나왔는지 표시가 된다.
                queue.append((nx,ny))
    return my_map[n-1][m-1]

#BFS를 수행한 결과 출력
print(bfs(0,0))