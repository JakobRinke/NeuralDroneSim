import time
from trainerSettings import TrainerSettings
import core2d.graphics
from core2d import *
import core2d.collision as col
from core2d.physics import *
import math
import pygame
import sys

def main():
    core2d.graphics.init(500, 500, "PhysTest")

    #rect = PhysicalBody(Rect(Vector2(100,100), Vector2(50, 50)))
    #core2d.graphics.physics_world.append(rect)

    drone1 = PhysicalBody(Circle(Vector2(-240,240), 10, Vector2(-240,240)))
    drone2 = PhysicalBody(Circle(core2d.Vector2(-100,-100),10,core2d.Vector2(240,-240)))
    drone1.velocity = Vector2(1,1)
    drone1.target
    drone2.velocity = Vector2(2,2)
    core2d.graphics.physics_world.append(drone1)
    core2d.graphics.physics_world.append(drone2)

    time.sleep(2)
    core2d.graphics.update()

    physicsProcess(core2d.graphics.physics_world, core2d.Vector2(240,-230))
    time.sleep(5)
    '''
    PhysicalBody.move(a,b) = function to move objects
    a = the object you want to move
    b = an "Vector2" object, which adds the x and y value in it to the position of the object
    '''
    print("-----Finished-----")
    sys.exit(0)

'''
    v_start = Vector2(0, 200)
    for i in range(-5, 5):
        v_dir = Vector2(i/7, -1)
        ln = col.raycast_sphere(circle, v_start, v_dir)
        core2d.graphics.raycasts.append((v_start, v_dir, ln))

    v_start = Vector2(0, -200)
    for i in range(-5, 5):
        v_dir = Vector2(i / 7, 1)
        ln = col.raycast_sphere(circle, v_start, v_dir)
        core2d.graphics.raycasts.append((v_start, v_dir, ln))

    v_start = Vector2(200, 0)
    for i in range(-5, 5):
        v_dir = Vector2(-1, i / 7)
        ln = col.raycast_sphere(circle, v_start, v_dir)
        core2d.graphics.raycasts.append((v_start, v_dir, ln))

    v_start = Vector2(-200, 0)
    for i in range(-5, 5):
        v_dir = Vector2(1, i / 7)
        ln = col.raycast_sphere(circle, v_start, v_dir)
        core2d.graphics.raycasts.append((v_start, v_dir, ln))

    
'''
if __name__ == '__main__':
    main()

