import timeit
edges = [(1, 2), (2, 3), (2, 4), (4, 5), (1, 6), (6, 7), (4, 5)]
def get_vertices(edges):
    """Получение списка вершин из списка ребер."""
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return list(vertices)
avg=0
ans=0
for i in range (5):
    otv=(timeit.repeat("get_vertices(edges)", setup="from __main__ import get_vertices, edges", number=10000000, repeat=5))
    avg = sum(otv)/len(otv)
    print(avg)
    ans+=avg
print(ans/5, "avg get_vertices")
# timeit res =  7.6582493599999
#               7.663443499998539
#               7.607033360001514
#               7.993803900000057
#               7.838286240000161
# timeit res avg = 7.752163272000034