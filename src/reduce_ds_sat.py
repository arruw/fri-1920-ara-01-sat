import sys
import os
import networkx as nx

from typing import List, Tuple
from src.libs.cnf import print_cnf_sat
from src.libs.vars import enc2d
from src.libs.graph import read_dimacs_graph

def reduce_ds_sat(G: nx.Graph, k: int) -> Tuple[int, List[List[int]]]:
  """
  Reduce dominanting set problem to SAT
  """
  n = G.number_of_nodes()
  clauses: List[List[int]] = []

  # point 1 - i-th node is the r-th node in the set
  clauses += [[enc2d(i,r,k) for i in range(n)] for r in range(k)]

  # point 2 - no node can appear twice in the set
  for i in range(n):
    for s in range(k):
      clauses += [[-enc2d(i,r,k), -enc2d(i,s,k)] for r in range(s)]

  # point 3 - only one node can be r-th node in the set
  for r in range(k):
    for i in range(n):
      clauses += [[-enc2d(i,r,k), -enc2d(j,r,k)] for j in range(i)]

  # point 4 - node x or one of its neighbors must be in the set
  for x in G.nodes():
    tmp = []
    for a in [x] + list(G.neighbors(x)):
      tmp += [enc2d(a,r,k) for r in range(k)]
    clauses.append(tmp)

  return (n*k, clauses)


if __name__ == "__main__" and os.getenv("DEBUG", "false") != "true":
  graphFile = sys.argv[1]
  k = int(sys.argv[2])
  sat_result = reduce_ds_sat(read_dimacs_graph(graphFile), k)
  print_cnf_sat(sat_result)
elif __name__ == "__main__" and os.getenv("DEBUG", "false") == "true":
  # DEBUG mode
  sat_result = reduce_ds_sat(read_dimacs_graph("input/test_diagonal.col"), 1)
  print_cnf_sat(sat_result)
