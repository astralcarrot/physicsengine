# rigidbody class and code and world class
import vectors
import vmath
import math
import transforms

shapeType = ['circle', 'box'] # meant to be an enum, but list is easier in python :)

class rigidbody: # rigidbody!!
  def __init__(self, pos : vectors.vector, mass, density, bounce, static, radius, width, height, type):
    
    def createBoxVertices(width, height): # creates a list of vectors to store vertices
      left = -width / 2
      right = left + width
      bottom = height / 2
      top = bottom + height
      return [vectors.vector(left, top), vectors.vector(right, top), vectors.vector(right, bottom), vectors.vector(left, bottom)]

    def createBoxTriangles(): # splitting the box up into multiple triangles, always the same so maybe jhust return the list?
      return [0, 1, 2, 0, 2, 3]

    self.type = shapeType[type]
    
    self.pos = pos # constantly pass this to graphics engine
    self.linearVelocity = 0
    self.rotation = 0
    self.rv = 0 # rotational velocity
    
    self.mass = mass
    self.density = density
    self.restitution = bounce
    self.isStatic = static
    
    self.radius = radius
    self.width = width
    self.height = height
    

    if self.type == 'box': # if it is a box type
      self.vertices = createBoxVertices(self.width, self.height)
      self.triangles = createBoxTriangles() # [0, 1, 2, 0, 2, 3] but the function may be used later
      self.transformedVertices = [] # list for transformed vertices
      
    else: # if it is another (currently just circle) type
      self.triangles = []
      self.vertices = []
      self.transformedVertices = []

    self.updaterequired = True # checks if an update to transform is required

# general rigidbody operations
  
  def move(self, amount : vectors.vector):
    self.pos = vectors.addvec(self.pos, amount) # ????
    self.updaterequired = True

  def moveTo(self, position : vectors.vector):
    self.pos = position # ????
    self.updaterequired = True

  def rotate(self, amount):
    self.rotation += amount
    self.updaterequired = True

  def getTransformedVertices(self): # speeeens the box essentially
    if self.updaterequired:
      transform = transforms.transform(self.pos.x, self.pos.y, self.rotation)
      for i in self.vertices:
        v = vectors.vector(i.x, i.y)
        self.transformedVertices.append(vectors.transform(v, transform))
    self.updaterequired = False
    return self.transformedVertices
  
  # making a circle body
  def createCircleBody(radius, pos : vectors.vector, density, static, bounce):
    # errormsg = ''
    
    area = radius**2 * math.pi
    
    if area < world.minBodySize:
      # errormsg = 'Circle area is too small. Min area is ' + str(world.minBodySize)
      return False
    elif area > world.maxBodySize:
      # errormsg = 'Circle area is too large. Max area is ' + str(world.maxBodySize)
      return False

    if density < world.minDensity:
      # errormsg = 'Density is too small. Min density is ' + str(world.minDensity)
      return False
    elif density > world.maxDensity:
      # errormsg = 'Density is too large. Max density is ' + str(world.maxDensity)
      return False

    restitution = vmath.clamp(bounce, 0, 1)
    mass = area * density

    body = rigidbody(pos, mass, density, restitution, static, radius, 0, 0, 0) # return the body if successful?
    return body

  def createBoxBody(width, height, pos : vectors.vector, density, static, bounce):
    # errormsg = ''
    
    area = width * height
    
    if area < world.minBodySize:
      # errormsg = 'Area is too small. Min area is ' + str(world.minBodySize)
      return False
    elif area > world.maxBodySize:
      # errormsg = 'Area is too large. Max area is ' + str(world.maxBodySize)
      return False
  
    if density < world.minDensity:
      # errormsg = 'Density is too small. Min density is ' + str(world.minDensity)
      return False
    elif density > world.maxDensity:
      # errormsg = 'Density is too large. Max density is ' + str(world.maxDensity)
      return False
  
    restitution = vmath.clamp(bounce, 0, 1)
    mass = area * density
  
    body = rigidbody(pos, mass, density, restitution, static, 0, width, height, 1) # return the body if successful?
    return body

# contains values about the world
class world:
  minBodySize = 0.0001
  maxBodySize = 4096

  minDensity = 0.2
  maxDensity = 21.4