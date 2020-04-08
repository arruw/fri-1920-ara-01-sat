import unittest

from src.libs.vars import enc2d, dec2d

class TestVars(unittest.TestCase):

  def test_encode_decode(self):
    n = 5
    m = 4

    for i in range(n):
      for j in range(m):
        self.assertEqual((i, j), dec2d(enc2d(i, j, m), m))

if __name__ == '__main__':
  unittest.main()
