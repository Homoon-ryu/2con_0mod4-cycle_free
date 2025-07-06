import networkx as nx
import os  

def read_graphs_from_file(filename):
    graphs = []
    with open(filename, 'r') as f:
        matrix = []
        for line in f:
            line = line.strip()
            if line == '':
                if matrix:
                    G = adj_matrix_to_nx(matrix)
                    graphs.append(G)
                    matrix = []
            else:
                matrix.append([int(x) for x in line.split()])
        if matrix:  # the last graph
            G = adj_matrix_to_nx(matrix)
            graphs.append(G)
    return graphs

def adj_matrix_to_nx(matrix):
    n = len(matrix)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j]:
                G.add_edge(i, j)
    return G

def deduplicate_graphs(graphs):
    unique_graphs = []
    for G in graphs:
        if not any(nx.is_isomorphic(G, H) for H in unique_graphs):
            unique_graphs.append(G)
    return unique_graphs

def save_graphs_to_file(graphs, filename):
    with open(filename, 'w') as f:
        for G in graphs:
            adj = nx.to_numpy_array(G, dtype=int)
            for row in adj:
                f.write(' '.join(map(str, row)) + '\n')
            f.write('\n')

def dedup_tight_file(l1, l2, n):
    in_file = f"tight_{l1}{l2}_{n}.txt"
    out_file = f"tight_{l1}{l2}_{n}_dedup.txt"

    graphs = read_graphs_from_file(in_file)
    unique_graphs = deduplicate_graphs(graphs)
    save_graphs_to_file(unique_graphs, out_file)

    print(f"Input graphs: {len(graphs)}, Unique (non-isomorphic): {len(unique_graphs)}")



def dedup_exceed_file(l1, l2, n):
    in_file = f"exceed_{l1}{l2}_{n}.txt"
    out_file = f"exceed_{l1}{l2}_{n}_dedup.txt"

    if not os.path.exists(in_file):
        print(f"[SKIP] {in_file} does not exist. No exceed-graphs to deduplicate.")
        return

    graphs = read_graphs_from_file(in_file)
    unique_graphs = deduplicate_graphs(graphs)
    save_graphs_to_file(unique_graphs, out_file)

    print(f"[EXCEED] n={n}, type={l1}{l2}: Input={len(graphs)}, Unique={len(unique_graphs)}")
