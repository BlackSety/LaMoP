import timeit

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

edges = [(1, 2), (2, 3), (2, 4), (4, 5), (1, 6), (6, 7), (4, 5)]
start = 1
end = 5
path, visited = wave_algorithm(edges, start, end)
if path:
    print (f"Кратчайший путь от {start} до {end}: {path}")
else:
    print (f"Путь от {start} до {end} не найден")
print ("Шаги посещения вершин:", visited)

def path_rec(edges, start, end):
    path, parent = wave_algorithm(edges, start, end)
    def reconstruct_path():
        if path is None:
             return None
        current_path = []
        current = end
        while current is not None:
            current_path.append(current)
            current = parent[current]
        current_path.reverse()
        return current_path
    return reconstruct_path

def alg():
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
    edges = [(1, 2), (2, 3), (2, 4), (4, 5), (1, 6), (6, 7), (4, 5)]
    start = 1
    end = 5
    path, visited = wave_algorithm(edges, start, end)
    if path:
        return (f"Кратчайший путь от {start} до {end}: {path}", ("Шаги посещения вершин:", visited))
    else:
        return (f"Путь от {start} до {end} не найден", ("Шаги посещения вершин:", visited))

avg=0
ans=0
for i in range (5):
    otv=(timeit.repeat("alg()", setup="from __main__ import alg", number=10000000, repeat=5))
    avg = sum(otv)/len(otv)
    print(avg)
    ans+=avg
print(ans/5, "avg alg")

avg=0
ans=0
for i in range (5):
    otv=(timeit.repeat("count_vertices(edges)", setup="from __main__ import count_vertices, edges", number=10000000, repeat=5))
    avg = sum(otv)/len(otv)
    print(avg)
    ans+=avg
print(ans/5, "avg count_vertices")

avg=0
ans=0
for i in range (5):
    otv=(timeit.repeat("get_vertices(edges)", setup="from __main__ import get_vertices, edges", number=10000000, repeat=5))
    avg = sum(otv)/len(otv)
    print(avg)
    ans+=avg
print(ans/5, "avg get_vertices")

ANS = path_rec(edges, start, end)
avg=0
ans=0
for i in range (5):
    otv=(timeit.repeat("ANS", setup="from __main__ import ANS", number=10000000, repeat=5))
    avg = sum(otv)/len(otv)
    print(avg)
    ans+=avg
print(ans/5, "avg path_rec")

avg=0
ans=0
for i in range (5):
    otv=(timeit.repeat("wave_algorithm(edges, start, end)", setup="from __main__ import wave_algorithm, edges, start, end", number=10000000, repeat=5))
    avg = sum(otv)/len(otv)
    print(avg)
    ans+=avg
print(ans/5, "avg wave_algorithm")