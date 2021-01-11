from directions import Direction
from grid import Grid
import os
import sys
import pygame
import pygame.freetype
import colors
from pygame.locals import *

pygame.init()
if not pygame.font:
    print('Warning, fonts disabled')

pygame.mouse.set_visible(1)
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('2048')
pygame.mouse.set_visible(0)
background = pygame.Surface(screen.get_size())
background.fill(colors.hex2rgb(colors.BACKGROUND))
screen.blit(background, (0, 0))

clock = pygame.time.Clock()

def main():
    grid = Grid()

    while True:
        clock.tick(60)
        if not grid.is_alive():
            return

        for event in pygame.event.get():
            if event.type == QUIT:
                return

            if event.type == KEYDOWN and event.key == K_UP:
                grid.move(Direction.UP)
            elif event.type == KEYDOWN and event.key == K_DOWN:
                grid.move(Direction.DOWN)
            elif event.type == KEYDOWN and event.key == K_LEFT:
                grid.move(Direction.LEFT)
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                grid.move(Direction.RIGHT)
        
        screen.blit(background, (0, 0))
        grid.draw(screen)
        pygame.display.flip()

main()
