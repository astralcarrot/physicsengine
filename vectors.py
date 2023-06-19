# class vector
# contains an x and y component and a bunch of different vector operations

# TO DO: create a function that convert between these vectors and pygane coordinates

import transforms

class vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __str__(self):
    return f'vector = {self.x}, {self.y}'

zero = vector(0,0)

# VECTOR OPERATIONS

def transform(v : vector, t : transforms.transform):
  return vector(t.cos * v.x - t.sin * v.y + t.positionx, t.sin * v.x + t.cos * v.y + t.positiony)

def addvec(a : vector, b : vector):
  return vector(a.x + b.x, a.y + b.y)

def subvec(a : vector, b : vector):
  return vector(a.x - b.x, a.y - b.y)

def mltvec(v : vector, s : float): # multiplies a vector by a scalar quantity
  return vector(v.x * s, v.y * s)

def divvec(v : vector, s : float): # divides a vector by a scalar quantity
  return vector(v.x / s, v.y / s)

def negate(v : vector): # negates a vector
  return vector(-v.x, -v.y)

def equal(a : vector, b : vector):
  return a.x == b.x and a.y == b.y