import neat
import os
import neat_agent
from trainerSettings import TrainerSettings
import random
import core2d
import core2d.physics
import time
import core2d.graphics
import core2d.physics_object
neat_agent.physics = core2d.physics
neat_agent.draw = core2d.graphics


GEN = 0
def main(genomes, config):
    global GEN
    global fast_forward
    GEN += 1
    nets = []
    ge = []
    agents = []
    core2d.graphics.init("Training AI")
   # world, swarmpos, objective = create_base_world()
    world, swarmpos, objective = random_defenceworld()
    core2d.graphics.goal = objective
    draw = True
    currently_showing = 0
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        agents.append(neat_agent.DefenceNeatAgent(world, swarmpos, objective, net.activate, draw))
        g.fitness = 0
        ge.append(g)
        draw = False

    endtime = time.time() + TrainerSettings.exec_time
    last = time.time()
    while time.time() <= endtime:
        time.sleep(TrainerSettings.update_time)
        delta_time = time.time() - last
        last = time.time()
        strongest = 0
        strogest_fitness = 0
        for i, agent in enumerate(agents):
            agent.proccess_network(delta_time*TrainerSettings.time_scale)
            ge[i].fitness = agent.getFitness(delta_time*TrainerSettings.time_scale)
            if ge[i].fitness > strogest_fitness:
                strongest = i
                strogest_fitness = ge[i].fitness
        agents[currently_showing].updateGraphics = False
        agents[strongest].updateGraphics = True
        currently_showing = strongest







def run_neat(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    winner = p.run(main, 100000000)
    print(winner)


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
    for i in range(6):
        points = [core2d.Vector2(def_world_rand(150, 250), def_world_rand()), core2d.Vector2(def_world_rand(150, 250), def_world_rand())]
        world.append(
            core2d.physics_object.path_moving_object(core2d.Rect(points[0], core2d.Vector2(40, 40)),
                                                     points, TrainerSettings.OBJ_SPEED))
    return world, core2d.Vector2(0, 0), core2d.Vector2(0, 0)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run_neat(config_path)

