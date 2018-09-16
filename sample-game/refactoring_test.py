import unittest
from refactoring import check_hero

class Test_check_friend(unittest.TestCase):

  def test_return_normal_number(self):
    self.assertEqual(check_hero('勇者', 16), True)
    # self.assertEqual(check_hero('勇者', 16), (True, 'では魔王を退治してきてください'))

if __name__ == '__main__':
  unittest.main()