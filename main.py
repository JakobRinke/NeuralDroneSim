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
    core2d.graphics.init(TrainerSettings.WORLD_SIZE, TrainerSettings.WORLD_SIZE, "PhysTest")

    #rect = PhysicalBody(Rect(Vector2(100,100), Vector2(50, 50)))
    #core2d.graphics.physics_world.append(rect)

    drone1 = PhysicalBody(Circle(Vector2(-240,260), 10))
    drone2 = PhysicalBody(Circle(core2d.Vector2(-100,-100),10))
    drone1.target = core2d.Vector2(0,100)
    drone2.target = core2d.Vector2(-50,200)
    drone1.velocity = Vector2(30,-10)
    drone2.velocity = Vector2(20,20)
    core2d.graphics.physics_world.append(drone1)
    core2d.graphics.physics_world.append(drone2)

    time.sleep(2)
    core2d.graphics.update()

    time_scale = 5.0
    t = time.time()
    for i in range(10000):
        time.sleep(1/60)
        physicsProcessTime(core2d.graphics.physics_world,(time.time()-t)*time_scale)
        t = time.time()


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

