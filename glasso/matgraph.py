import graphviz

def generate_graph(matrix, epsilon=0, negative=True, header=None, legend=''):
    edges = []
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] > epsilon or negative and matrix[i][j] < -epsilon:
                edges.append((i, j))

    dot = graphviz.Graph(legend)

    for i in range(n):
        if header:
            dot.node(str(i), str(header[i]))
        else:
            dot.node(str(i))

    for (src, dst) in edges:
        dot.edge(str(src), str(dst))

    return dot


