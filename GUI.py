from tkinter import *
import configparser
from classes import *


class Window():
    def __init__(self, config):

        self.config = config['Window']
        self.window = Tk()
        self.frame_numbers = int(self.config['frame_numbers'])
        self.window.title('Entropia')

        self.window.geometry(
            str(self.frame_numbers * 55 - 79) + 'x' + str((self.frame_numbers // 2) * 55 + 80)
        )

        self.frame_start = self.generate_frames()

        self.canvas = Canvas(self.frame_start, bg = 'pink')
        self.canvas.pack(side = RIGHT, fill = BOTH, expand = True)

        self.button_generate = self.generate_button('Generuj Atomy', self.generate_atoms, NORMAL, 1, 80, 98, 20)

        self.button_start = self.generate_button('START', self.START, DISABLED,
                                                 (self.frame_numbers * 55 - 279) // 2, 80, 98, 20)

        self.button_stop = self.generate_button('STOP', self.STOP, DISABLED, (self.frame_numbers * 55 - 79) // 2,
                                                80, 98, 20)

    def generate_frames(self):
        frame_start = Frame(master=self.window, background='#F3E77F')
        frame_start.place(x=1, y=1, width=self.frame_numbers * 55 - 77, height=104)

        for i in range(1, self.frame_numbers + 1):
            for j in range(1, (self.frame_numbers // 2) + 1):
                if i == 1:
                    fr = Frame(master=self.window,
                               background='#D5E88F')
                else:
                    fr = Frame(master=self.window,
                               background='#889E9D')

                fr.place(x=(i + 50 * (i - 1)), y=105 + j + 50 * (j - 1), width=50, height=50)

        return frame_start

    def generate_button(self, text, command, state, x, y, width, height):
        button = Button(master=self.frame_start, text=text, command=command)
        button.config(state=state)
        button.place(x=x, y=y, width=width, height=height)

        return button

    def generate_atoms(self):
        self.button_generate.config(state=DISABLED)
        self.button_start.config(state=NORMAL)

    def START(self):
        self.button_start.config(state=DISABLED)
        self.button_stop.config(state=NORMAL)

    def STOP(self):
        self.button_stop.config(state=DISABLED)
        self.button_start.config(state=NORMAL)

# class GuiView()
if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')
    atoms = []
    for i in range(3):
        atoms.append(Atom(1, 1, 1, 1, 1, config['Atom']))
    print(atoms[1].access_atom())
    print(atoms[0])

    container = Container(config['Container'], config['Atom'])

    for i in range(5):
        print(container.atoms[i].access_atom())

    for i in range(5):
        container.atoms[i].move()

    for i in range(5):
        print(container.atoms[i].access_atom())

    print(container)

    window = Window(config)
    while True:
        window.window.update_idletasks()
        window.window.update()
