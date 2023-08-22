#Adjacency List(인접 리스트)는 연결된 정보만을 저장하기 때문에 Matrix에 비해 메모리를 효율적으로 사용
#하지만 특정 2개의 node가 서로 연결되었는지에 대한 정보를 얻기 어렵다.

# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장 (노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장 (노드, 거리)
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장 (노드, 거리)
graph[2].append((0, 5))

print(graph)