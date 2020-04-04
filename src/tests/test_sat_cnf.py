import unittest

from src.libs.cnf import equal_one_cnf, less_equal_one_cnf

class TestSatCnf(unittest.TestCase):

  def test_equal_one_cnf(self):
    variables = [1,2,3]
    expected = list(map(sorted, [[-1,-2], [-1,-3], [-2,-3], [1,2,3]]))
    test = list(map(sorted, equal_one_cnf(variables)))
    
    for c in expected:
      self.assertIn(c, test)
    for c in test:
      self.assertIn(c, expected)

  def test_less_equal_one_cnf(self):
    variables = [1,2,3]
    expected = list(map(sorted, [[-1,-2], [-1,-3], [-2,-3]]))
    test = list(map(sorted, less_equal_one_cnf(variables)))
    
    for c in expected:
      self.assertIn(c, test)
    for c in test:
      self.assertIn(c, expected)

if __name__ == '__main__':
  unittest.main()
