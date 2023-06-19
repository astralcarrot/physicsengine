# will contain main loop
# contains code for displaying everything on screen
# zoom functionality is pretty cool, try adding that!

# time to start developing some actual graphics for this thing
# currently on episode 7, 7:30

import pygame
import random
import rigidbody
import vectors
import collisions

pygame.init()

xsize, ysize = 300, 300

# create the display surface object
window = pygame.display.set_mode((xsize, ysize))
 
# creating a list of all the rigidbodies in the scene

numrbs =  5
rbradius = 10

rbs = [rigidbody.rigidbody.createCircleBody(rbradius, vectors.vector(random.randint(10,xsize-10), random.randint(10,ysize-10)), 1, 0, 0) for i in range(numrbs)]

boxes = [rigidbody.rigidbody.createBoxBody(20, 20, vectors.vector(random.randint(10,xsize-10), random.randint(10,ysize-10)), 1, 0, 1) for i in range(numrbs)]

# print(boxes)

x = 50
y = 50
radius = 10
vel = 10
gravity = 8

# player = rigidbody.rigidbody.createCircleBody(radius, vectors.vector(x, y), 1, 0, 1)

player = rigidbody.rigidbody.createBoxBody(10, 10, vectors.vector(x, y), 1, 0, 1)

run = True

# use vector positions instead of pygame pixel coordinates, and use rigidbody class. pygame ONLY used to draw graphics

# loop through all rigidbody objects and update positions accordingly after calculating collisions

while run:
  pygame.time.delay(100)

  for i in boxes:
    print(i.pos)
  print('player', player.pos)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  # priority: first movement should be calculated, then collisions

  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT]:
    player.pos.x -= vel

  if keys[pygame.K_RIGHT]:
    player.pos.x += vel

  if keys[pygame.K_UP]:
    player.pos.y -= vel

  if keys[pygame.K_DOWN]:
    player.pos.y += vel

  window.fill((0,40,140)) # 0,40,140

  # circle collisions
  # block out all of this for later
  if False:
  # inefficient "brute force" collision detection
    for i in rbs:
      # if i.pos.y <= rbradius + ysize -40:
      #   i.move(vectors.vector(0, gravity))
      for j in rbs:
        out = collisions.collisions.intersectionCircles(player.pos, radius, i.pos, 10)
        # print(out)
        out2 = collisions.collisions.intersectionCircles(j.pos, 10, i.pos, 10)
        
        if out:
          # print(out)
          player.move(vectors.mltvec(vectors.negate(out[0]), out[1] / 2)) # [player]
          i.move(vectors.mltvec(out[0], out[1] / 2))
        if out2:
          # print(out2)
          try:
            j.move(vectors.mltvec(vectors.negate(out2[0]), out2[1] / 2))
            i.move(vectors.mltvec(out2[0], out2[1] / 2))
          except: continue
    
        #pygame.draw.circle(window, (255,43,18), [i.pos.x, i.pos.y], i.radius, 0)
        if i.type == 'circle':
          pygame.draw.circle(window, (255,43,18), [i.pos.x, i.pos.y], i.radius, 0)
          pygame.draw.circle(window, (0,0,0), [i.pos.x, i.pos.y], i.radius, 1)


  # polygon collisions
  if True:
    for i in boxes:
      for j in boxes:
        
        out = collisions.collisions.intersectionPolygons(player.getTransformedVertices(), i.getTransformedVertices())
        # print(out)
        out2 = collisions.collisions.intersectionPolygons(j.getTransformedVertices(), i.getTransformedVertices())
        # print(out2)

        # try:
        if out: 
          print('collision of player')
          
          player.move(vectors.mltvec(vectors.negate(out[0]), out[1] / 2)) # [player]
          i.move(vectors.mltvec(out[0], out[1] / 2))
        if out2: #print('other collision', out2)
          
          j.move(vectors.mltvec(vectors.negate(out2[0]), out2[1] / 2))
          i.move(vectors.mltvec(out2[0], out2[1] / 2))
        # except: pass
          
        if j.type == 'circle': # circle with outline
          pygame.draw.circle(window, (255,43,18), [j.pos.x, j.pos.y], j.radius, 0)
          pygame.draw.circle(window, (0,0,0), [j.pos.x, j.pos.y], j.radius, 1)
        elif j.type == 'box':
          pts = [(i.x, i.y) for i in j.getTransformedVertices()]
          pygame.draw.polygon(window, (255,43,18), pts) # should be the moved vertices
      
  pygame.draw.circle(window, [255,255,255], [player.pos.x, player.pos.y], radius, 0)
  pygame.draw.circle(window, [0,0,0], [player.pos.x, player.pos.y], radius, 1)

#  pygame.draw.rect(window, [255, 255, 255], player.transformedVertices)

  # print(player.pos)

  pygame.display.update()

pygame.quit()