#  File: Geom.py
 
#  Description: Program that computes basic geometry solutions involving 
#  points and lines

#  Nate Eastwick and Caleb Campbell
 
import math
 
 
class Point (object):
  # constructor with default values for x and y coordinates
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y
 
 
  # get distance from Point obect to another Point object
  def dist (self, other):
    return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
 
 
  # create a string representation of a Point in "(x, y)" format
  def __str__ (self):
    return "(" + str(self.x) + ", " + str(self.y) + ")"
 
 
  # test for equality between two points
  def __eq__ (self, other):
    if is_equal(self.x, other.x) and is_equal(self.y, other.y):
      return True
    else:
      return False
 
 
class Line (object):
  # line is defined by two Point objects p1 and p2
  # constructor assign default values if user does not define
  # the coordinates of p1 and p2 or the two points are the same
  def __init__ (self, p1_x = 0, p1_y = 0, p2_x = 1, p2_y = 1):
    if is_equal(p1_x, p2_x) and is_equal(p1_y, p2_y):
      self.p1_x = 0
      self.p1_y = 0
      self.p2_x = 1
      self.p2_y = 1
    else:
      self.p1_x = p1_x
      self.p1_y = p1_y
      self.p2_x = p2_x
      self.p2_y = p2_y
 
 
  # returns True if the line is parallel to the x axis 
  # and False otherwise
  def is_parallel_x (self):
    return is_equal(self.p1_y, self.p2_y)
 
 
  # returns True if the line is parallel to the y axis
  # and False otherwise
  def is_parallel_y (self):
    return is_equal(self.p1_x, self.p2_x)
 
 
  # determine slope for the line
  # return float ('inf') if line is parallel to the y-axis
  def slope (self):
    if self.is_parallel_y() == True:
      return float('inf')
    elif is_equal(self.p1_y, self.p2_y):
      return 0
    else:
      return float((self.p2_y - self.p1_y) / (self.p2_x - self.p1_x))
    
 
  # determine the y-intercept of the line
  # return None if line is parallel to the y axis
  def y_intercept (self):
    if self.slope() == float('inf'):
      return None
    else:
      return self.p1_y - self.p1_x * self.slope()
 
 
  # determine the x-intercept of the line
  # return None if line is parallel to the x axis
  def x_intercept (self):
    if self.slope() == 0:
      return None
    else:
      return -self.y_intercept() / self.slope()
 
 
  # returns True if line is parallel to other and False otherwise
  def is_parallel (self, other):
    if is_equal(self.slope(), other.slope()):
      return True
    else:
      return False
 
 
  # returns True if line is perpendicular to other and False otherwise
  def is_perpendicular (self, other):
    if self.slope() == float('inf') and other.slope() == 0:
      return True
    elif other.slope() == float('inf') and self.slope() == 0:
      return True
    elif self.slope() * other.slope() == -1:
      return True
    else:
      return False
 
  # returns True if Point p is on the line or an extension of it
  # and False otherwise
  def is_on_line (self, p):
    if p.y == self.slope() * p.x + self.y_intercept():
      return True
    else:
      return False
 
 
  # determine the perpendicular distance of Point p to the line
  # return 0 if p is on the line
  def perp_dist (self, p):
    return -1
 
 
  # returns a Point object which is the intersection point of line
  # and other or None if they are parallel
  def intersection_point (self, other):
    if is_equal(self.slope(), other.slope()):
      return None
    else:
      xInt = ((other.y_intercept() - self.y_intercept()) / (self.slope() - other.slope()))
      yInt = self.slope() * xInt + self.y_intercept()
      return Point(xInt, yInt)
 
 
  # return True if two points are on the same side of the line
  # and neither points are on the line
  # return False if one or both points are on the line or both 
  # are on the same side of the line
  def on_same_side (self, p1, p2):
    p1X = p1.x
    p1Y = p1.y
    p2X = p2.x
    p2Y = p2.y
    if (p1Y > self.slope() * p1X + self.y_intercept() and
     p2Y > self.slope() * p2X + self.y_intercept()):
      return True
    elif (p1Y < self.slope() * p1X + self.y_intercept() and p2Y < self.slope() * p2X + self.y_intercept()):
      return True
    else:
      return False
 
 
  # string representation of the line - one of three cases
  # y = c if parallel to the x axis
  # x = c if parallel to the y axis
  # y = m * x + b
  def __str__ (self):
    if self.slope() == 0:
      return "y = " + str(self.y_intercept)
    elif self.slope() == float('inf'):
      return "x = " + str(self.x_intercept)
    else:
      return "y = " + str(self.slope()) + " * x " + str(self.y_intercept())
 
 
