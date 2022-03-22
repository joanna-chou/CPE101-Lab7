# Lab 7 - Classes
# 
# Name: Joanna Chou
# Instructor: S. Einakian 
# Section: 07
# Date: 2/16/2022

# 1) This class represents a 2D point and can compute the Euclidean distance between points.
from utility import epsilon_equal
from math import *

class Point:
	def __init__(self, x:int, y:int):
		self.x = x
		self.y = y
	def __eq__(self, other) -> bool:
		return epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y)
	def __repr__(self) -> str:
		return '(' + str(self.x) + ',' + str(self.y) + ')'
	# Signature: Point -> float
	def distance (self, to) -> float:
		dist = sqrt(((self.x - to.x)**2) + ((self.y-to.y)**2))
		return dist

# 2) This class represents a 2D circle and can check for overlapping circles.
class Circle:
	def __init__(self, center: Point, radius: float):
		self.center = center
		self.radius = radius
	def __eq__ (self, other) -> bool:
		return epsilon_equal(self.center.x, other.center.x) and epsilon_equal(self.center.y, other.center.y) and epsilon_equal(self.radius, other.radius)
	def __ne__ (self, other) -> bool:
		if epsilon_equal(self.center.x, other.center.x) and epsilon_equal(self.center.y, other.center.y) and epsilon_equal(self.radius, other.radius) == True:
			return False
		else:
			return True
	def __repr__ (self) -> str:
		return str(self.radius) + " @ (" + str(self.center.x) + ", " + str(self.center.y) + ")"
	# Signature: Circle -> bool
	def overlaps(self, other) -> bool:
		dist = sqrt(((self.center.x - other.center.x)**2) + ((self.center.y-other.center.y)**2))
		radii = self.radius + other.radius
		if dist < radii:
			return True
		else:
			return False