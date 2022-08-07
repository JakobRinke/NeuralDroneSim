from trainerSettings import TrainerSettings
import core2d
import random
import core2d.physics
import core2d.physics_object


def create_base_world():
    world = []
    ws_div_3 = int(TrainerSettings.WORLD_SIZE / 3)
    swarmpos = core2d.Vector2(random.randrange(-ws_div_3, ws_div_3),
                              random.randrange(-ws_div_3, ws_div_3))
    objectivePos = core2d.Vector2( -TrainerSettings.WORLD_SIZE / 2 - 100,  -TrainerSettings.WORLD_SIZE / 2 - 100)
    while not ( -TrainerSettings.WORLD_SIZE / 2 < objectivePos.x < TrainerSettings.WORLD_SIZE / 2 and
                -TrainerSettings.WORLD_SIZE / 2 < objectivePos.y < TrainerSettings.WORLD_SIZE / 2) or \
            (objectivePos - swarmpos).length() < TrainerSettings.WORLD_SIZE/2:
        objectivePos.x = random.randrange(-TrainerSettings.WORLD_SIZE / 2, TrainerSettings.WORLD_SIZE / 2)
        objectivePos.y = random.randrange(-TrainerSettings.WORLD_SIZE / 2, TrainerSettings.WORLD_SIZE / 2)

    for i in range(2):
        pos = core2d.Vector2(-TrainerSettings.WORLD_SIZE / 2 - 100, -TrainerSettings.WORLD_SIZE / 2 - 100)
        while not (-TrainerSettings.WORLD_SIZE / 2 < pos.x < TrainerSettings.WORLD_SIZE / 2 and
                   -TrainerSettings.WORLD_SIZE / 2 < pos.y < TrainerSettings.WORLD_SIZE / 2) or \
                (pos - swarmpos).length() < 150 and  (pos - objectivePos).length() < 50:
            pos.x = random.randrange(-TrainerSettings.WORLD_SIZE / 2, TrainerSettings.WORLD_SIZE / 2)
            pos.y = random.randrange(-TrainerSettings.WORLD_SIZE / 2, TrainerSettings.WORLD_SIZE / 2)
        rect = core2d.physics.PhysicalBody(core2d.Rect(pos, core2d.Vector2(40, 40)))
        world.append(rect)
    return world, swarmpos, objectivePos

def createStaticworld():
    world = []

    world.append(core2d.physics.PhysicalBody(core2d.Rect(core2d.Vector2(0, 50), core2d.Vector2(40, 40))))
    world.append(core2d.physics.PhysicalBody(core2d.Rect(core2d.Vector2(100, 0), core2d.Vector2(40, 40))))

    return world, core2d.Vector2(-200, -100), core2d.Vector2(200,200)

def defence_world():
    world = []
    points = [core2d.Vector2(200, -200), core2d.Vector2(-200, 200)]
    world.append(core2d.physics_object.path_moving_object(core2d.Rect(core2d.Vector2(-200, 200), core2d.Vector2(40, 40)),points,TrainerSettings.OBJ_SPEED))
    points = [core2d.Vector2(-200, -200), core2d.Vector2(200, 200)]
    world.append(core2d.physics_object.path_moving_object(core2d.Rect(core2d.Vector2(-200, -200), core2d.Vector2(40, 40)),points,TrainerSettings.OBJ_SPEED))
    points = [core2d.Vector2(200, -200), core2d.Vector2(-200, 200)]
    world.append(core2d.physics_object.path_moving_object(core2d.Rect(core2d.Vector2(200, -200), core2d.Vector2(40, 40)), points,TrainerSettings.OBJ_SPEED))
    points = [core2d.Vector2(-200, -200), core2d.Vector2(200, 200)]
    world.append(core2d.physics_object.path_moving_object(core2d.Rect(core2d.Vector2(200, 200), core2d.Vector2(40, 40)),points, TrainerSettings.OBJ_SPEED))
    return world, core2d.Vector2(0, 0), core2d.Vector2(0, 0)


def def_world_rand(x=0, y=250):
    return random.choice([-1, 1]) * random.randrange(x, y)


def random_defenceworld():
    world = []
    points = [core2d.Vector2(200, -200), core2d.Vector2(-200, 200)]
    world.append(
        core2d.physics_object.path_moving_object(core2d.Rect(core2d.Vector2(-200, 200), core2d.Vector2(40, 40)), points,
                                                 TrainerSettings.OBJ_SPEED))
    for i in range(3):
        points = [core2d.Vector2(def_world_rand(150, 250), def_world_rand(150, 250)),
                  core2d.Vector2(def_world_rand(), def_world_rand()),
                  core2d.Vector2(def_world_rand(), def_world_rand()),
                  core2d.Vector2(def_world_rand(), def_world_rand())]
        world.append(
            core2d.physics_object.path_moving_object(core2d.Rect(points[0], core2d.Vector2(40, 40)),
                                                     points, TrainerSettings.OBJ_SPEED))
    return world, core2d.Vector2(0, 0), core2d.Vector2(0, 0)