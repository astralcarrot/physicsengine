import vectors
import math

class transform:
  # TWO WAYS to define a transform so make a way to make the object out of both?
  def __init__(self, x, y, angle):
    self.positionx = x
    self.positiony = y
    self.sin = math.sin(angle)
    self.cos = math.cos(angle)