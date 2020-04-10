import sys
import os
import networkx as nx

from typing import List, Tuple
from src.libs.cnf import print_cnf_sat
from src.libs.graph import read_dimacs_graph
from src.libs.vars import enc2d
from functools import reduce
from operator import add


def reduce_vc_sat(G: nx.Graph, k: int) -> Tuple[int, List[List[int]]]:
  """
  Reduce vertex coverage problem to SAT
  """
  n = G.number_of_nodes()
  clauses: List[List[int]] = []

  # point 1 - i-th node is the r-th node in the set
  clauses += [[enc2d(i,r,k) for i in range(n)] for r in range(k)]

  # point 2 - no node can appear twice in the set
  for i in range(n):
    for s in range(k):
      clauses += [[-enc2d(i,r,k), -enc2d(i,s,k)] for r in range(s)]

  # point 3 - no more then one node appears in the rth position in the set
  for r in range(k):
    for i in range(n):
      clauses += [[-enc2d(i,r,k), -enc2d(j,r,k)] for j in range(i)]

  # point 4 - every edge is incident to at least one node in the set
  for i, j in G.edges():
    clauses.append(list(reduce(add, [[enc2d(i,r,k), enc2d(j,r,k)] for r in range(k)])))

  return (n*k, clauses)


if __name__ == "__main__" and os.getenv("DEBUG", "false") != "true":
  graphFile = sys.argv[1]
  k = int(sys.argv[2])
  sat_result = reduce_vc_sat(read_dimacs_graph(graphFile), k)
  print_cnf_sat(sat_result)
else:
  sat_result = reduce_vc_sat(read_dimacs_graph("input/test_rocket.col"), 3)
  print_cnf_sat(sat_result)
