import pygame
from hiragana import *
import spritesheet
from random import shuffle
from pygame_textinput import *
import time

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Hiragana Flash Cards")
screen.fill((255, 255, 255))
deckcount=0
shuffle(deck)
print(len(deck))
ss=spritesheet.spritesheet('hira.gif')
correct=pygame.image.load('Correct.jpeg').convert()
tryagain=pygame.image.load("Try-Again.jpeg").convert()
N=ss.image_at((deck[deckcount].X, deck[deckcount].Y, 78, 80))
textinput=TextInput("","bitstreamverasans",35)
screen.blit(N, (300, 100))

pygame.display.flip()

clock = pygame.time.Clock()
while True:
    screen.fill((255, 255, 255))
    screen.blit(N, (300, 100))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    # Feed it with events every frame

    # Blit its surface onto the screen
    screen.blit(textinput.get_surface(), (325, 300))
    if textinput.update(events):
        if textinput.get_text()==deck[deckcount].Name:
            print("correct!")
            screen.blit(correct, (400, 100))
            pygame.display.flip()
            time.sleep(1.5)
            deckcount+=1
            if deckcount>47:
                shuffle(deck)
                deckcount=0
            N = ss.image_at((deck[deckcount].X, deck[deckcount].Y, 78, 80))
            screen.fill((255, 255, 255))
            screen.blit(N, (300, 100))

            textinput = TextInput("", "bitstreamverasans", 35)
            pygame.display.flip()

        else:
            print("Try Again")

            textinput = TextInput("", "bitstreamverasans", 35)
            screen.blit(tryagain, (400, 100))
            pygame.display.flip()
            time.sleep(1.5)


    pygame.display.update()
    clock.tick(30)


