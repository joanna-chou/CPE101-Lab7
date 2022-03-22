#object tests
import unittest
from objects import *

class TestCases(unittest.TestCase):
   def test_point(self):
      p1 = Point(1,2)
      p2 = Point(3,5)
      p3 = Point(1.22,6)

      self.assertEqual(p1.x, 1)
      self.assertEqual(p2.y, 5)
      self.assertEqual(p3.x, 1.22)

      self.assertEqual(p1.__repr__(), '(1,2)')
      self.assertEqual(p2.__repr__(), '(3,5)')
      self.assertEqual(p3.__repr__(), '(1.22,6)')

      self.assertEqual(p1.__eq__(p3), False)
      self.assertEqual(p2.__eq__(p2), True)
      self.assertEqual(p3.__eq__(p2), False)

      self.assertAlmostEqual(p1.distance(p2), 3.605551275464)
      self.assertAlmostEqual(p2.distance(p3), 2.0416659863944)
      self.assertAlmostEqual(p3.distance(p3), 0.0)

   def test_circle(self):
      circle1 = Circle(Point(3,3), 5.2)
      circle2 = Circle(Point(10,13), 3)
      circle3 = Circle(Point(1,5), 10.6)
      circle4 = Circle(Point(3,3), 5.2)

      self.assertEqual(circle1.center.x, 3)
      self.assertEqual(circle2.center.y, 13)
      self.assertEqual(circle3.radius, 10.6)

      self.assertEqual(circle1.__repr__(), "5.2 @ (3, 3)")
      self.assertEqual(circle2.__repr__(), "3 @ (10, 13)")
      self.assertEqual(circle3.__repr__(), "10.6 @ (1, 5)")

      self.assertEqual(circle1.__eq__(circle4), True)
      self.assertEqual(circle2.__eq__(circle3), False)
      self.assertEqual(circle3.__eq__(circle4), False)

      self.assertEqual(circle1.__ne__(circle4), False)
      self.assertEqual(circle2.__ne__(circle3), True)
      self.assertEqual(circle3.__ne__(circle4), True)

      self.assertEqual(circle1.overlaps(circle3), True)
      self.assertEqual(circle2.overlaps(circle3), True)
      self.assertEqual(circle2.overlaps(circle4), False)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

