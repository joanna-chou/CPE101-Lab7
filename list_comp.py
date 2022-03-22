# Lab 7 - List Comprehension Functions
# 
# Name: Joanna Chou
# Instructor: S. Einakian 
# Section: 07
# Date: 2/16/2022

from objects import *

#1) This function computes the distance each point is from the origin.
def point_distance_all (points: list[Point]) -> list[float]:
    origin = Point(0,0)
    new_list = list(map(lambda point: origin.distance(point), points))
    return new_list

#2) This function returns all the points in the input lists that are in the first quadrant.
def are_in_first_quadrant(points: list[Point]) -> list[Point]:
    new_list = list(filter(lambda point: point.x > 0 and point.y > 0, points))
    return new_list

#3) This function returns a list contianing the distance from the origin to the corresponding circle in the input list.
def circle_distance_all(circles: list[Circle]) -> list[float]:
    origin = Point(0,0)
    new_list = list(map(lambda circle: origin.distance(circle.center), circles))
    return new_list

#4) This function returns a list of Cicle that overlap with the unit circle.
def overlaps_all(circles: list[Circle]) -> list[Circle]:
    unit_circle = Circle(Point(0,0), 1)
    new_list = list(filter(lambda circle: unit_circle.overlaps(circle), circles))
    return new_list

