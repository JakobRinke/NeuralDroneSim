import time

import pygame
import sys
import core2d
physics_world = []
raycasts = []

def init(W, H, T, raycast_color=(0,255,0)):
    global height
    height = H
    global width
    width = W
    global window
    global raycolor
    raycolor = raycast_color
    window = pygame.display.set_mode((W, H))
    pygame.display.set_caption(T)
    clock = pygame.time.Clock()

def update():
    global width
    global height
    global physics_world
    global window
    global raycasts
    global raycolor

    i = 0
    crashed = False

    window.fill((255, 255, 255))

    for PhysObj in physics_world:
        PhysObj.draw(pygame, window, width, height)

    centerVec = core2d.Vector2(width/2, height/2)
    for raycast in raycasts:
        cast = (raycast[0].inverse_Y()+centerVec)
        pygame.draw.line(window, raycolor, cast.to_tuple(), (cast+raycast[1].normalize().inverse_Y()*raycast[2]).to_tuple())

    pygame.display.update()