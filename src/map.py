import sys
import matplotlib.pyplot as plt
import networkx as nx
from src.libs.vars import dec2d

if __name__ == "__main__":
  n = int(sys.argv[1])
  if 's UNSATISFIABLE' == input().strip(): exit(0)
  
  print()
  print('MAP (enc => dec):')
  for var in map(int, input()[1:-1].strip().split(' ')):
    if var <= 0: continue
    print(f'{var} => {dec2d(var, n)}')
  exit(0)