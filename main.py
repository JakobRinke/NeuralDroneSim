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

    drone1 = PhysicalBody(Circle(Vector2(-20,0), 10))
    drone2 = PhysicalBody(Circle(core2d.Vector2(-119,0),10))
    drone1.velocity = Vector2(10,0)
    drone2.velocity = Vector2(10,0)
    core2d.graphics.physics_world.append(drone1)
    core2d.graphics.physics_world.append(drone2)

    time.sleep(2)
    core2d.graphics.update()
    time_scale = TrainerSettings.time_scale
    t = time.time()

    for i in range(200):
        time.sleep(TrainerSettings.time_Waiting)
        physicsProcessTime(core2d.graphics.physics_world,TrainerSettings.time_Waiting*time_scale)
        t = time.time()
    time.sleep(5)

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

