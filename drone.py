import math
import core2d.physics
import core2d.collision
from core2d import *
from trainerSettings import TrainerSettings


class Drone(core2d.physics.PhysicalBody):

    def __init__(self, swarmStartPos, fieldX, fieldY, Swarm):
        super().__init__(Circle(swarmStartPos +
                                Vector2(fieldX * TrainerSettings.DRONE_DIST,
                                        fieldY * TrainerSettings.DRONE_DIST),
                                TrainerSettings.DRONE_SIZE),
                         color=(255, 0, 0))
        self.fieldX = fieldX
        self.fieldY = fieldY
        self.Swarm = Swarm

    def getAliveNeighbourCount(self):
        o = -1
        for x in range(-1, 2):
            for y in range(-1, 2):
                if not self.Swarm[self.fieldX + x][self.fieldY + y] is None:
                    o += 1
        return o

    # The Output (tilt and speed of the Drone) calculate to real Velocity and set as parameters
    def set_drone_output_params(self, params):
        self.velocity = Vector2(params[0] * TrainerSettings.MAX_DRONE_SPEED,
                                params[1] * math.pi * 2,
                                rad=True)

    ####### Parameters that a given to the Neural Network  ###########
    def get_network_parameters(self, objective):
        params = self.get_inner_parameters(objective)
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (x != 0 or y != 0) and not self.Swarm[self.fieldX + x][self.fieldY + y] is None:
                    params = (*params,
                              *self.Swarm[self.fieldX + x][self.fieldY + y]
                              .get_export_parameters(self.pos))
        return params

    # Parameters that the Neighbours get
    def get_export_parameters(self, relative):
        return (self.pos - relative).as_rad_tuple()

    # Parameters that only the Drone itself has
    def get_inner_parameters(self, objective, world):
        dst_obj = (self.pos - objective).as_rad_tuple()
        return *dst_obj, self.getAliveNeighbourCount(), *self.get_all_dir_raycast(world)

    def get_all_dir_raycast(self, world):
        output = []
        for cast in TrainerSettings.RAYCASTS_DRONE:
            output.append(core2d.collision.raycast_world(self, world, cast))
        return output

