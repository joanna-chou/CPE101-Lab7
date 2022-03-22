#list comprehension tests
import unittest
from list_comp import *
from objects import *

class TestCases(unittest.TestCase):
   #do not delete this part, use this to comapre two lists
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_distance_all(self):
      points1 = [Point(1,2), Point(3,5)]
      points2 = [Point(2,7.5), Point(-2,44), Point(0,0)]
      points3 = [Point(3,9), Point(-1,6)]
      self.assertListAlmostEqual(point_distance_all(points1), [2.2360679774998, 5.8309518948453])
      self.assertListAlmostEqual(point_distance_all(points2), [7.76208734813, 44.04543109109, 0])
      self.assertListAlmostEqual(point_distance_all(points3), [9.486832980505138, 6.082762530298219])

   def test_are_in_first_quadrant(self):
      points1 = [Point(1,2), Point(3,-5)]
      points2 = [Point(2,7.5), Point(-2,44), Point(0,0)]
      points3 = [Point(3,9), Point(-1,6)]
      self.assertListAlmostEqual(are_in_first_quadrant(points1), [Point(1,2)])
      self.assertListAlmostEqual(are_in_first_quadrant(points2), [Point(2,7.5)])
      self.assertListAlmostEqual(are_in_first_quadrant(points3), [Point(3,9)])

   def test_circle_distance_all(self):
      circles1 = [Circle(Point(1,2),4), Circle(Point(3,5),2)]
      circles2 = [Circle(Point(-1,2.4),4)]
      circles3 = [Circle(Point(3,-4),0.3), Circle(Point(0,0),1), Circle(Point(4,202), 50)]
      self.assertListAlmostEqual(circle_distance_all(circles1), [2.2360679774998, 5.8309518948453])
      self.assertListAlmostEqual(circle_distance_all(circles2), [2.6])
      self.assertListAlmostEqual(circle_distance_all(circles3), [5, 0, 202.0396000788])

   def test_overlaps_all(self):
      circles1 = [Circle(Point(1,2),4), Circle(Point(300,5000),2)]
      circles2 = [Circle(Point(-1,2.4),7)]
      circles3 = [Circle(Point(3,-4),0.3), Circle(Point(0,0),1), Circle(Point(4,202), 500)]
      self.assertListAlmostEqual(overlaps_all(circles1), [Circle(Point(1,2),4)])
      self.assertListAlmostEqual(overlaps_all(circles2), [Circle(Point(-1,2.4),7)])
      self.assertListAlmostEqual(overlaps_all(circles3), [Circle(Point(0,0),1), Circle(Point(4,202), 500)])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

