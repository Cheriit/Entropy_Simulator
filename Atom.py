import random as r


class Atom:
    def __init__(self, master, x, y, speed_x, speed_y, name, config):
        self.config = config
        self.pos = (x, y)
        self.speed = (speed_x, speed_y)
        self.radius = float(self.config['radius'])
        self.name = name
        self.master = master
        self.color = '#%02x%02x%02x'%(
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
        self.pos = (
            self.pos[0] + self.speed[0] * (1 / self.master.tick_rate),
            self.pos[1] + self.speed[1] * (1 / self.master.tick_rate)
        )
        self.master.move(self.point,
                         self.speed[0] * (1 / self.master.tick_rate),
                         self.speed[1] * (1 / self.master.tick_rate))
