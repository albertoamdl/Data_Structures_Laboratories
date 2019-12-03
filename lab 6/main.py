from graph import GraphNode
# Helped by Eduardo and Diego
# Both labs implemented in same method because they use same constructors (some)


def topological_sort(graph):
    all = graph.compute_indegree()
    soted = []

    sett = []

    for i in range(len(all)):
        if all[i] == 0:
            sett.append(i)

    while len(sett) > 0:
        u = sett.pop()

        soted.append(u)

        for adj_vertex in graph.vertices_reachable_from(u):
            all[adj_vertex] -= 1

            if all[adj_vertex] == 0:
                sett.append(adj_vertex)

    if len(soted) != graph.num_vertices():
        return None

    return soted


def kruskal(graph):
    sortedE = []

    for lst in graph:
        for edge in lst:
            sortedE.append(edge)

    sortedE.sort(key=lambda e: e.weight)  # sort by weight
    item = GraphNode(6, weighted=True, directed=False)  # 6 is # of numbers (?)

    for edge in sortedE:
        if not item.contains_cyle():
            item.insert(edge.source, edge.dest, edge.weight)

    return item


def edit_distance(str1, str2):
    demen = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]

    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            if i == 0:
                demen[i][j] = j

            elif j == 0:
                demen[i][j] = i

            elif str1[i - 1] == str2[j - 1]:
                demen[i][j] = demen[i - 1][j - 1]

            else:
                demen[i][j] = 1 + min(demen[i][j - 1],      # Insert
                                      demen[i - 1][j],      # Remove
                                      demen[i - 1][j - 1])  # Replace

    return demen[-1][-1]


s1 = "Hello"
s2 = "Hello"

print(edit_distance(s1, s2))
print()
# Test Cases

n = GraphNode(6, weighted=True, directed=True)
n.insert(4, 4, 1)
n.insert(5, 2, 3)
n.insert(4, 3, 2)
n.insert(3, 4, 1)  # Numbers can change to test
n.insert(2, 5, 0)
n.insert(1, 1, 4)
n.display()

wow = kruskal(n.al)
wow.display()

print(topological_sort(n))
