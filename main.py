from physics2d import *
import physics2d.collision as col
import math


def main():
    rect = Rect(Vector2(2, 0), Vector2(2, 2))
    cast = col.raycast_rect(rect, Vector2(2, 2), Vector2(0, -1))
    print(cast)
    print(rect.in_bounds(Vector2(1, 2)))



if __name__ == '__main__':
    main()

