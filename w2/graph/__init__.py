# 인접 행렬로 그래프 구현
class GraphMatrix:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]

    def add_edge(self, v1, v2):
        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1 # 무방향(양방향) 그래프인 경우

    def print_matrix(self):
        for row in self.matrix:
            print(row)


# 인접 리스트로 그래프 구현
class GraphList:
    def __init__(self):
        self.graph = {}

    def add_edge(self, v1, v2):
        if v1 not in self.graph:
            self.graph[v1] = []
        if v2 not in self.graph:
            self.graph[v2] = []
        self.graph[v1].append(v2)
        self.graph[v2].append(v1) # 무방향 그래프인 경우

    def print_graph(self):
        for key in self.graph:
            print(key, ":", self.graph[key])



# 예제 사용
graph = GraphList()
graph.add_edge(1, 3)
graph.add_edge(1, 5)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 5)
graph.add_edge(4, 5)

print('인접 리스트:')
graph.print_graph()

