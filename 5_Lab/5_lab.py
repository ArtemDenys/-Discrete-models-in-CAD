from itertools import permutations
from colorama import Fore,Style


def read_adjacency_matrix(file_path):
    adjacency_matrix = []
    with open(file_path, 'r') as f:
        for line in f:
            row = line.strip().split()
            row = [int(i) for i in row]
            adjacency_matrix.append(row)
    return adjacency_matrix


def isomorphic(graph1, graph2):
    n = len(graph1)
    m = len(graph2)

    if n != m:
        print("Графи неізоморфні: різна кількість вершин")
        return False

    nodes1 = list(range(n))
    nodes2 = list(range(m))

    # Перебираємо всі можливі перестановки вершин в графі 2
    for perm in permutations(nodes2):
        is_iso = True

        # Перевіряємо, чи збігається структура графів
        for i in range(n):
            for j in range(n):
                if graph1[i][j] != graph2[perm[i]][perm[j]]:
                    is_iso = False
                    break
            if not is_iso:
                break

        if is_iso:
            print(f"{Fore.LIGHTGREEN_EX}Графи ізоморфні: знайдено відображення вершин:")
            for i in range(n):
                print(f"{i} -> {perm[i]}")
            return True

    print(f"{Fore.LIGHTRED_EX}Графи неізоморфні: не знайдено відображення вершин")
    return False


# Перевірка графів на ізоморфність (TRUE)
print(f"{Fore.LIGHTCYAN_EX}Test #1")
graph1 = read_adjacency_matrix('5_Lab/data_1(1)')
graph2 = read_adjacency_matrix('5_Lab/data_1(2)')

if isomorphic(graph1, graph2):
    print(f"{Fore.LIGHTGREEN_EX}Графи ізоморфні\n")
else:
    print(f"{Fore.LIGHTRED_EX}Графи неізоморфні\n")

# Перевірка графів на ізоморфність (FALSE)
print(f"{Fore.LIGHTCYAN_EX}Test #2")
graph1 = read_adjacency_matrix('5_Lab/data_2(1)')
graph2 = read_adjacency_matrix('5_Lab/data_2(2)')

if isomorphic(graph1, graph2):
    print(f"{Fore.LIGHTGREEN_EX}Графи ізоморфні\n")
else:
    print(f"{Fore.LIGHTRED_EX}Графи неізоморфні\n{Style.RESET_ALL}")
