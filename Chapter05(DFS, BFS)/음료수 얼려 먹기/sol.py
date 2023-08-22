# -*- coding: cp949 -*-
#문제) 
#N x M 크기의 얼음 틀, 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1
#구멍이 뚫려있는 부분끼리 상,하,좌,우로 붙어있는 경우 서로 연결되어 있는 것으로 간주

#풀이)

# N, M을 공백으로 구분하여 입력받기
n, m = map(int,input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False#영역을 벗어나면 False반환
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y]==0: #하나 영역에 들어가면 재귀적으로 모든 영역을 찾고, 1로 만든다.
        #해당 노드 방문 처리
        graph[x][y]=1
        #상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        #위의 재귀 함수가 모두 종료되면 하나의 영역 전체를 찾은 것, 따라서 True를 반환하여 result에 +1
        return True
    return False#이미 방문한 node라면 False 반환

result=0

for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result+=1

print(result)