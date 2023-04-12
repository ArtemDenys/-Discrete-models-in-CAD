import itertools
from colorama import Fore

with open("data", "r") as f:
    num_vertices = int(f.readline())
    graph = []
    for i in range(num_vertices):
        graph.append(list(map(int, f.readline().split())))
selected_options = 0
best_path = None
min_distance = float("inf")

for path in itertools.permutations(range(num_vertices)):
    distance = 0
    valid_path = True
    for i in range(num_vertices):
        if i == num_vertices - 1:
            if graph[path[i]][path[0]] == 0:
                valid_path = False
        else:
            if graph[path[i]][path[i + 1]] == 0:
                valid_path = False
    if valid_path:
        for i in range(num_vertices):
            distance += graph[path[i - 1]][path[i]]
        if distance < min_distance:
            best_path = path
            min_distance = distance
        selected_options += 1
print(f"{Fore.LIGHTGREEN_EX}\tКількість перербраних шляхів:", selected_options)
print(f"\tКращий шлях:", tuple(v + 1 for v in best_path))
print(f"\tМінімальний шлях:", min_distance)
