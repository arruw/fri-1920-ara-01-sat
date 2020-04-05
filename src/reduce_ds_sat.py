import sys
from typing import List, Tuple
from src.libs.cnf import equal_one_cnf, less_equal_one_cnf, print_cnf_sat
from src.libs.graph import read_dimacs_graph
from networkx import Graph

def reduce_ds_sat(G, k: int) -> Tuple[int, List[List[int]]]:
  return (0, [])





# if __name__ == "__main__":
#   graphFile = sys.argv[1]
#   k = int(sys.argv[2])
#   sat_result = reduce_ds_sat(read_dimacs_graph(graphFile), k)
#   print_cnf_sat(sat_result)

read_dimacs_graph('input/g2.col')