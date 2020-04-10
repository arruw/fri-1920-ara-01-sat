import os
import sys
import subprocess

def bisection(command: str, min: int, max: int, type: str):
  pass

def solve(command: str, k: int):
  pc = subprocess.run(command.split(' '), stdout=True)
  

def main(command: str, minBound: int, maxBound: int, optType: str):
  bisection(command, minBound, maxBound, optType)


if __name__ == "__main__" and os.getenv("DEBUG", "false") != "true":
  main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
elif __name__ == "__main__" and os.getenv("DEBUG", "false") == "true":
  main("make ds_sat G=input/test_rocket.col K=2", 0, 6, "min")