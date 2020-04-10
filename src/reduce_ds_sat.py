import sys
import os
import networkx as nx

from typing import List, Tuple
from src.libs.cnf import print_cnf_sat
from src.libs.graph import read_dimacs_graph
from src.reduce_vc_sat import reduce_vc_sat

def reduce_ds_sat(G: nx.Graph, k: int) -> Tuple[int, List[List[int]]]:
  """
  Reduce dominanting set problem to SAT
  """
  
  # Generate proxy nodes
  x = G.number_of_nodes() + 1
  newEdges = []
  for i, j in G.edges():
    newEdges += [(i, x), (x, j)]
    x += 1
  G.add_edges_from(newEdges)

  # Solve vertex cover problem
  return reduce_vc_sat(G, k)


if __name__ == "__main__" and os.getenv("DEBUG", "false") != "true":
  graphFile = sys.argv[1]
  k = int(sys.argv[2])
  sat_result = reduce_ds_sat(read_dimacs_graph(graphFile), k)
  print_cnf_sat(sat_result)
else:
  # DEBUG mode
  sat_result = reduce_ds_sat(read_dimacs_graph("input/test_rocket.col"), 2)
  print_cnf_sat(sat_result)
