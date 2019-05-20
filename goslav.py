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


if __name__ == "__main__":
    atomy = []
    for i in range(3):
        atomy.append(Atom(1, 1, 1, 1))
    print(atomy[1].access_atom())
