from colorama import Fore

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result

    def read_from_file(self, file_path):
        with open(file_path) as f:
            lines = f.readlines()
            for i in range(1, self.V+1):
                line = lines[i].split()
                for j in range(self.V):
                    if int(line[j]) > 0:
                        self.add_edge(i-1, j, int(line[j]))


if __name__ == "__main__":
    g = Graph(8)
    g.read_from_file("data_1(1)")
    result = g.kruskal()
    print(f"\t{Fore.GREEN}Minimum Spanning Tree:")
    for u, v, weight in result:
        print(f"\t\t{chr(u + 65)}-{chr(v + 65)}: {weight}")
    print(f"\tTotal weight of the Minimum Spanning Tree: {sum(weight for _, _, weight in result)}")