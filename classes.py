import random as r


class Atom:
    def __init__(self, x, y, speed_x, speed_y, name, config):
        self.config = config
        self.pos = (x, y)
        self.speed = (speed_x, speed_y)
        self.radius = float(self.config['radius'])
        self.name = name

    def __str__(self):
        return f"Atom \"{self.name}\"\n" \
            f"Pozycja: {self.pos}\n" \
            f"Prędkość: {self.speed}\n"

    def access_atom(self):
        return self.pos[0], self.pos[1], \
               self.speed[0], self.speed[1]

    def move(self, tickrate=20):
        self.pos = (
            self.pos[0] + self.speed[0] * (1 / int(tickrate)),
            self.pos[1] + self.speed[1] * (1 / int(tickrate))
        )


class Container:
    def __init__(self, containerConfig, atomConfig):
        """
        Inicjuje pojemnik, zawierający atomy. Właściwoći definiuje config
        Na ten moment liczba atomów jest związana z wysokością tablicy i jest jer równa,
         a każdy atom pojawia się na środku komórki
        """
        self.config = containerConfig
        self.width = int(self.config['width'])
        self.height = int(self.config['height'])
        self.tickrate = int(self.config['tickrate'])
        self.number_of_atoms = int(self.config['number_of_atoms'])

        self.atoms = []
        for i in range(self.number_of_atoms):
            self.atoms.append(Atom(r.uniform(0, 1), r.uniform(0, self.height),
                                   r.uniform(int(self.config['min_speed']), int(self.config['max_speed'])),
                                   r.uniform(int(self.config['min_speed']), int(self.config['max_speed'])),
                                   i, atomConfig))

    def tick(self):
        for i in range(len(self.atoms)):
            self.atoms[i].move(self.tickrate)
        # canvas.after(self.tickrate , self.tick())

    def atoms_pos(self, scale=(1, 1)):
        output = []
        for i in range(self.number_of_atoms):
            output.append((self.atoms[i].pos[0]*scale[0], self.atoms[i].pos[1]*scale[1]))
        return output

    def atoms_speed(self):
        output = []
        for i in range(self.number_of_atoms):
            output.append(self.atoms[i].speed)
        return output

    def export_pixels(self, h=500, w=500):
        pixels = self.atoms_pos((h//self.height, w//self.width))
        for i in range(len(pixels)):
            pixels[i] = (round(pixels[i][0]), round(pixels[i][1]))
        return pixels

    def __str__(self):
        return f"Pojemnik po rozmiarach {self.width} x {self.height}, zawierający {len(self.atoms)} atomów"
