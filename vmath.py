# vector math module

from vectors import vector
import vectors
import math

def clamp(val, min, max):
  if min == max:
    return min
  if min > max:
    print('min is greater than the max')

  if val < min:
    return min

  if val > max:
    return max

  return val

def length(v : vector): # try length squared for optimization
  return math.sqrt(v.x**2 + v.y**2)
  
def distance(a : vector, b : vector) -> float: # distance squared for optimization
  return math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)

# FIX THIS because I think it's breaking the pushing stuff
def normalize(v : vector): # returns a vector with the same direction, but different magnitude
  vlen = length(v)
  if vlen:
    return vector(v.x / vlen, v.y / vlen)

def dot(a : vector, b : vector): # dot product of vectors
  return a.x * b.x + a.y * b.y

def cross(a : vector, b : vector): # only calculates cz because az and bz are 0, so cx and cy are 0
  return a.x*b.y - a.y*b.x