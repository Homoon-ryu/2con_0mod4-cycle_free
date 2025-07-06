import networkx as nx
import itertools

def has_cycle_length_mod4(G):
    """
    checks only 4-cycles to reduce computing time.
    """
    nodes = list(G.nodes)
    n = len(nodes)

    for i in range(n):
        v = nodes[i]
        rest = [x for x in nodes if x > v]

        for p, q, r in itertools.permutations(rest, 3):
            if (G.has_edge(v, p) and
                G.has_edge(p, q) and
                G.has_edge(q, r) and
                G.has_edge(r, v)):
                return True

    return False

import itertools

def has_8_cycle_exact(G):
    """
    checks if there is an 8-cycles in a graph.
    """
    nodes = list(G.nodes)
    n = len(nodes)

    for i in range(n):
        v = nodes[i]
        rest = [x for x in nodes if x > v]

        for path in itertools.permutations(rest, 7):  # p1 ~ p7
            if (G.has_edge(v, path[0]) and
                all(G.has_edge(path[i], path[i+1]) for i in range(6)) and
                G.has_edge(path[6], v)):
                return True
    return False



def has_path_between_mod4(G, v1, v2, target_mod, max_len=10):
    """
    Check if there exists a (v1,v2)-path of length ≡ target_mod mod 4.
    """
    if v1 == v2:
        return False

    try:
        for path in nx.all_simple_paths(G, source=v1, target=v2, cutoff=max_len):
            if (len(path) - 1) % 4 == target_mod:
                return True
        return False
    except nx.NetworkXNoPath:
        return False

def has_vertex_deg_le_1(G):
    """
    Check if there exists a vertex with degree ≤ 1.
    """
    return any(G.degree(v) <= 1 for v in G.nodes)
