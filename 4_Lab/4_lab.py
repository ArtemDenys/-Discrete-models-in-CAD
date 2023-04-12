def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)
        for ind, val in enumerate(graph[u]):
            if not visited[ind] and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return visited[t]


def ford_fulkerson(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(graph, source, sink, parent):
        # Знаходимо мінімальний шлях та його потік
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        # Додаємо потік до максимального потоку та зменшуємо відповідні ребра
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

            # Виводимо ребро та його вагу, яке було змінено
            print("Змінено ребро ({}, {}) з вагою {} на {}".format(u, v, graph[v][u] + path_flow, graph[v][u]))

        # Виводимо максимальний потік на даний момент
        print("Максимальний потік на даний момент: {}".format(max_flow))

    # Виводимо кінцевий результат
    print("Максимальний потік в графі: {}".format(max_flow))


# Зчитування матриці з файлу
with open("data", "r") as f:
    n = int(f.readline().strip())
    graph = []
    for i in range(n):
        row = list(map(int, f.readline().strip().split()))
        graph.append(row)

source = 0
sink = n - 1

max_flow = ford_fulkerson(graph, source, sink)
