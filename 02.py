import sys, pygame  
pygame.init()
size = width, height = 1200, 800  
speed = [5, 2]
black = 249, 130, 57
screen = pygame.display.set_mode(size)
ball = pygame.image.load('12320170924195020.png')
ballrect = ball.get_rect()
while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
  ballrect = ballrect.move(speed)
  if ballrect.left < 0 or ballrect.right > width:
    speed[0] = -speed[0]
  if ballrect.top < 0 or ballrect.bottom > height:
    speed[1] = - speed[1]
  screen.fill(black)
  screen.blit(ball, ballrect)
  pygame.display.flip()



