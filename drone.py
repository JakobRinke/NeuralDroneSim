import math
import core2d.physics
import core2d.collision
from core2d import *
from trainerSettings import TrainerSettings


class Drone(core2d.physics.PhysicalBody):

    def __init__(self, swarmStartPos, fieldX, fieldY, agent):
        super().__init__(Circle(swarmStartPos +
                                Vector2((fieldX-TrainerSettings.DRONENUM/2) * TrainerSettings.DRONE_DIST,
                                        (fieldY-TrainerSettings.DRONENUM/2) * TrainerSettings.DRONE_DIST),
                                TrainerSettings.DRONE_SIZE),
                         color=(255, 0, 0))
        self.fieldX = fieldX
        self.fieldY = fieldY
        self.agent = agent

    def getAliveNeighbourCount(self):
        o = -1
        for x in range(-1, 2):
            for y in range(-1, 2):
                if not self.agent.swarm[self.fieldX + x][self.fieldY + y] is None:
                    o += 1
        return o

    # The Output (tilt and speed of the Drone) calculate to real Velocity and set as parameters
    def set_drone_output_params(self, params):
        """
        self.velocity = Vector2(params[0] * TrainerSettings.MAX_DRONE_SPEED,
                                params[1] * math.pi * 2,
                                rad=True)
        """
        self.velocity = Vector2(params[0], params[1]).normalize() * TrainerSettings.MAX_DRONE_SPEED


    ####### Parameters that a given to the Neural Network  ###########
    def get_network_parameters(self):
        params = self.get_inner_parameters()
        """
        
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x != 0 or y != 0:
                    if not self.agent.swarm[self.fieldX + x][self.fieldY + y] is None:
                        params = (*params,
                                  *self.agent.swarm[self.fieldX + x][self.fieldY + y]
                                  .get_export_parameters(self.pos))
                    else:
                        params = (*params, TrainerSettings.WORLD_SIZE, 0)
        """
        return params

    # Parameters that the Neighbours get
    def get_export_parameters(self, relative):
        return (self.pos - relative).as_rad_tuple()

    # Parameters that only the Drone itself has
    def get_inner_parameters(self):
        #dst_obj = (self.pos - self.agent.objective).as_rad_tuple()
        dst_obj = (self.pos - self.agent.objective).to_tuple()
        return *dst_obj, *self.get_all_dir_raycast() \
             #, self.getAliveNeighbourCount()

    def get_all_dir_raycast(self):
        output = []
        for cast in TrainerSettings.RAYCASTS_DRONE:
            output.append(core2d.collision.raycast_world(self, self.agent.world, cast))
        return output



    def remove_drone_from_swarm(self):
        for item in self.agent.world:
            if isinstance(item ,Drone) and item is not None:
                if item.fieldX == self.fieldX and item.fieldY == self.fieldY:
                    self.agent.world.remove(item)

        self.agent.swarm[self.fieldX][self.fieldY] = None

    def evt_collision(self, other):
        self.remove_drone_from_swarm()

    def evt_world_border(self):
        self.remove_drone_from_swarm()


