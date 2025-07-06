from graph_generator import generate_all_graphs_with_fixed_edges
import networkx as nx
from graph_utils import has_cycle_length_mod4, has_path_between_mod4, has_vertex_deg_le_1

def adj_to_nx_graph(adj):
    n = len(adj)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i+1, n):
            if adj[i][j]:
                G.add_edge(i, j)
    return G

def save_graphs_with_conditions(i, j, l1, l2, k, fixed_edges_fn, path_maxlen=10):
    for n in range(i, j+1):
        e_max = (3 * n - k) / 2.0
        l3 = l1 + 2 
        l4 = l2 + 2
        fixed_edges = fixed_edges_fn(n)
        filename = f"tight_{l1}{l2}_{n}.txt"
        count = 0

        with open(filename, 'a') as f:
            for adj in generate_all_graphs_with_fixed_edges(n, fixed_edges):
                # number of edges
                edge_count = sum(adj[i][j] for i in range(n) for j in range(i+1, n))

                G = adj_to_nx_graph(adj)

                # check conditions
                if has_cycle_length_mod4(G):
                    continue
                if has_path_between_mod4(G, 0, 1, l3 % 4, path_maxlen):
                    continue
                if has_path_between_mod4(G, 0, 1, l4 % 4, path_maxlen):
                    continue
                if has_vertex_deg_le_1(G):
                    continue

                if edge_count > e_max:
                    print(f"e_max might be wrong for n = {n}, type = {l1}{l2} (actual edge count = {edge_count}, e_max = {e_max})")
                    exceed_filename = f"exceed_{l1}{l2}_{n}.txt"
                    with open(exceed_filename, 'a') as ef:
                        for row in adj:
                            ef.write(' '.join(str(x) for x in row) + '\n')
                        ef.write('\n')
                    continue


                if edge_count < e_max:
                    continue
                
                # save it to a text file
                for row in adj:
                    f.write(' '.join(str(x) for x in row) + '\n')
                f.write('\n')
                count += 1

        print(f"n = {n}: saved {count} tight graphs to {filename}")
