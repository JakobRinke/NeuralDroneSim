import time
from trainerSettings import TrainerSettings
import pygame
import pygame.draw
import sys
import core2d
physics_world = []
raycasts = []
goal = core2d.Vector2(0, 0)

def init(T, raycast_color=(0,255,0)):
    global height
    height = TrainerSettings.WORLD_SIZE
    global width
    width = TrainerSettings.WORLD_SIZE
    global window
    global raycolor
    raycolor = raycast_color
    window = pygame.display.set_mode((height, width))
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
        if PhysObj is not None:
            PhysObj.draw(pygame, window, width, height)

    centerVec = core2d.Vector2(width/2, height/2)
    for raycast in raycasts:
        cast = (raycast[0].inverse_Y()+centerVec)
        pygame.draw.line(window, raycolor, cast.to_tuple(), (cast+raycast[1].normalize().inverse_Y()*raycast[2]).to_tuple())

    npos = (TrainerSettings.WORLD_SIZE / 2 + goal.x, TrainerSettings.WORLD_SIZE / 2 - goal.y)
    pygame.draw.circle(window, (0, 0, 255), npos, 10)

    pygame.display.update()