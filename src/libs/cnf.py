from typing import List, Tuple

def equal_one_cnf(variables: List[int]) -> List[List[int]]:
  """
  Only 1 variable must be set
  """
  return less_equal_one_cnf(variables) + [variables]


def less_equal_one_cnf(variables: List[int]) -> List[List[int]]:
  """
  At most 1 variable can be set
  """
  from itertools import combinations
  def invers(i: int) -> int:
    return i*-1
  clauses = list(map(list, combinations(map(invers, variables), 2)))
  return clauses


def print_cnf_sat(sat: Tuple[int, List[List[int]]]):
  """
  Print SAT clauses in the CNF DIMACS format.
  """
  n, clause = sat
  print(f'p cnf {n} {len(clause)}')
  for c in clause:
    print(*[*c, 0], sep=' ')