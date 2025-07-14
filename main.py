from example_generator import save_graphs_with_conditions
from dedup_tight_graphs import dedup_tight_file, dedup_exceed_file
from filter_8cycles import filter_out_8cycle_graphs  

def main():
    test_cases = [
        # Check (A1)
        (0, 3, 6, 6, 4, lambda n: [(0,2),(2,3),(3,4),(4,1)]), 
        
        # Check (A2)
        (0, 1, 7, 7, 3, lambda n: [(0,2),(2,3),(3,4),(4,5),(5,1)]), 

        # Check (A3)
        (1, 2, 8, 8, 2, lambda n: [(0,2),(2,3),(3,4),(4,5),(5,1)]),  
        (1, 2, 8, 8, 2, lambda n: [(0,2),(2,3),(3,4),(4,5),(5,6),(6,1)]), 

        # Check (A4) and (A5)
        (2, 3, 7, 9, 3, lambda n: [(0,2),(2,3),(3,4),(4,5),(5,6),(6,1)]), 
        (2, 3, 9, 9, 3, lambda n: [(0,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,1)]), 
    ]

    for l1, l2, i, j, k, fixed_edges_fn in test_cases:
        save_graphs_with_conditions(i, j, l1, l2, k, fixed_edges_fn)

        for n in range(i, j + 1):
            dedup_tight_file(l1, l2, n)
            dedup_exceed_file(l1, l2, n)

            # delete graphs with an 8-cycle
            filter_out_8cycle_graphs(f"tight_{l1}{l2}_{n}_dedup.txt")
            filter_out_8cycle_graphs(f"exceed_{l1}{l2}_{n}_dedup.txt")

if __name__ == "__main__":
    main()
