#nested list tests
import unittest
from nested_list import *

class TestCases(unittest.TestCase):
   def test_groups_of_3(self):
      self.assertEqual(groups_of_3([1,2,3,4,5,6,7,8,9]),[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
      self.assertEqual(groups_of_3([3,4,5,10,22,5,6,7]),[[3,4,5], [10,22,5], [6,7]])
      self.assertEqual(groups_of_3([0,-4]),[[0,-4]])
   def test_final_value(self):
      self.assertEqual(final_value([[-1,12,3], [8], [], [1,-3]]),[3, 8,-3])
      self.assertEqual(final_value([[0,2,5], [1,2222,34,0], [423432], []]),[5,0,423432])
      self.assertEqual(final_value([[],[],[],[]]),[])
   def test_repeat_value(self):
      self.assertEqual(repeat_value([1,5,3,0]),[[1],[5,5,5,5,5],[3,3,3],[]])
      self.assertEqual(repeat_value([1,2,3]), [[1],[2,2],[3,3,3]])
      self.assertEqual(repeat_value([12, 0]), [[12,12,12,12,12,12,12,12,12,12,12,12],[]])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()