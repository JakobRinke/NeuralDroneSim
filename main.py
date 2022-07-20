import time
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
    circle = PhysicalBody(Circle(Vector2(0,0), 100))
    core2d.graphics.physics_world.append(circle)
    bar = PhysicalBody(Rect(Vector2(2, -200), Vector2(250, 10)))
    bar2 = PhysicalBody(Rect(Vector2(2, 200), Vector2(250, 10)))

    '''
    PhysicalBody.move(a,b) = function to move objects
    a = the object you want to move
    b = an "Vector2" object, which adds the x and y value in it to the position of the object
    '''
    sleepFine = 1
    rect = PhysicalBody(Rect(Vector2(100,100),Vector2(50,100)))
    core2d.graphics.physics_world.append(rect)
    core2d.graphics.update()
    print(col.colldide(rect, circle))
    time.sleep(sleepFine)

    PhysicalBody.move(rect,Vector2(50,30))
    core2d.graphics.update()
    print(col.colldide(rect, circle))
    time.sleep(sleepFine)

    PhysicalBody.move(circle,Vector2(-20,-20))
    core2d.graphics.update()
    print(col.colldide(rect, circle))
    time.sleep(sleepFine)

    core2d.graphics.physics_world.append((bar))
    time.sleep(sleepFine)
    core2d.graphics.update()
    core2d.graphics.physics_world.append((bar2))
    core2d.graphics.update()
    print(col.colldide(bar, circle))
    print(col.colldide(bar2, circle))
    time.sleep(sleepFine)

    PhysicalBody.move(bar,Vector2(0,100))
    core2d.graphics.update()
    print(col.colldide(bar, circle))
    time.sleep(sleepFine)

    PhysicalBody.move(bar2, Vector2(0,-100))
    core2d.graphics.update()
    print(col.colldide(bar2, circle))
    time.sleep(sleepFine)

    PhysicalBody.move(circle, Vector2(20,20))
    core2d.graphics.update()
    print(col.colldide(bar, circle))
    print(col.colldide(bar2, circle))
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

