import sys
import matplotlib.pyplot as plt
import networkx as nx

from typing import List, Tuple
from src.libs.cnf import equal_one_cnf, less_equal_one_cnf, print_cnf_sat
from src.libs.graph import read_dimacs_graph
from networkx.algorithms.approximation.clique import large_clique_size

def reduce_clique_sat(G: nx.Graph, k: int) -> Tuple[int, List[List[int]]]:
  """
  Reduce clique problem to SAT, for graph G = <V, E> check if graph contains clique of size >= k
  """
  n = G.number_of_nodes()
  clauses: List[List[int]] = []

  # point 1
  clauses += [[var(i,r,k) for i in range(n)] for r in range(k)]

  # point 2
  for i in range(n):
    for s in range(k):
      clauses += [[-var(i,r,k), -var(i,s,k)] for r in range(s)]

  # point 3
  for r in range(k):
    for s in range(k):
      if s == k: continue
      for j in range(n):
        for i in range(j):
          if G.has_edge(i, j): continue
          clauses.append([-var(i,r,k), -var(j,s,k)])

  return (n*k, clauses)


def var(i: int, r: int, k: int) -> int:
  """
  Return variable name
  """
  return k*i+r+1


if __name__ == "__main__":
  graphFile = sys.argv[1]
  k = int(sys.argv[2])
  sat_result = reduce_clique_sat(read_dimacs_graph(graphFile), k)
  print_cnf_sat(sat_result)

# G = read_dimacs_graph('input/g2.col')
# cs = large_clique_size(G)
# print(cs)

# # sat_result = reduce_clique_sat(G, 3)
# # print_cnf_sat(sat_result)

# # nx.draw(G, with_labels=True)
# # plt.show()