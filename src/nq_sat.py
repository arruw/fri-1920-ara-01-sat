import sys
from typing import List, Tuple
from src.libs.cnf import equal_one_cnf, less_equal_one_cnf, print_cnf_sat


def nq_sat(n: int) -> Tuple[int, List[List[int]]]:
  clause: List[List[int]] = []
  for x in range(n):
    # rows & columns
    clause += equal_one_cnf([var(x, j, n) for j in range(n)])
    clause += equal_one_cnf([var(i, x, n) for i in range(n)])
    # diagonals
    for d in diagonals(n):
      clause += less_equal_one_cnf(d)

  return n*n, clause


def var(i: int, j: int, n: int) -> int:
  """
  Return variable name computed from the index pair (i, j)
  """
  return n*i+j+1


def diagonals(n: int) -> List[List[int]]:
  d = []
  for x in range(n):
    d.append([var(x+j, j, n) for j in range(n) if x+j <  n])
    d.append([var(i, x+i, n) for i in range(n) if x+i <  n])
    d.append([var(n-1-j-x, j, n) for j in range(n) if n-1-j-x >= 0])
    d.append([var(i+x, n-1-i, n) for i in range(n) if n-1-i >= 0 and i+x < n])
  return d

if __name__ == "__main__":
  n = int(sys.argv[1])
  sat_result = nq_sat(n)
  print_cnf_sat(sat_result)
