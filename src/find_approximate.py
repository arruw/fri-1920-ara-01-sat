from networkx.algorithms.approximation.dominating_set import min_weighted_dominating_set
from src.libs.graph import read_dimacs_graph

inputs = [
  'input/g2.col',
  'input/g3.col',
  'input/g1.col',
  'input/g5.col',
  'input/g4.col',
]

for path in inputs:
  print(f'Reading graph {path} ...')
  G = read_dimacs_graph(path)
  print('Finding min dominanting set approximation ...')
  DS = min_weighted_dominating_set(G)
  print(f'Set size: {len(DS)}')
  print()