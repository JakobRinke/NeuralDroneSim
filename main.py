import core2d.graphics
from core2d import *
import core2d.collision as col
from core2d.physics import *
import math


def main():
    core2d.graphics.init(500, 500, "PhysTest")
    rect = PhysicalBody(Rect(Vector2(0,0), Vector2(50, 50)))
    rect2 = PhysicalBody(Rect(Vector2(-250, -250), Vector2(50, 50)), (255, 0, 0))
    rect3 = PhysicalBody(Rect(Vector2(250, 250), Vector2(50, 50)), (0, 0, 255))
    core2d.graphics.physics_world.append(rect)
    core2d.graphics.physics_world.append(rect2)
    core2d.graphics.physics_world.append(rect3)
    core2d.graphics.update()



if __name__ == '__main__':
    main()

