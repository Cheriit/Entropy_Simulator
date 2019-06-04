import random as r
import numpy as np
import math


class Atom:
    def __init__(self, master, x, y, speed_x, speed_y, name, config):
        self.config = config
        self.pos = [x, y]
        self.speed = [speed_x, speed_y]
        self.radius = float(self.config['radius'])
        self.name = name
        self.master = master
        self.color = '#%02x%02x%02x' % (
            r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)
        )
        self.point = master.create_oval(x - self.radius, y - self.radius,
                                        x + self.radius, y + self.radius,
                                        fill=self.color)

    def __str__(self):
        return f"Atom \"{self.name}\"\n" \
            f"Pozycja: {self.pos}\n" \
            f"Prędkość: {self.speed}\n"

    def move(self):
        # print(self.name)
        tick = (1 / self.master.tick_rate)
        self.pos = [
            self.pos[0] + self.speed[0] * tick,
            self.pos[1] + self.speed[1] * tick
        ]
        self.master.move(self.point,
                         self.speed[0] * tick,
                         self.speed[1] * tick)

    def is_wall(self):

        max_x = self.master.width_container-self.radius
        max_y = self.master.height_container-self.radius
        pos = self.pos
        speed = self.speed
        radius = self.radius

        # if self.pos[0] < self.radius or self.pos[0] > max_x:
        #     self.speed = (-self.speed[0], self.speed[1])
        #
        # if self.pos[1] < 0 or self.pos[1] > max_y:
        #     self.speed = (self.speed[0], -self.speed[1])

        if pos[0] < radius:
            self.speed = (-speed[0], speed[1])
            self.pos = (radius, pos[1])
        elif pos[0] > max_x:
            self.speed = (-speed[0], speed[1])
            self.pos = (max_x, pos[1])
        elif pos[1] < 0:
            self.speed = (speed[0], -speed[1])
            self.pos = (pos[0], 0)
        elif pos[1] > max_y:
            self.speed = (speed[0], -speed[1])
            self.pos = (pos[0], max_y)

    def distance(self, point):
        return math.sqrt((self.pos[0] - point.pos[0]) ** 2 + (self.pos[1] - point.pos[1]) ** 2)

    def is_collision(self, point):
        """
        Ta funkcja działą mniejwięcej ale bardziej mniej niż więcej, dobra na teraz, wera pisze nową
        :param point:
        :return:
        """
        pos_source = self.pos
        pos_target = point.pos
        radius = self.radius *2

        if abs(self.pos[0]) <= abs(point.pos[0] + radius ) or \
                abs(self.pos[0]) <= abs(point.pos[0] - radius):
            temp = self.speed[1]
            self.speed = (self.speed[0], point.speed[1])
            point.speed = (point.speed[0], temp)

        else:
            temp = self.speed[0]
            self.speed = (point.speed[0], self.speed[1])
            point.speed = (temp, point.speed[1])

        """else:
            point_1_vx = 0.5 * (self.speed[1] - point.speed[1]) * ((point.pos[0] - self.pos[0]) / (self.pos[1] - point.pos[1])) + 0.5 * (self.speed[0] + point.speed[0])
            point_1_vy = 0.75 * ((self.pos[1] - point.pos[1]) / (point.pos[0] - self.pos[0])) * (self.speed[0] - point.speed[0]) + 0.5 * self.speed[1]
            point_2_vx = 0.5 * ((point.pos[0] - self.pos[0]) / (self.pos[1] - point.pos[1])) * (point.speed[1] - self.speed[1]) + 0.5 * point.speed[0]
            point_2_vy = 0.5 * ((self.pos[1] - point.pos[1])/(point.pos[0] - self.pos[0])) * (point.speed[0] - self.speed[0]) - self.pos[1] + 0.5 * (self.speed[1] + point.speed[1])
            self.speed = (point_1_vx, point_1_vy)
            point.speed = (point_2_vx, point_2_vy)"""