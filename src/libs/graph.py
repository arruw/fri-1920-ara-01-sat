from typing import Tuple
from operator import itemgetter
from networkx import Graph


def read_dimacs_graph(filePath: str) -> Graph:
  """
  Construct Networkx graph from dimacs graph file.
  """
  def transform(line: str) -> Tuple[int]:
    _, i, j = line.rstrip().split(' ')
    return (int(i), int(j))

  with open(filePath) as f:
    lines = f.readlines()

  edges = list(map(transform, lines[1:]))

  G = Graph()
  G.add_edges_from(edges)

  return G