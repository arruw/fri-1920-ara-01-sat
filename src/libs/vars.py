from math import floor
from typing import Tuple


# n = 4
#  |0 1 2 3 j
# -----------
# 0|1 2 3 4
# 1|5 6 7 8
# 2|...
# 3|
# i|


def enc2d(i: int, j: int, n: int) -> int:
  """
  Encoded parameters (i, j)
  """
  return n*i+j+1


def dec2d(var: int, n: int) -> Tuple[int, int]:
  """
  Decode parameters (i, j)
  """
  var -= 1
  i = floor(var / n)
  j = var % n
  return (i, j)
