import sys
import pygame

pygame.init()

# Window Set up
HEIGHT = 700
WIDTH = 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paint')
win.fill(pygame.Color('white'))

# Knapp set up
clear_button = pygame.image.load('clear_button2.png')
clear_button = pygame.transform.scale(clear_button, (90, 50))

# Definiera färger
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SKIN = (255, 220, 177)

färg = BLACK

# Färg set up
färg_radius = 10


while True:
  keys = pygame.key.get_pressed()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

   # Kolla om musknappen trycks ned
    if event.type == pygame.MOUSEBUTTONDOWN:
        if clear_button.get_rect(topleft=(20, 20)).collidepoint(event.pos):
            # Sudar allt på skärmen
            win.fill((255, 255, 255))


  # Ändrar färgen
  if keys[pygame.K_1]:
    färg = BLACK
  if keys[pygame.K_2]:
    färg = WHITE
  if keys[pygame.K_3]:
    färg = BLUE
  if keys[pygame.K_4]:
    färg = RED
  if keys[pygame.K_5]:
    färg = YELLOW
  if keys[pygame.K_6]:
    färg = GREEN
  if keys[pygame.K_7]:
    färg = SKIN
  
  # hämtar musens x,y position
  mouse_x, mouse_y = pygame.mouse.get_pos()

  # Målar saker på skärmen
  win.blit(clear_button, (20, 20))
  if pygame.mouse.get_pressed()[0]:
    pygame.draw.circle(win, färg, (mouse_x, mouse_y), färg_radius)


  pygame.display.update()
