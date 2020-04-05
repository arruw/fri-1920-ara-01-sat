import unittest

from src.reduce_nq_sat import diagonals

class TestNqSat(unittest.TestCase):

  def test_diagonals(self):
    expect = list(map(sorted, [
      [13], [9,14], [5,10,15], [1,6,11,16], [2,7,12], [3,8], [4],
      [1], [2,5], [3,6,9], [4,7,10,13], [8,11,14], [12,15], [16]
    ]))
    test = list(map(sorted, diagonals(4)))

    # not found
    for d in expect:
      self.assertIn(d, test)

    # misses
    for d in test:
      self.assertIn(d, expect)

if __name__ == '__main__':
  unittest.main()
