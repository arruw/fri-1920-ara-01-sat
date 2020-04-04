import sys
from typing import List, Tuple
from libs.cnf import equal_one_cnf, less_equal_one_cnf, print_cnf_sat


def reduce_nq_sat(n: int) -> Tuple[int, List[List[int]]]:
  clause: List[List[int]] = []
  for x in range(n):
    # rows & columns
    clause += equal_one_cnf([var(x, j, n) for j in range(n)])
    clause += equal_one_cnf([var(i, x, n) for i in range(n)])
    # diagonals
    clause += less_equal_one_cnf([var(x+j, j, n) for j in range(n) if x+j <  n])
    clause += less_equal_one_cnf([var(i, x+i, n) for i in range(n) if x+i <  n])
    clause += less_equal_one_cnf([var(x-j, j, n) for j in range(n) if x-j >= 0])
    clause += less_equal_one_cnf([var(i, x-i, n) for i in range(n) if x-i >= 0])

  return n*n, clause


def var(i: int, j: int, n: int) -> int:
  """
  Return variable name computed from the index pair (i, j)
  """
  return n*i+j+1


if __name__ == "__main__":
  n = int(sys.argv[1])
  sat_result = reduce_nq_sat(n)
  print_cnf_sat(sat_result)
