# Python3 program to print DFS traversal
# from a given graph
from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation


class Graph:

    # Constructor
    def __init__(self):

        #dùng thư viên mặc định để lưu trữ đồ thị
        self.graph = defaultdict(list)

    # Hàm thêm 1 canh vào đồ thị
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Hàm sd bởi DFS để duyệt đồ thị
    def DFSUtil(self, v, visited):

        # đánh dấu nút hiện tại đã được duyệt

        # và in ra nút đó
        visited.add(v)
        print(v, end=' ')

        # duyệt các đỉnh kề của nút hiện tại
        # nếu chưa được duyệt thì gọi đệ quy
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # Hàm duyệt đồ thị theo DFS
    # Sử dụng hàm DFSUtil
    def DFS(self, v):

        # tạo tập chứa các đỉnh đã được duyệt
        visited = set()

        # gọi hàm DFSUtil để duyệt đồ thị
        # để in ra
        self.DFSUtil(v, visited)


# Driver's code


# Tạo đồ thị
# Với 8 đỉnh và 10 cạnh
if __name__ == "__main__":
    g = Graph()

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 5)
    g.addEdge(3, 6)
    g.addEdge(4, 7)
    g.addEdge(4, 5)
    g.addEdge(5, 2)
    print("DSF: (bắt đầu từ đỉnh 0)")
    # gọi hàm DFS để duyệt đồ thị
    g.DFS(0)
    print("Hello world")
