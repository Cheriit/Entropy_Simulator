import random as r

class Atom:
    def __init__(self, x, y, speed_x, speed_y):
        self.pos = (x, y)
        self.speed = (speed_x, speed_y)
        self.mass = 1
        self.radius = 0.1

    def __str__(self):
        return f"Pozycja: {self.pos}\n" \
            f"Prędkość: {self.speed}\n" \
            f"Stałe: masa = {self.mass}, promień = {self.radius}"

    def access_atom(self):
        return self.pos[0], self.pos[1], self.speed[0], self.speed[1]

    def move(self, step=0.05):
        self.pos = (self.pos[0] + self.speed[0]*step, self.pos[1] + self.speed[1]*step)


class Pojemnik:
    def __init__(self, x, y):
        self.width = x
        self.height = y
        self.atoms = []
        for h in range(self.height):
            self.atoms.append(Atom(0.5, h + 0.5, r.uniform(-1, 1), r.uniform(-1, 1)))

    def tick(self):
        for i in range(len(self.atoms)):
            self.atoms[i].move()

    def __str__(self):
        return f"Pojemnik po rozmiarach {self.width} x {self.height}, zawierający {len(self.atoms)} cząstek"
# TODO: Zrobić dokumentację


if __name__ == "__main__":
    atomy = []
    for i in range(3):
        atomy.append(Atom(1, 1, 1, 1))
    print(atomy[1].access_atom())
    pojemnik = Pojemnik(5, 5)
    for i in range(5):
        print(pojemnik.atoms[i].access_atom())
    for i in range(5):
        pojemnik.atoms[i].move()
    for i in range(5):
        print(pojemnik.atoms[i].access_atom())
    print(pojemnik)
