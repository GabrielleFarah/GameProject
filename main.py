
#import Py game

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame

pygame.init()
#create  window
SCREEN_WIDTH = 1366  
SCREEN_HEIGHT = 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SharkArcade101")
font = pygame.font.SysFont("comicSans", 57)
TEXT_COL = (250, 250, 250)
#Load all buttons

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#loop
run = True
while run:
  screen.fill((0, 0, 102))
  #eventleader
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        Menu = True
    if event.type == pygame.QUIT:
      run = False
  draw_text("Hello and welcome to SharkArcade101", font, TEXT_COL, 160, 250)

  pygame.display.update()

pygame.quit()
screen.fill((255,0,0))
pygame.display.update()

class Button1:
    def __init__(self, text,  pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)


