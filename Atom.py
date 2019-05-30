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

    def access_atom(self):
        return self.pos[0], self.pos[1], \
               self.speed[0], self.speed[1]

    def distance(self, atom):
        return 100
        pass

    def apply_collision(self, atom):
        pass

    def move(self):
        # print(self.name)
        self.pos = [
            self.pos[0] + self.speed[0] * (1 / self.master.tick_rate),
            self.pos[1] + self.speed[1] * (1 / self.master.tick_rate)
        ]
        self.master.move(self.point,
                         self.speed[0] * (1 / self.master.tick_rate),
                         self.speed[1] * (1 / self.master.tick_rate))

    def is_wall(self):

        max_x = self.master.width_container-self.radius
        max_y = self.master.height_container-self.radius

        if self.pos[0] < self.radius or self.pos[0] > max_x:
            self.speed[0] *= -1

        if self.pos[1] < 0 or self.pos[1] > max_y:
            self.speed[1] *= -1

        # if self.pos[0] < self.radius:
        #     self.speed[0] *= -1
        #     # self.pos[0] = self.radius
        #
        # elif self.pos[0] > max_x:
        #     self.speed[0] *= -1
        #     # self.pos[0] = max_x
        #
        #
        # if self.pos[1] < 0:
        #     self.speed[1] *= -1
        #     # self.pos[1] = 0
        #
        # elif self.pos[1] > max_y:
        #     self.speed[1] *= -1
        #     # self.pos[1] = max_y

    def distance(self, point):
        return math.sqrt((self.pos[0] - point.pos[0]) ** 2 + (self.pos[1] - point.pos[1]) ** 2)

    def is_collision(self, point):

        if self.pos[1] == point.pos[1]:
            tmp = point.pos[0]
            self.pos[0], point.pos[0] = point.pos[0], self.pos[0]

        elif self.pos[0] == point.pos[0]:
            self.pos[1], point.pos[1] = point.pos[1], self.pos[1]

        else:
            punkt_Hx = 0.5 * ((point.pos[0] - self.pos[0]) / (self.pos[1] - point.pos[1])) * (
                    self.pos[1] - point.pos[1] - point.speed[1] + (point.pos[0] + point.speed[0]) * (
                    (self.pos[1] - point.pos[1]) / (point.pos[0] - self.pos[0])) - self.pos[0] * (
                            (point.pos[1] - self.pos[1]) / (point.pos[0] - self.pos[0])))

            punkt_Hy = 0.5 * (self.pos[1] - point.pos[1] - point.speed[1] + (point.pos[0] + point.speed[0]) * (
                    (self.pos[1] - point.pos[1]) / (point.pos[0] - self.pos[0])) - self.pos[0] * (
                                      (point.pos[1] - self.pos[1]) / (
                                      point.pos[0] - self.pos[0]))) + point.pos[1] + point.speed[1] - (
                               point.pos[0] + point.speed[0]) * (
                               (self.pos[1] - point.pos[1]) / (point.pos[0] - self.pos[0]))
            punkt_1_Vx = math.sqrt((0.5 * ((point.pos[0] - self.pos[0]) / (self.pos[1] - point.pos[1])) * (
                    point.pos[1] + point.speed[1] - (self.pos[0] + self.speed[0]) * (
                    (point.pos[1] - self.pos[1]) / (point.pos[0] - self.pos[0])) + (
                            self.pos[0] - point.pos[0] + punkt_Hx) * (
                            (point.pos[1] - self.pos[1]) / (point.pos[0] - self.pos[0])) - punkt_Hy) - self.pos[0]) ** 2)

            punkt_1_Vy = math.sqrt((0.5 * (point.pos[1] + point.speed[1] - (self.pos[0] + self.speed[0]) * (
                    (point.pos[1] - self.pos[1]) / (point.pos[0] - self.pos[0])) + (
                                                   self.pos[0] - point.pos[0] + punkt_Hx) * (
                                                   (point.pos[1] - self.pos[1]) / (
                                                   point.pos[0] - self.pos[0])) - punkt_Hy) + punkt_Hy - point.pos[1] +
                                    self.pos[1] - (
                                            punkt_Hx - point.pos[0] + self.pos[0]) * (
                                            (self.pos[1] - point.pos[1]) / (point.pos[0] - self.pos[0]))) ** 2)

            punkt_Fx = 0.5 * ((point.pos[0] - self.pos[1]) / (point.pos[1] - self.pos[1])) * (
                    self.speed[1] - (self.pos[0] + self.speed[0]) * (
                    (self.pos[1] - point.pos[1]) / (point.pos[0] - self.pos[0])) + self.pos[0] * (
                            (point.pos[1] - self.pos[1]) / (point.pos[0] - self.pos[0])))

            punkt_Fy = 0.5 * (self.speed[1] - (self.pos[0] + self.speed[0]) * (
                    (self.pos[1] - point.pos[1]) / (point.pos[0] - self.pos[0])) + self.pos[0] * (
                                      (point.pos[1] - self.pos[1]) / (
                                      point.pos[0] - self.pos[0]))) + self.pos[1] - self.pos[0] * (
                               (point.pos[1] - self.pos[1]) / (point.pos[0] - self.pos[0]))

            punkt_2_Vx = math.sqrt((0.5 * ((point.pos[0] - self.pos[0]) / (self.pos[1] - point.pos[1])) * (
                    point.speed[1] + self.pos[1] - punkt_Fy + (punkt_Fx - self.pos[0] + point.pos[0]) * (
                    (self.pos[1] - point.pos[1]) / (point.pos[0] - self.pos[0])) - (point.pos[0] + point.speed[0]) * (
                            (point.pos[1] - self.pos[1]) / (point.pos[0] - self.pos[0]))) - point.pos[0]) ** 2)

            punkt_2_Vy = math.sqrt(
                (0.5 * (point.speed[1] + self.pos[1] - punkt_Fy + (punkt_Fx - self.pos[0] + point.pos[0]) * (
                        (self.pos[1] - point.pos[1]) / (point.pos[0] - self.pos[0])) - (
                                point.pos[0] + point.speed[0]) * (
                                (point.pos[1] - self.pos[1]) / (
                                point.pos[0] - self.pos[0]))) + punkt_Fy - self.pos[1] + point.pos[1] - (
                         punkt_Fx - self.pos[0] + point.pos[0]) * (
                         (self.pos[1] - point.pos[1]) / (point.pos[0] - self.pos[0])) - point.pos[1]) ** 2)

            self.speed = (punkt_1_Vx, punkt_1_Vy)
            point.speed = (punkt_2_Vx, punkt_2_Vy)
