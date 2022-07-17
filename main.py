import physics2d as graph
import physics2d.collision as col
import math


def main():
    rect1 = graph.Rect(graph.Vector2(2,5), graph.Vector2(4,4))
    rect2 = graph.Rect(graph.Vector2(0,0), graph.Vector2(4,4))
    print(col.colldide(rect1, rect2))


if __name__ == '__main__':
    main()

