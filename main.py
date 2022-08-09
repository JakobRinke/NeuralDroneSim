import neat
import os
import neat_agent
from trainerSettings import TrainerSettings
import world_gen
import core2d
import core2d.physics
import time
import pickle
from multiprocessing import Pool
import core2d.graphics
import core2d.physics_object
neat_agent.physics = core2d.physics
neat_agent.draw = core2d.graphics
GEN = 0






def proccess_net(*args):
    nets = args[0][0]
    drw = args[0][1]
    fitness_save = []
    agents = []
    world, swarmpos, objective = world_gen.random_defenceworld()
    draw = True
    currently_showing = 0
    if drw:
        core2d.graphics.init("Training AI")
        core2d.graphics.goal = objective
    for net in nets:
        agents.append(neat_agent.DefenceNeatAgent(world, swarmpos, objective, net.activate, draw and drw))
        fitness_save.append(0)
        draw = False
    for i in range(int((TrainerSettings.exec_time/TrainerSettings.update_time))):
        delta_time = TrainerSettings.update_time*TrainerSettings.time_scale
        strongest = 0
        strogest_fitness = 0
        core2d.physics.physicsProcessTime(world, delta_time, observe_collisions=False)
        for i, agent in enumerate(agents):
            agent.proccess_network(delta_time)
            fitness_save[i] = agent.getFitness(delta_time)
            if drw and fitness_save[i] > strogest_fitness:
                strongest = i
                strogest_fitness = fitness_save[i]
        if drw and agents[currently_showing].updateGraphics == False:
            agents[strongest].updateGraphics = True
            currently_showing = strongest

    return fitness_save

def main(genomes, config):
    global GEN
    GEN += 1
    nets = []
    ge = []
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0
        ge.append(g)

    ThreadArgs = [(nets, True)]
    for i in range(TrainerSettings.THREAD_NUM-1):
        ThreadArgs.append((nets, False))

    with Pool(len(ThreadArgs)) as pool:
        Returns = pool.map(proccess_net, ThreadArgs)

    for Ret in Returns:
        for i in range(len(Ret)):
            ge[i].fitness+=Ret[i]/TrainerSettings.THREAD_NUM

def run_neat(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    winner = p.run(main, 400)
    print(winner)
    win = p.best_genome
    pickle.dump(winner, open('winner9.pkl', 'wb'))
    pickle.dump(win, open('real_winner9.pkl', 'wb'))



if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run_neat(config_path)

