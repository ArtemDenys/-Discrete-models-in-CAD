def read_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        size = int(file.readline())
        matrix = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            row = file.readline().split()
            for j in range(size):
                matrix[i][j] = int(row[j])
        return matrix


def convert_matrix_to_dict(matrix):
    nodes = {}
    size = len(matrix)
    for i in range(size):
        node = []
        for j in range(size):
            if matrix[i][j] != 0:
                node.append({'id': j, 'weight': matrix[i][j]})
        nodes[chr(ord('a') + i)] = node
    return nodes


def is_euler_graph(nodes):
    for node in nodes.values():
        if len(node) % 2 != 0:
            return False
    return True


def add_edges(nodes):
    pass


def find_postman_way(nodes, additional_edges):
    if not is_euler_graph(nodes):
        print("Граф не є Ейлеровим. Розпочинається перебудова графа.")
        add_edges(nodes)
    find_way(nodes, additional_edges)


def find_way(nodes, additional_edges):
    way = 0
    for node in nodes.values():
        for edge in node:
            way += edge['weight']
    way /= 2
    print(f"Шлях без повторень: {way}")
    way += sum([edge['length'] for edge in additional_edges])
    print(f"Повний шлях: {way}")


matrix = read_matrix_from_file('data')
nodes = convert_matrix_to_dict(matrix)
additional_edges = [{'id': 0, 'length': 27}, {'id': 1, 'length': 36}, {'id': 2, 'length': 16}]
find_postman_way(nodes, additional_edges)
