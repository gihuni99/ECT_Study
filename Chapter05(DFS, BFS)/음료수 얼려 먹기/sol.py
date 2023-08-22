# -*- coding: cp949 -*-
#����) 
#N x M ũ���� ���� Ʋ, ������ �շ� �ִ� �κ��� 0, ĭ���̰� �����ϴ� �κ��� 1
#������ �շ��ִ� �κг��� ��,��,��,��� �پ��ִ� ��� ���� ����Ǿ� �ִ� ������ ����

#Ǯ��)

# N, M�� �������� �����Ͽ� �Է¹ޱ�
n, m = map(int,input().split())

# 2���� ����Ʈ�� �� ���� �Է¹ޱ�
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#DFS�� Ư���� ��带 �湮�� �ڿ� ����� ��� ���鵵 �湮
def dfs(x,y):
    #�־��� ������ ����� ��쿡�� ��� ����
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False#������ ����� False��ȯ
    #���� ��带 ���� �湮���� �ʾҴٸ�
    if graph[x][y]==0: #�ϳ� ������ ���� ��������� ��� ������ ã��, 1�� �����.
        #�ش� ��� �湮 ó��
        graph[x][y]=1
        #��, ��, ��, ���� ��ġ�� ��� ��������� ȣ��
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        #���� ��� �Լ��� ��� ����Ǹ� �ϳ��� ���� ��ü�� ã�� ��, ���� True�� ��ȯ�Ͽ� result�� +1
        return True
    return False#�̹� �湮�� node��� False ��ȯ

result=0

for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result+=1

print(result)