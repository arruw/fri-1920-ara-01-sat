import sys
import os
import networkx as nx

from typing import List, Tuple
from src.libs.cnf import print_cnf_sat
from src.libs.graph import read_dimacs_graph
from src.libs.vars import enc2d


def reduce_clique_sat(G: nx.Graph, k: int) -> Tuple[int, List[List[int]]]:
  """
  Reduce clique problem to SAT

  Resources:
    - https://blog.computationalcomplexity.org/2006/12/reductions-to-sat.html
  """
  n = G.number_of_nodes()
  clauses: List[List[int]] = []

  # point 1
  clauses += [[enc2d(i,r,k) for i in range(n)] for r in range(k)]

  # point 2
  for i in range(n):
    for s in range(k):
      clauses += [[-enc2d(i,r,k), -enc2d(i,s,k)] for r in range(s)]

  # point 3
  for r in range(k):
    for s in range(k):
      if r == s: continue
      for j in range(n):
        for i in range(j):
          if G.has_edge(i, j) or G.has_edge(j, i): continue
          clauses.append([-enc2d(i,r,k), -enc2d(j,s,k)])

  return (n*k, clauses)


if __name__ == "__main__" and os.getenv("DEBUG", "false") != "true":
  graphFile = sys.argv[1]
  k = int(sys.argv[2])
  sat_result = reduce_clique_sat(read_dimacs_graph(graphFile), k)
  print_cnf_sat(sat_result)
elif __name__ == "__main__" and os.getenv("DEBUG", "false") == "true":
  sat_result = reduce_clique_sat(read_dimacs_graph("input/test_rocket.col"), 3)
  print_cnf_sat(sat_result)
