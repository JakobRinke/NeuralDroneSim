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
import gzip
import random
neat_agent.physics = core2d.physics
neat_agent.draw = core2d.graphics
GEN = 0

RESTORE = "./neat-checkpoint-34"




def proccess_net(*args):
    nets = args[0][0]
    drw = args[0][1]
    fitness_save = []
    agents = []
    world, swarmpos, objective = world_gen.create_base_world()
    draw = True #True
    currently_showing = 0
    if drw:
        core2d.graphics.init("Training AI")
        core2d.graphics.goal = objective

    for net in nets:
        agents.append(neat_agent.BaseNeatAgent(world, swarmpos, objective, net.activate, draw and drw))
        fitness_save.append(0)
        draw = False
    for i in range(int((TrainerSettings.exec_time/TrainerSettings.update_time/TrainerSettings.time_scale))):
        delta_time = TrainerSettings.update_time*TrainerSettings.time_scale
        strongest = 0
        strogest_fitness = 0
        core2d.physics.physicsProcessTime(world, delta_time, observe_collisions=False)
        for i, agent in enumerate(agents):
            agent.proccess_network(delta_time)
            fitness_save[i] = agent.getFitness(TrainerSettings.update_time)
            if drw and fitness_save[i] > strogest_fitness:
                strongest = i
                strogest_fitness = fitness_save[i]
        #agents[strongest].proccess_network(delta_time)

        if drw:
            agents[currently_showing].updateGraphics = False
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
    for i in range(TrainerSettings.THREAD_NUM - 1):
        ThreadArgs.append((nets, False))
    with Pool(len(ThreadArgs)) as pool:
        print(pool)
        Returns = pool.map(proccess_net, ThreadArgs)

    for Ret in Returns:
        for i in range(len(Ret)):
            ge[i].fitness += Ret[i] / TrainerSettings.THREAD_NUM

def run_neat(config_path):
    global config
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    try:
        if RESTORE == "":
            raise
        p = Checkpointer.restore_checkpoint(RESTORE)
    except Exception as e:
        print(e)
        p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = Checkpointer()
    p.add_reporter(stats)
    winner = p.run(main, 400)
    print(winner)
    win = p.best_genome
    pickle.dump(winner, open('levelup1.pkl', 'wb'))
    pickle.dump(win, open('real_levelup1.pkl', 'wb'))


class Checkpointer(neat.reporting.BaseReporter):
    def __init__(self, generation_interval=5, time_interval_seconds=15000,
                 filename_prefix='neat-checkpoint-'):

        self.generation_interval = generation_interval
        self.time_interval_seconds = time_interval_seconds
        self.filename_prefix = filename_prefix

        self.current_generation = None
        self.last_generation_checkpoint = -1
        self.last_time_checkpoint = time.time()

    def start_generation(self, generation):
        self.current_generation = generation

    def end_generation(self, config, population, species_set):
        checkpoint_due = False

        if self.time_interval_seconds is not None:
            dt = time.time() - self.last_time_checkpoint
            if dt >= self.time_interval_seconds:
                checkpoint_due = True

        if (checkpoint_due is False) and (self.generation_interval is not None):
            dg = self.current_generation - self.last_generation_checkpoint
            if dg >= self.generation_interval:
                checkpoint_due = True

        if checkpoint_due:
            self.save_checkpoint(config, population, species_set, self.current_generation)
            self.last_generation_checkpoint = self.current_generation
            self.last_time_checkpoint = time.time()


    def save_checkpoint(self, config, population, species_set, generation):
        filename = '{0}{1}'.format(self.filename_prefix, generation)
        print("Saving checkpoint to {0}".format(filename))

        with gzip.open(filename, 'w+', compresslevel=5) as f:
            data = (generation, config, population, species_set, random.getstate())
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)


    @staticmethod
    def restore_checkpoint(filename):
        """Resumes the simulation from a previous saved point."""
        with gzip.open(filename) as f:
            generation, config, population, species_set, rndstate = pickle.load(f)
            random.setstate(rndstate)
            return neat.population.Population(config, (population, species_set, generation))



if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run_neat(config_path)




