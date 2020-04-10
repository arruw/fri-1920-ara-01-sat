import sys
import os
from src.libs.vars import dec2d
from typing import List
from functools import reduce
from operator import add


def parseVariables(lines: List[str]):
  def extract(x: List[str]) -> List[int]:
    return list(map(int, x[2:].split(' ')))

  if len(lines) <= 1:
    return None

  return list(reduce(add, map(extract, lines[1:])))


def main(n, path):
  with open(path) as f:
    lines = list(map(lambda x: x.rstrip(), f.readlines()))

  variables = parseVariables(lines)
  if not variables: exit(0)

  print()
  print('MAP (enc => dec):')
  for var in variables:
    if var <= 0: continue
    print(f'{var} => {dec2d(var, n)}')
  exit(0)


if __name__ == "__main__" and os.getenv("DEBUG", "false") != "true":
  n = int(sys.argv[1])
  path = sys.argv[2]
  main(n, path)
elif __name__ == "__main__" and os.getenv("DEBUG", "false") == "true":
  # DEBUG mode
  main(3, "input/test.solution")
