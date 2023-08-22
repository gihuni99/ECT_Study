#Adjacency Matric(인접 행렬)은 node끼리의 모든 관계 정보를 저장하기 때문에 node가 많을 수록 메모리 많이 필요
#하지만 인접한 두 노드끼리의 관계 등 데이터를 빠르게 얻을 수 있다.

#Ex) node 1과 node 7이 연결되어 있는지 확인하기 위해서 adjacency matrix에서는 graph[1][7]을 확인하면 되지만,
# adjacency list에서는 node 1에 대한 list를 모두 확인해보아야 한다.

INF = 999999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)