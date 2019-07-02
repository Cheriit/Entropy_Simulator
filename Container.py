import random as r
from tkinter import *
import numpy as np
import math

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
        self.height_container = int(self.config['height'])*self.frames_number//2
        self.tick_rate = int(self.config['tick_rate'])
        self.number_of_atoms = int(self.config['number_of_atoms'])
        self.radius_error = float(self.config['radius_error'])
        self.atomsConfig = atomConfig
        self.master = master
        self.tk = master.tk
        self.x = [0]
        self.y = [0.0]
        self._after = None
        self.red = None

        super().__init__(master, background='#' + self.config['background'])
        # self.canvas = Canvas()
        self.place(x=1, y=80, width=self.frames_number * self.width, height=(self.frames_number // 2) * self.width)
        # self.pack()
        self.draw_gui()
        self.atoms = np.empty(0)

    def draw_gui(self):
        for i in range(1, self.frames_number):
            self.create_line(i * self.width, 0, i * self.width, (self.frames_number // 2) * self.width, fill='#D9CCFF')

        for i in range(1, self.frames_number):
            self.create_line(0, i * self.width, self.frames_number * self.width, i * self.width, fill='#D9CCFF')

    def generate_atoms(self):
        atoms = []
        for i in range(self.number_of_atoms):
            atoms.append(
                Atom(self, r.randint(int(self.atomsConfig['radius']), self.width - int(self.atomsConfig['radius'])),
                     r.randint(int(self.atomsConfig['radius']), (self.frames_number // 2) * self.width) - int(
                         self.atomsConfig['radius']),
                     r.uniform(int(self.config['min_speed']), int(self.config['max_speed'])),
                     r.uniform(int(self.config['min_speed']), int(self.config['max_speed'])),
                     str(i),
                     self.atomsConfig)
                )
        self.atoms = np.asarray(atoms)
        self.red = self.create_line(self.width, 0, self.width, (self.frames_number // 2) * self.width, fill="red")

    def delete_atoms(self):
        # print(str(self.atoms.shape))
        if self.atoms.shape[0] > 0:
            for i in range(len(self.atoms)):
                atom = self.atoms[i]
                self.delete(atom.point)
                del atom
            np.delete(self.atoms, 0)
        self.x=[0]
        self.y=[0]
        chart = self.master.chart
        chart.plt.clf()
        chart.plt.add_subplot(111).plot(self.x,self.y)
        chart.canvas.draw()
        # self.master.after_cancel(self.tick)

    def serve_colisions(self):
        radius = int(self.atomsConfig['radius'])
        error = self.radius_error
        for i in range(self.number_of_atoms):
            atom1 = self.atoms[i]
            for j in range(i+1, self.number_of_atoms):
                atom2 = self.atoms[j]
                if atom1.distance(atom2) <= 2*radius-error:
                    atom1.is_collision(atom2)
            atom1.is_wall()

    def replot(self):
        chart = self.master.chart
        self.x.append(self.x[-1]+1)
        self.y.append(self.entropy()[1])
        chart.plt.add_subplot(111).plot(self.x, self.y, color='red')
        chart.canvas.draw()

    def tick(self):
        self.serve_colisions()
        for i in range(len(self.atoms)):
            self.atoms[i].move()
        # print(str(self.generate_counted_atoms_list()))
        self.replot()
        self._after = self.master.after(self.tick_rate, self.tick)

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
        x = math.factorial(self.number_of_atoms)
        y = 1
        counted_atoms = self.generate_counted_atoms_list()
        for i in range(len(counted_atoms)):
            y *= (math.factorial(counted_atoms[i]))

        return x/y, math.log(x/y)

    def generate_counted_atoms_list(self):
        counted_atoms = np.zeros(self.frames_number)
        width = self.width
        for i in self.atoms:
            counted_atoms[int(i.pos[0]//width)] += 1
        return counted_atoms

    def __str__(self):
        return f"Pojemnik po rozmiarach {self.width} x {self.height}, zawierający {len(self.atoms)} atomów"
