import vectors
import vmath
import math

# collision detection and resolution
# NOTE: must manually add the conditional statement to force the bodies apart
# move both bodies in equal and opposite directions, cuz of Newton's third law
class collisions:
  # collisions done using the "separating axis theorem"
  # returns a boolean which states whether there is an intersection or not
  def intersectionCircles(centerA : vectors.vector, radiusA, centerB : vectors.vector, radiusB):
    # returns a boolean which states whether there is an intersection or not
    distance = vmath.distance(centerA, centerB)
    radii = radiusA + radiusB

    if distance < radii:
      normal = vmath.normalize(vectors.subvec(centerB, centerA))
      depth = (radii - distance)
  
      return [normal, depth]

  # uses separating axis theorem, checks if there is separation along any of the axis
  # returns a depth and normal vector

  def projectVertices(vertices : list , axis : vectors.vector): # vertices -> list of vectors
    proj = []
    
    for i in range(len(vertices)):
      v = vertices[i]
      proj.append(vmath.dot(v, axis))

    return min(proj), max(proj)

  def arithmeticmean(vertices : list): # list of vectors
    sumx = 0
    sumy = 0
    length = len(vertices)
    
    for i in vertices:
      sumx += i.x
      sumy += i.y

    return vectors.vector(sumx / length, sumy / length)
  
  def intersectionPolygons(verticesA : list, verticesB : list): # transformed vertices, so they're lists (wait vectors????)

    normal = vectors.zero
    depth = 0
    
    for i in range(len(verticesA)-1):
      va = verticesA[i] # verticesA[i][0], verticesA[i][1]
      vb = verticesA[(i+1)] #  (i+1) % len(verticesA)][0], verticesA[ (i+1) % len(verticesA)][1]

      edge = vectors.subvec(va, vb)
      axis = vectors.vector(-edge.y, edge.x)
  
      minA, maxA = collisions.projectVertices(verticesA, axis)
      minB, maxB = collisions.projectVertices(verticesB, axis)

      if minA >= maxB or minB >= maxA: # are they overlapping?
        return False # these are separated along this axis

      # occurs if there are no gaps
      axisDepth = min(minA - maxB, minA - maxB)
  
      if axisDepth < depth:
        depth = axisDepth
        normal = axis

    # second loop identcal to first except it compares the verticesB
    for i in range(len(verticesB)):
      va = verticesB[i]
      vb = verticesB[ (i+1) % len(verticesB)]

      edge = vectors.subvec(va, vb)
      axis = vectors.vector(-edge.y, edge.x)
  
      minA, maxA = collisions.projectVertices(verticesA, axis)
      minB, maxB = collisions.projectVertices(verticesB, axis)

      if minA >= maxB or minB >= maxA: # are they overlapping?
        return [False, False] # these are separated along this axis

      # occurs if there are no gaps
      axisDepth = min(minA - maxB, minA - maxB)
  
      if axisDepth < depth:
        depth = axisDepth
        normal = axis
    
    try:
      centerA = collisions.arithmeticmean(verticesA)
      centerB = collisions.arithmeticmean(verticesB)
      direction = vectors.subvec(centerB - centerA)
      depth /= vmath.length(normal)
      normal = vmath.normalize(normal)
      
      if vmath.dot(direction, normal) < 0: # check if the dot is negative, meaning the shadow of the vector is not overtop the other and therefore not same direction
        normal = vectors.negate(normal)
    
    except : pass

    if depth > 0:
      return [normal, depth]
    # else:
    #   return [False, False]