def is_equal (a, b):
  tol = 1.0e-6
  return (abs(a - b) < tol)
    
 
def main():
  # open file "geom.txt" for reading
  currentFile = open("geom.txt", "r")
 
  # read the coordinates of the first Point P
  pCoord = currentFile.readline().split('#')[0]
  pCoordX = float(pCoord.split(' ')[0])
  pCoordY = float(pCoord.split(' ')[1])
  pointP = Point(pCoordX, pCoordY)
  # read the coordinates of the second Point Q
  qCoord = currentFile.readline().split('#')[0]
  qCoordX = float(qCoord.split(' ')[0])
  qCoordY = float(qCoord.split(' ')[1])
  pointQ = Point(qCoordX, qCoordY)
  # print the coordinates of points P and Q
  print("Coordinates of P:", (pointP))
  print("Coordinates of Q:", (pointQ))
  # create line PQ
  linePQ = Line(pCoordX, pCoordY, qCoordX, qCoordY)
 
  # print distance between P and Q
  print("Distance between P and Q:", round(pointP.dist(pointQ), 2))
  # print the slope of the line PQ
  print("Slope of PQ:", linePQ.slope())
  # print the y-intercept of the line PQ
  print("Y-Intercept of PQ:", linePQ.y_intercept())
  # print the x-intercept of the line PQ
  print("X-Intercept of PQ:", linePQ.x_intercept())
 
  # read the coordinates of the third Point A
  aCoord = currentFile.readline().split('#')[0]
  aCoordX = float(aCoord.split(' ')[0])
  aCoordY = float(aCoord.split(' ')[1])
  pointA = Point(aCoordX, aCoordY)
  # read the coordinates of the fourth Point B
  bCoord = currentFile.readline().split('#')[0]
  bCoordX = float(bCoord.split(' ')[0])
  bCoordY = float(bCoord.split(' ')[1])
  pointB = Point(bCoordX, bCoordY)
  # create line AB
  lineAB = Line(aCoordX, aCoordY, bCoordX, bCoordY)
 
  # print the string representation of the line AB
  print("Line AB:", lineAB)
  # print if the lines PQ and AB are parallel or not
  if lineAB.is_parallel(linePQ) == True:
    print("PQ is parallel to AB")
  elif lineAB.is_parallel(linePQ) == False:
    print("PQ is not parallel to AB")
  # print if the lines PQ and AB (or extensions) are perpendicular or not
  if lineAB.is_perpendicular(linePQ) == True:
    print("PQ is perpendicular to AB")
  elif lineAB.is_perpendicular(linePQ) == False:
    print("PQ is not perpendicular to AB")
 
  # print coordinates of the intersection point of PQ and AB if not parallel
  if not lineAB.is_parallel(linePQ):
    print("Intersection point of PQ and AB:", lineAB.intersection_point(linePQ))
 
  # read the coordinates of the fifth Point G
  gCoord = currentFile.readline().split('#')[0]
  gCoordX = float(gCoord.split(' ')[0])
  gCoordY = float(gCoord.split(' ')[1])
  pointG = Point(gCoordX, gCoordY)
  # read the coordinates of the sixth Point H
  hCoord = currentFile.readline().split('#')[0]
  hCoordX = float(hCoord.split(' ')[0])
  hCoordY = float(hCoord.split(' ')[1])
  pointH = Point(hCoordX, hCoordY)
 
  # print if the the points G and H are on the same side of PQ
  if linePQ.on_same_side(pointG, pointH) == True:
    print("G and H are on the same side of PQ")
  elif linePQ.on_same_side(pointG, pointH) == False:
    print("G and H are not on the same side of PQ")
  # print if the the points G and H are on the same side of AB
  if lineAB.on_same_side(pointG, pointH) == True:
    print("G and H are on the same side of PQ")
  elif lineAB.on_same_side(pointG, pointH) == False:
    print("G and H are not on the same side of PQ")
 
  # close file "geom.txt"
  currentFile.close()
 
 
if __name__ == "__main__":
  main()
 
 
