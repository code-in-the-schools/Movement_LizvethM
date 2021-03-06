import pygame
import os

img_path = os.path.join('chibi.png')

class Character(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    Character.image = pygame.image.load("chibi.png")
    self.image = Character.image
#    self.image = pygame.transform.scale(self.image(50,50))

    self.x = 50
    self.y = 50
    self.hitbox = (self.x,self.y,55, 55)

  def draw(self, surface):
    surface.blit(self.image,(self.x,self.y))

  def movement(self):
    key = pygame.key.get_pressed()

    if key[pygame.k_DOWN]:
      self.y -= 1
    if key[pygame.k_UP]:
      self.y += 1
    if key[pygame.k_LEFT]:
      self.x += 1
    if key[pygame.k_Right]:
      self.x -=1 
      


pygame.init()
screen_width =600
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

sprite = Character()
clock = pygame.time.Clock()

running = True

while running:
  for event in pygame.event.get():
    if event.type== pygame.QUIT:
      pygame.quit()
      running= False

  screen.fill((255,255,255))

  Character.movement(sprite)

  sprite.draw(screen)

  pygame.display.update()
  
  clock.tick(60)


