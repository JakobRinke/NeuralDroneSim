import math
import core2d
import array
import copy
from trainerSettings import TrainerSettings

from trainerSettings import TrainerSettings

def colldide(o1, o2):
    if o1.type == "rect" and o2.type == "rect":
        return rects_collide(o1, o2)
    elif o1.type == "circle" and o2.type == "circle":
        return spheres_collide(o1, o2)
    elif o1.type == "rect" and o2.type == "circle":
        return sphere_collide_rect(o2, o1)
    elif o2.type == "rect" and o1.type == "circle":
        return sphere_collide_rect(o1, o2)

def out_worldborder(object):
    if object.type == "rect":
        return rect_out_worldborder(object)
    elif object.type == "circle":
        return circle_out_worldborder(object)

def rects_collide(r1, r2):
    l1 = r1.pos - r1.param2/2
    l2 = r2.pos - r2.param2/2
    return (l1.x <= l2.x + r2.param2.x and
            l1.x + r1.param2.x >= l2.x and
            l1.y <= l2.y + r2.param2.y and
            r1.param2.y + l1.y >= l2.y)

def spheres_collide(s1, s2):
    return (s1.pos-s2.pos).length() <= s1.param2 + s2.param2

def sphere_collide_rect(circle, rect):
    circleDistance = abs(circle.pos - rect.pos)
    halfSize = rect.param2/2
    if (circleDistance.x > (halfSize.x + circle.param2)):
        return False
    if circleDistance.y > (halfSize.y + circle.param2):
        return False
    if circleDistance.x <= (halfSize.x):
        return True
    if circleDistance.y <= (halfSize.y):
        return True
    cornerDistance_sq = (circleDistance.x - halfSize.x)**2 + \
                        (circleDistance.y - halfSize.y)**2
    return (cornerDistance_sq <= (circle.param2**2))


def rect_out_worldborder(rect):
    return  rect.pos.x-rect.param2.x/2 < -TrainerSettings.WORLD_SIZE/2 or \
            rect.pos.y-rect.param2.y/2 < -TrainerSettings.WORLD_SIZE/2 or \
            rect.pos.x+rect.param2.x/2 > TrainerSettings.WORLD_SIZE/2 or \
            rect.pos.y+rect.param2.y/2 > TrainerSettings.WORLD_SIZE/2


def circle_out_worldborder(circle):
    return circle.pos.x - circle.param2 / 2 < -TrainerSettings.WORLD_SIZE / 2 or \
           circle.pos.y - circle.param2 / 2 < -TrainerSettings.WORLD_SIZE / 2 or \
           circle.pos.x + circle.param2 / 2 > TrainerSettings.WORLD_SIZE / 2 or \
           circle.pos.y + circle.param2 / 2 > TrainerSettings.WORLD_SIZE / 2


def raycast_sphere(cyc, start, dir, in_bounds_break=True):
    if in_bounds_break and cyc.in_bounds(start) :
        return 0
    dir = dir.normalize()
    dx = start.x - cyc.pos.x
    dy = cyc.pos.y - start.y
    a = - dir.x*dir.x - dir.y*dir.y
    b = 2 * (-dir.x*dx+dir.y*dy)
    c = -dx*dx-dy*dy + cyc.param2*cyc.param2
    try:
        l = min((-b+math.sqrt(b*b-4*a*c))/(2*a), \
                   (-b-math.sqrt(b*b-4*a*c))/(2*a) )
        if l < 0:
            return math.inf
        else:
            return l
    except:
        return math.inf


def raycast_line(LineStart, LineDir, start, dir):
    dir = dir.normalize()
    x1 = LineStart.x
    y1 = LineStart.y
    x2 = start.x
    y2 = start.y
    x3 = x1 + LineDir.x
    y3 = y1 + LineDir.y
    x4 = x2 + dir.x
    y4 = y2 + dir.y
    uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
    if uA >= 0 and uA <= 1:
        return ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
    else:
        return math.inf


def raycast_rect(rect, start, dir, in_bounds_break=True):
    if in_bounds_break and rect.in_bounds(start):
        return 0
    bottomleft = rect.pos - rect.param2 / 2
    topright = rect.pos + rect.param2 / 2
    l = min(raycast_line(bottomleft,
                         core2d.Vector2(rect.param2.x, 0),
                         start, dir), math.inf)
    l = min(raycast_line(bottomleft,
                         core2d.Vector2(0, rect.param2.y),
                         start, dir), l)
    l = min(raycast_line(topright,
                         -core2d.Vector2(rect.param2.x, 0),
                         start, dir), l)

    l = min(raycast_line(topright,
                         -core2d.Vector2(0, rect.param2.y),
                         start, dir), l)
    return l

World_Rect = core2d.Rect(core2d.Vector2(0,0),
                         core2d.Vector2(TrainerSettings.WORLD_SIZE,TrainerSettings.WORLD_SIZE))
def raycast_worldborder(start, dir):
    return raycast_rect(World_Rect, start, dir, False)


def raycast_world(me, world, dir):
    l = raycast_worldborder(me.pos, dir)
    for b in world:
        if me.pos.x != b.pos.x and me.pos.y != b.pos.y:
            if b.type == "circle":
                l = min(l, raycast_sphere(b, me.pos, dir))
            if b.type == "rect":
                l = min(l, raycast_rect(b, me.pos, dir))
    return l


def generateCoordinatesOnWay(start, vel):
    raycast = []
    for a in raycast:
        a = -501
    y = 0
    current = copy.deepcopy(start)
    while(y < TrainerSettings.MAX_RAYCAST_LEN):
        current.x = current.x + vel.x
        current.y = current.y + vel.y
        raycast.append(current)
        y = y + abs((vel.x+vel.y))
    return raycast

def sort(dir):
    newDir = []
    for y in range(len(dir)):
        actual = core2d.Vector2(101,101)
        for i in dir:
            if ((i.x + i.y)/2 < (actual.x + actual.y)/2):
                actual = i
        newDir.append(actual)
        dir.remove(i)
    return newDir


