import timeit
edges = [(1, 2), (2, 3), (2, 4), (4, 5), (1, 6), (6, 7), (4, 5)]
start = 1
end = 5
def count_vertices(edges):
    """Подсчет количества вершин в графе."""
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return len(vertices)

def get_vertices(edges):
    """Получение списка вершин из списка ребер."""
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return list(vertices)

def wave_algorithm(edges, start, end):
    """Реализация волнового алгоритма."""
    vertices = get_vertices(edges)
    num_vertices = count_vertices(edges)

    # Инициализация массива пройденных вершин
    visited = {v: 0 for v in vertices}
    visited[start] = 1

    # Инициализация массива предков для восстановления пути
    parent = {v: None for v in vertices}

    # Флаг для проверки, найдена ли конечная вершина
    found = False

    # Шаг волнового алгоритма
    step = 1

    while True:
        # Флаг для проверки, были ли найдены новые вершины на текущем шаге
        new_vertices_found = False

        # Проходим по всем вершинам, которые были посещены на предыдущем шаге
        for v in vertices:
            if visited[v] == step:
                # Проходим по всем соседям текущей вершины
                for edge in edges:
                    if edge[0] == v and visited[edge[1]] == 0:
                        visited[edge[1]] = step + 1
                        parent[edge[1]] = v
                        new_vertices_found = True
                    if edge[1] == v and visited[edge[0]] == 0:
                        visited[edge[0]] = step + 1
                        parent[edge[0]] = v
                        new_vertices_found = True

        # Если конечная вершина найдена, выходим из цикла
        if visited[end] != 0:
            found = True
            break

        # Если новые вершины не найдены, выходим из цикла
        if not new_vertices_found:
            break

        step += 1

    # Восстановление пути
    if found:
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
        return path, visited
    else:
        return None, visited

avg=0
ans=0
for i in range (5):
    otv=(timeit.repeat("wave_algorithm(edges, start, end)",setup="from __main__ import wave_algorithm, edges, start, end", number=10000000, repeat=5))
    avg = sum(otv)/len(otv)
    print(avg)
    ans+=avg
print(ans/5, "avg wave_algorithm")
# timeit res =  61.19800001033582
#               61.1903999815695
#               60.36079998011701
#               61.01339997258037
#               62.28120002197102
# timeit res avg = 61.20875999331474