import sys
from typing import List, Tuple
from src.libs.cnf import equal_one_cnf, less_equal_one_cnf, print_cnf_sat
from src.libs.vars import enc2d


def nq_sat(n: int) -> Tuple[int, List[List[int]]]:
  """
  Generate list of CNF clauses to solve N-queens problem
  """
  clause: List[List[int]] = []
  for x in range(n):
    # rows & columns
    clause += equal_one_cnf([enc2d(x, j, n) for j in range(n)])
    clause += equal_one_cnf([enc2d(i, x, n) for i in range(n)])
    # diagonals
    for d in diagonals(n):
      clause += less_equal_one_cnf(d)

  return n*n, clause


def diagonals(n: int) -> List[List[int]]:
  """
  Return all possible diagonals
  """
  d = []
  for x in range(n):
    d.append([enc2d(x+j, j, n) for j in range(n) if x+j <  n])
    d.append([enc2d(i, x+i, n) for i in range(n) if x+i <  n])
    d.append([enc2d(n-1-j-x, j, n) for j in range(n) if n-1-j-x >= 0])
    d.append([enc2d(i+x, n-1-i, n) for i in range(n) if n-1-i >= 0 and i+x < n])
  return d


if __name__ == "__main__":
  n = int(sys.argv[1])
  sat_result = nq_sat(n)
  print_cnf_sat(sat_result)
