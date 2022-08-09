import time
import drone
import core2d.collision
import core2d.physics
import random

TESTNUM = 1000000


Vec1 = core2d.Vector2(random.random()*40, random.random()*10)
Vec2 = core2d.Vector2(random.random(), random.random())
Vec3 = core2d.Vector2(random.random()*40, random.random()*40)
Vec4 = core2d.Vector2(random.random(), random.random())

ta = time.time()
for i in range(TESTNUM):
    core2d.collision.raycast_line(Vec1, Vec2, Vec3, Vec4)
ta = time.time() - ta
print(f"Test A Method 1: {ta}")

tb = time.time()
for i in range(TESTNUM):
    core2d.collision.raycast_line2(Vec1, Vec2, Vec3, Vec4)
tb = time.time() - tb
print(f"Test A Method 2: {tb}")
print(f"Speed Improvement: {100*ta/tb-100}% \n")


Vec1 = core2d.Vector2(random.random()*40, random.random()*10)
Vec2 = core2d.Vector2(random.random(), random.random())
Vec3 = core2d.Vector2(random.random()*40, random.random()*40)
Vec4 = core2d.Vector2(random.random(), random.random())

ta = time.time()
for i in range(TESTNUM):
    core2d.collision.raycast_line(Vec1, Vec2, Vec3, Vec4)
ta = time.time() - ta
print(f"Test B Method 1: {ta}")

tb = time.time()
for i in range(TESTNUM):
    core2d.collision.raycast_line2(Vec1, Vec2, Vec3, Vec4)
tb = time.time() - tb
print(f"Test B Method 2: {tb}")
print(f"Speed Improvement: {100*ta/tb-100}% \n")



