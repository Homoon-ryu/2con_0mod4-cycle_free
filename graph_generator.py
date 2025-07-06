import itertools

def generate_all_graphs_with_fixed_edges(n, fixed_edges):
    all_edges = [(i, j) for i in range(n) for j in range(i+1, n)]
    fixed_set = set(fixed_edges)
    free_edges = [e for e in all_edges if e not in fixed_set]

    for bits in itertools.product([0, 1], repeat=len(free_edges)):
        # initialize adjacency matrix
        adj = [[0]*n for _ in range(n)]

        # insert fixed edges
        for u, v in fixed_edges:
            adj[u][v] = adj[v][u] = 1

        # insert free edges based on current combination
        for idx, (u, v) in enumerate(free_edges):
            if bits[idx] == 1:
                adj[u][v] = adj[v][u] = 1

        yield adj
