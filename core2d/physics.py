import sys

import core2d
from trainerSettings import TrainerSettings
from core2d import graphics
import time
from core2d import collision

class PhysicalBody(core2d.Shape2):

    def __init__(self, Shape, color=(0, 0, 0), evt_oncol=lambda:None):
        super().__init__(Shape.pos, Shape.param2, Shape.type)
        self.velocity = core2d.Vector2(0, 0)
        self.color = color
        self.evt_oncollision=evt_oncol

    def moveAsTest(self, direction):
        breakDown = False
        sleepFine = 1/TrainerSettings.OBJECT_VEL
        i = 0
        while(breakDown == False):

            #obverves collisions
            for Object in graphics.physics_world:
                if(collision.colldide(Object,self) == True):
                    if(self != Object):
                        print("Game Over: Objects collided in coordinate (" + str(self.pos.x)+"|"+str(self.pos.y)+")")
                        time.sleep(5)
                        sys.exit()

            breakDown = True
            if(direction.x < self.pos.x):
                self.pos.x = self.pos.x - 1
                breakDown = False
            elif(direction.x > self.pos.x):
                self.pos.x = self.pos.x + 1
                breakDown = False
            if(direction.y < self.pos.y):
                self.pos.y = self.pos.y - 1
                breakDown = False
            elif(direction.y > self.pos.y):
                self.pos.y = self.pos.y + 1
                breakDown = False
            else:
                breakDown = True
            core2d.graphics.update()
            i = i+1
            if(i%10 == 0):
                print("------------------")
                print("| position x :" + str(self.pos.x)+ "|")
                print("| position y : " + str(self.pos.y)+"|")
                print("------------------")
            time.sleep(sleepFine)



    def proccessVelocity(self, t):
        self.pos += t*self.velocity

    def move(objects):
        breakUpCounter = 0
        for i in objects:
            if(i.pos.x < i.target.x):
                i.pos.x = i.pos.x + i.velocity.x
                if(i.pos.y < i.target.y):
                    i.pos.y = i.pos.y + i.velocity.y
                if (i.pos.y > i.target.y):
                    i.pos.y = i.pos.y - i.velocity.y
            elif(i.pos.x > i.target.x):
                i.pos.x = i.pos.x - i.velocity.x
                if (i.pos.y < i.target.y):
                    i.pos.y = i.pos.y + i.velocity.y
                if(i.pos.y > i.target.y):
                    i.pos.y = i.pos.y - i.velocity.y
            else:
                breakUpCounter = breakUpCounter +1

        if(breakUpCounter == len(objects)):
            return True
        core2d.graphics.update()

    def draw(self, pygame, window, width, height):
        npos = (width / 2 + self.pos.x, height / 2 - self.pos.y)
        if self.type == "circle":
            pygame.draw.circle(window, self.color, npos, self.param2)
        elif self.type == "rect":
            pygame.draw.rect(window, self.color, (npos[0]-self.param2.x/2, npos[1]-self.param2.y/2,
                                             self.param2.x, self.param2.y))

    def evt_oncollision(self):
        pass

def physicsProcess(objects, target):

    while(True):
        for b in objects:
            if(b.pos.x == b.target.x and b.pos.y == b.target.y):
                b.target = core2d.Vector2(0,240)
        if(PhysicalBody.move(objects) == True):
            break
        for a in objects:
            observeCollisions(a, objects)

def observeCollisions(self, objects):
    # obverves collisions
    for i in objects:
        if(collision.colldide(self, i )== True):
            if(self != i):
                print("Game Over: Objects collided in coordinate (" + str(self.pos.x) + "|" + str(self.pos.y) + ")")
                time.sleep(5)
                sys.exit()

