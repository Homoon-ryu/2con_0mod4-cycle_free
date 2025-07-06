from dedup_tight_graphs import read_graphs_from_file, save_graphs_to_file
from graph_utils import has_8_cycle_exact  
import os

def filter_out_8cycle_graphs(filename):
    if not os.path.exists(filename):
        print(f"[SKIP] {filename} does not exist.")
        return

    graphs = read_graphs_from_file(filename)
    filtered = [G for G in graphs if not has_8_cycle_exact(G)]

    out_file = filename.replace(".txt", "_noC8.txt")
    save_graphs_to_file(filtered, out_file)

    print(f"[8CYCLE] {filename} → {out_file} (kept {len(filtered)} / {len(graphs)} graphs)")
