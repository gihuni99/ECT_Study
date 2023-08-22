# -*- coding: cp949 -*-
#����) N x M ũ���� ���簢�� �̷�, ������ ��ġ�� (1,1) �̷��� �ⱸ�� (N,M)�� ����
#������ �ִ� �κ��� 0, ���� �κ��� 1
from collections import deque

n, m = map(int,input().split())

my_map=[]

for i in range(n):
    my_map.append(list(map(int,input())))

# �̵��� �� ���� ����(�����¿�)
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        #���� ��ġ���� �� ���������� ��ġ Ȯ��
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #�̷� ã�� ������ ��� ��� ����
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            #���� ��� ����
            if my_map[nx][ny]==0:
                continue
            #�ش� ��带 ó�� �湮�ϴ� ��쿡�� �ִ� �Ÿ� ���
            if my_map[nx][ny]==1: #1�� ������ ���� ������ ��
                my_map[nx][ny]=my_map[x][y]+1 #�� ��ġ�� ��ŭ ���� ��带 �����Դ��� ǥ�ð� �ȴ�.
                queue.append((nx,ny))
    return my_map[n-1][m-1]

#BFS�� ������ ��� ���
print(bfs(0,0))