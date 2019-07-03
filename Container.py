import random as r
from tkinter import *
import numpy as np
import math
from scipy.ndimage.filters import gaussian_filter1d


from Atom import Atom


class Container(Canvas):
    def __init__(self, master, containerConfig, atomConfig):
        """
        Inicjuje pojemnik, zawierający atomy. Właściwoći definiuje config
        Na ten moment liczba atomów jest związana z wysokością tablicy i jest jer równa,
         a każdy atom pojawia się na środku komórki
        """
        self.config = containerConfig
        self.width = int(self.config['width'])
        self.height = int(self.config['height'])
        self.frames_number = master.get_frames_number()
        self.width_container = int(self.config['width'])*self.frames_number
        self.height_container = int(self.config['height'])*self.frames_number
        self.tick_rate = int(self.config['tick_rate'])
        self.number_of_atoms = int(self.config['number_of_atoms'])
        self.radius_error = float(self.config['radius_error'])
        self.atomsConfig = atomConfig
        self.master = master
        self.tk = master.tk
        self.x = []
        self.y = []
        self._after = None
        self.red = None
        self.statesPerm = []
        self.tickCount=0
        super().__init__(master, background='#' + self.config['background'])
        self.place(x=1, y=80, width=self.frames_number * self.width, height=(self.frames_number) * self.width)
        self.draw_gui()
        self.atoms = np.empty(0)
        self.generate_states()


    def generate_states(self):
        max_state_position = self.frames_number
        max_state_speed = int(float(self.atomsConfig['max_speed'])*2)+1
        for v in range(max_state_position):
            for x in range(max_state_position):
                for y in range(max_state_speed+1):
                    for z in range(max_state_speed):
                        self.statesPerm.append([v,x,y,z])


    def draw_gui(self):
        for i in range(1, self.frames_number):
            self.create_line(i * self.width, 0, i * self.width, (self.frames_number) * self.width, fill='#D9CCFF')

        for i in range(1, self.frames_number):
            self.create_line(0, i * self.width, self.frames_number * self.width, i * self.width, fill='#D9CCFF')

    def generate_atoms(self):
        atoms = []
        for i in range(self.number_of_atoms):
            atoms.append(
                Atom(self, r.randint(int(self.atomsConfig['radius']), self.width - int(self.atomsConfig['radius'])),
                     r.randint(int(self.atomsConfig['radius']), (self.frames_number) * self.width) - int(
                         self.atomsConfig['radius']),
                     r.uniform(int(self.config['min_speed']), int(self.config['max_speed'])),
                     r.uniform(int(self.config['min_speed']), int(self.config['max_speed'])),
                     str(i),
                     self.atomsConfig)
                )
        self.atoms = np.asarray(atoms)
        self.red = self.create_line(self.width, 0, self.width, (self.frames_number) * self.width, fill="red")

    def delete_atoms(self):
        if self.atoms.shape[0] > 0:
            for i in range(len(self.atoms)):
                atom = self.atoms[i]
                self.delete(atom.point)
                del atom
            np.delete(self.atoms, 0)
        self.x=[]
        self.y=[]
        chart = self.master.chart
        chart.plt.clf()
        chart.plt.add_subplot(111).plot(self.x,self.y)
        chart.canvas.draw()

    def serve_colisions(self):
        radius = int(self.atomsConfig['radius'])
        error = self.radius_error
        for i in range(self.number_of_atoms):
            atom1 = self.atoms[i]
            for j in range(i+1, self.number_of_atoms):
                atom2 = self.atoms[j]
                dist = atom1.distance(atom2)
                if dist <= 2*radius and dist > radius*1.5:
                    atom1.is_collision(atom2)
                    atom1.limit_speed()
            atom1.is_wall()

    def replot(self):
        self.x.append(self.tickCount)
        self.y.append(self.entropy())
        yNew = gaussian_filter1d(self.y, sigma=2)
        self.master.chart.plot(self.x,yNew)


    def tick(self):
        self.serve_colisions()
        if self.tickCount % 10 ==0:
            self.replot()

        for i in range(len(self.atoms)):
            self.atoms[i].move()
        self._after = self.master.after(self.tick_rate, self.tick)
        self.tickCount += 1

    def atoms_pos(self, scale=(1, 1)):
        output = []
        for i in range(self.number_of_atoms):
            output.append((self.atoms[i].pos[0] * scale[0], self.atoms[i].pos[1] * scale[1]))
        return output

    def atoms_speed(self):
        output = []
        for i in range(self.number_of_atoms):
            output.append(self.atoms[i].speed)
        return output

    def export_pixels(self, h=500, w=500):
        pixels = self.atoms_pos((h // self.height, w // self.width))
        for i in range(len(pixels)):
            pixels[i] = (round(pixels[i][0]), round(pixels[i][1]))
        return pixels

    # zwraca tuplę z zawartością: (prawdopodobienstwo_termodynamiczne,entropia)
    def entropy(self):
        # x = math.factorial(self.number_of_atoms)
        y = 1.0
        counted_atoms = self.generate_counted_atoms_list()
        for i in range(len(counted_atoms)):
            y *= math.factorial(counted_atoms[i])
        #Alternatywa - suma logartymow
        n = self.number_of_atoms
        x = n * math.log(n) - n
        print(str(x),str(math.log(y)))

        return x - math.log(y)

    def generate_counted_atoms_list(self):
        countedStates = []
        for i in range(len(self.statesPerm)):
            countedStates.append(0)
        for i in self.atoms:
            stateId=self.statesPerm.index(i.getState())
            countedStates[stateId] += 1
        return countedStates

    def __str__(self):
        return f"Pojemnik po rozmiarach {self.width} x {self.height}, zawierający {len(self.atoms)} atomów"
