import pygame
import sys

physics_world = []


def init(W, H, T):
    global height
    height = H
    global width
    width = W
    global window
    global clock
    window = pygame.display.set_mode((W, H))
    pygame.display.set_caption(T)
    clock = pygame.time.Clock()

def update():
    global width
    global height
    global physics_world
    global window
    global clock
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        window.fill((255, 255, 255))

        for PhysObj in physics_world:
            PhysObj.draw(pygame, window, width, height)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()
    sys.exit(0)