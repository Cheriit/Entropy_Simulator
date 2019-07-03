from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from Container import Container
from chart import chart


class Window(Tk):
    def __init__(self, config):
        super().__init__()
        self.config = config['Window']
        self.frames_numbers = int(self.config['frame_numbers'])
        self.generate_gui(config)

    def generate_gui(self, config):
        self.title('Entropia')

        self.geometry(
            str(self.frames_numbers * 55 +460) + 'x' + str((self.frames_numbers) * 50 + 80)
        )

        # self.frame_start = self.generate_frames()
        self.frame_start = Frame(master=self, background='#F3E77F')
        self.frame_start.pack(side=LEFT,fill=Y)

        self.frame_start.place(x=1, y=1, width=self.frames_numbers * 50 , height=80)

        self.container = Container(self, config['Container'], config['Atom'])


        self.generate_buttons()

        self.chart = chart(self)
        self.chart.place( y=80, x=self.frames_numbers * 51 ,width=600, height=400)
        self.chart.pack(side=RIGHT,fill=Y)
        self.resizable(False, False)

    def get_frames_number(self):
        return self.frames_numbers

    def generate_buttons(self):
        self.button_generate = self.generate_button(self.frame_start, 'Generuj Atomy', self.generate_atoms, NORMAL,
                                                    10, 40, 100, 20)

        self.button_stop = self.generate_button(self.frame_start, 'STOP', self.STOP, DISABLED,
                                                (self.frames_numbers * 50) // 2,
                                                40, 100, 20)

        self.button_start = self.generate_button(self.frame_start, 'START', self.START, DISABLED,
                                                 (self.frames_numbers * 50 - 200) // 2,
                                                 40, 98, 20)

    def generate_button(self, master, text, command, state, x, y, width, height):
        button = Button(master=master, text=text, command=command)
        button.config(state=state)
        button.place(x=x, y=y, width=width, height=height)

        return button

    def generate_atoms(self):
        self.container.delete_atoms()
        self.container.generate_atoms()
        self.button_generate.config(state=DISABLED)
        self.button_start.config(state=NORMAL)

    def START(self):
        self.container.delete(self.container.red)
        self.container.tick()
        self.button_start.config(state=DISABLED)
        self.button_stop.config(state=NORMAL)
        self.button_generate.config(state=DISABLED)

    def STOP(self):
        self.after_cancel(self.container._after)
        self.button_stop.config(state=DISABLED)
        self.button_start.config(state=NORMAL)
        self.button_generate.config(state=NORMAL)

    def __str__(self):
        return "GUI"
