import copy
import math
from drone import Drone
import core2d
physics = ()
draw = ()
from trainerSettings import TrainerSettings

class BaseNeatAgent:

    def __init__(self, world_base, startPos, objective, activate, updateGraphics=False):
        self.world = []
        for i in world_base:
            self.world.append(i)

        self.swarm = []
        for i in range(TrainerSettings.DRONENUM):
            for j in range(TrainerSettings.DRONENUM):
                self.swarm.append(Drone(startPos, i, j, self, i*TrainerSettings.DRONENUM+j))
                self.world.append(self.swarm[i*TrainerSettings.DRONENUM+j])
        self.activate = activate
        self.objective = objective
        self.updateGraphics = updateGraphics
        self.stored_fitness = []
        for i in range(TrainerSettings.DRONENUM**2):
            self.stored_fitness.append(0)


    def proccess_network(self, deltaTime):
        for drone in self.swarm:
            params = drone.get_network_parameters()
            outp = self.activate(params)
            drone.set_drone_output_params(outp)
        physics.physicsProcessTime(self.world, deltaTime, False, True)
        if self.updateGraphics:
            draw.physics_world = self.world
           # self.updateRaycasts()
            draw.update()


    def updateRaycasts(self):
        draw.raycasts = []
        for drone in self.swarm:
            for i, cast in enumerate(drone.get_all_dir_raycast()):
                draw.raycasts.append((drone.pos, TrainerSettings.RAYCASTS_DRONE[i].normalize(), cast))


    def getFitness(self, dTime):
        fitness = 0
        for drone in self.swarm:
            f = (TrainerSettings.WORLD_DIAG-(self.objective - drone.pos).length() / TrainerSettings.WORLD_DIAG)**2/10000
            fitness += f
            self.stored_fitness[drone.id] = max(self.stored_fitness[drone.id], f)
        fitness += sum(self.stored_fitness) * 2 + fitness
        return fitness



class DefenceNeatAgent(BaseNeatAgent):
    def getFitness(self, deltaTime):
        for _ in self.swarm:
            self.stored_fitness += deltaTime
        return self.stored_fitness