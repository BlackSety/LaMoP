import timeit
edges = [(1, 2), (2, 3), (2, 4), (4, 5), (1, 6), (6, 7), (4, 5)]
def count_vertices(edges):
    """Подсчет количества вершин в графе."""
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return len(vertices)
avg=0
ans=0
for i in range (5):
    otv=(timeit.repeat("count_vertices(edges)", setup="from __main__ import count_vertices, edges", number=10000000, repeat=5))
    avg = sum(otv)/len(otv)
    print(avg)
    ans+=avg
print(ans/5, "avg count_vertices")
# timeit res =  6.548137459997088
#               6.750570059998426
#               6.512972140000784
#               6.496892899999511
#               6.49756492000306
# timeit res avg = 6.561227495999773