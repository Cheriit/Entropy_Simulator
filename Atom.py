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
        self.max_speed = float(self.config['max_speed'])
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

    def limit_speed(self):
        max_speed = self.max_speed
        min_speed = max_speed*-1
        speed = self.speed

        if speed[0] > max_speed:
            self.speed = (max_speed, speed[1])
        elif speed[0] < min_speed:
            self.speed = (min_speed, speed[1])
        if speed[1] > max_speed:
            self.speed = (speed[0], max_speed)
        elif speed[1] < min_speed:
            self.speed = (speed[0],min_speed)

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

    def is_collision_tryg(self, point):

        alpha_1 = math.atan2(self.speed[1], self.speed[0])
        alpha_2 = math.atan2(point.speed[1], point.speed[0])
        phi = math.atan2(self.pos[1] - point.pos[1], self.pos[0] - point.pos[0])
        point_1_v = math.sqrt(self.speed[0] ** 2 + self.speed[1] ** 2)
        point_2_v = math.sqrt(point.speed[0] ** 2 + point.speed[1] ** 2)
        point_1_vx = point_2_v * math.cos(alpha_2 - phi) * math.cos(phi) + point_1_v * math.sin(
            alpha_1 - phi) * math.cos(phi + math.pi / 2)
        point_1_vy = point_2_v * math.cos(alpha_2 - phi) * math.sin(phi) + point_1_v * math.sin(
            alpha_1 - phi) * math.sin(phi + math.pi / 2)
        point_2_vx = point_1_v * math.cos(alpha_1 - phi) * math.cos(phi) + point_2_v * math.sin(
            alpha_2 - phi) * math.cos(phi + math.pi / 2)
        point_2_vy = point_1_v * math.cos(alpha_1 - phi) * math.sin(phi) + point_2_v * math.sin(
            alpha_2 - phi) * math.sin(phi + math.pi / 2)
        self.speed = (point_1_vx, point_1_vy)
        point.speed = (point_2_vx, point_2_vy)

        self.limit_speed()
        point.limit_speed()

    def is_collision_vect(self, point):
        vec_n = [point.pos[0] - self.pos[0], point.pos[1] - self.pos[1]]
        len_n = math.sqrt(vec_n[0]**2 + vec_n[1]**2)
        unit_n = [vec_n[0]/len_n, vec_n[1]/len_n]
        unit_t = [-unit_n[1], unit_n[0]]
        v_1n = unit_n[0]*self.speed[0] + unit_n[1]*self.speed[1]
        v_1t = unit_t[0]*self.speed[0] + unit_t[1]*self.speed[1]
        v_2n = unit_n[0]*point.speed[0] + unit_n[1]*point.speed[1]
        v_2t = unit_t[0]*point.speed[0] + unit_t[1]*point.speed[1]
        v_1n, v_2n = v_2n, v_1n
        vec_v_1n = [unit_n[0] * v_1n, unit_n[1] * v_1n]
        vec_v_1t = [unit_t[0] * v_1t, unit_t[1] * v_1t]
        vec_v_2n = [unit_n[0] * v_2n, unit_n[1] * v_2n]
        vec_v_2t = [unit_t[0] * v_2t, unit_t[1] * v_2t]

        self.speed = (vec_v_1n[0] + vec_v_1t[0], vec_v_1n[1] + vec_v_1t[1])
        point.speed = (vec_v_2n[0] + vec_v_2t[0], vec_v_2n[1] + vec_v_2t[1])
        self.limit_speed()
        point.limit_speed()

    def getState(self):
        x = int(round(self.pos[0]//50))
        y = int(round(self.pos[1]//50))
        if x<0:
            x=0
        if y<0:
            y=0
        Vx = int(round(self.speed[0]+self.max_speed))
        Vy = int(round(self.speed[1]+self.max_speed))
        return [x,y,Vx,Vy]
