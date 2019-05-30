import random as r
from tkinter import *
import numpy as np

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
        self.tick_rate = int(self.config['tick_rate'])
        self.number_of_atoms = int(self.config['number_of_atoms'])
        self.radius_error = float(self.config['radius_error'])
        self.atomsConfig = atomConfig
        self.master = master
        self.tk = master.tk

        self.frames_number = master.get_frames_number()

        super().__init__(master, background='#' + self.config['background'])
        # self.canvas = Canvas()
        self.place(x=1, y=80, width=self.frames_number * 51, height=(self.frames_number // 2) * 50)
        # self.pack()
        self.draw_gui()
        self.atoms = np.empty(0)

    def draw_gui(self):
        for i in range(1, self.frames_number):
            self.create_line(i * 51, 0, i * 51, (self.frames_number // 2) * 51, fill='#D9CCFF')

        for i in range(1, self.frames_number):
            self.create_line(0, i * 51, self.frames_number * 51, i * 51, fill='#D9CCFF')

    def generate_atoms(self):
        atoms = []
        for i in range(self.number_of_atoms):
            atoms.append(
                Atom(self, r.randint(int(self.atomsConfig['radius']), 51 - int(self.atomsConfig['radius'])),
                     r.randint(int(self.atomsConfig['radius']), (self.frames_number // 2) * 51) - int(
                         self.atomsConfig['radius']),
                     r.uniform(int(self.config['min_speed']), int(self.config['max_speed'])),
                     r.uniform(int(self.config['min_speed']), int(self.config['max_speed'])),
                     str(i),
                     self.atomsConfig)
                )
        self.atoms = np.asarray(atoms)
        self.red = self.create_line(51, 0, 51, (self.frames_number // 2) * 51, fill="red")

    def delete_atoms(self):
        # print(str(self.atoms.shape))
        if self.atoms.shape[0] > 0:
            for i in range(len(self.atoms)):
                atom = self.atoms[i]
                self.delete(atom.point)
                del atom
            np.delete(self.atoms, 0)
        # self.master.after_cancel(self.tick)

    def serve_colisions(self):
        radius = int(self.atomsConfig['radius'])
        error = self.radius_error
        for i in self.atoms:
            for j in self.atoms:
                if i.distance(j)<=radius-error:
                    i.apply_collision(j)
                    break



    def tick(self):
        self.serve_colisions()
        for i in range(len(self.atoms)):
            self.atoms[i].move()
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

    def __str__(self):
        return f"Pojemnik po rozmiarach {self.width} x {self.height}, zawierający {len(self.atoms)} atomów"
