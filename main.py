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

    a = TrainerSettings.DRONE_SIZE
    drone = PhysicalBody(Circle(Vector2(0,0),a))
    wall = PhysicalBody(Rect(Vector2(200, -230),Vector2(2,500)))
    wall2 = PhysicalBody(Rect(Vector2(100,-170),Vector2(200,2)))
    core2d.graphics.physics_world.append(wall)
    core2d.graphics.physics_world.append(wall2)
    core2d.graphics.physics_world.append(drone)
    core2d.graphics.update()
    time.sleep(2)

    PhysicalBody.move(drone, Vector2(250,-250))
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

