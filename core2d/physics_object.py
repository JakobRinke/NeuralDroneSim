import core2d.physics



class path_moving_object(core2d.physics.PhysicalBody):
    def __init__(self, Shape, points, speed, color=(0, 0, 0)):
        super().__init__(Shape, color)
        self.points = points
        self.speed = speed
        self.next_point = 0
        if len(points)<=0:
            self.next_point=-1
        else:
            self.velocity = (self.points[self.next_point % len(self.points)] - self.pos).normalize() * self.speed

    def processVelocity(self, time):
        super().processVelocity(time)
        if self.next_point == -1:
            return
        if (self.pos-self.points[self.next_point%len(self.points)]).length() < self.speed*1.5:
            self.next_point += 1
            self.velocity= (self.points[self.next_point%len(self.points)]-self.pos).normalize()*self.speed


class target_moving_object(core2d.physics.PhysicalBody):

    def __init__(self, Shape, target, speed, color=(0, 0, 0)):
        super().__init__(Shape, color)
        self.target = target
        self.speed = speed
        self.velocity = (target.pos - self.pos).normalize() * self.speed

    def processVelocity(self, time):
        super().processVelocity(time)
        self.velocity = (self.target.pos - self.pos).normalize() * self.speed