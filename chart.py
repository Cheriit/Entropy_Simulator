import matplotlib
import tkinter as tk
from tkinter import  ttk
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class chart(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self, parent)
        # label = tk.Label(self, text="Entopia!")
        # label.pack(pady=10, padx=10)

        self.plt = Figure(figsize=(5, 5), dpi=100)
        # self.plt.add_subplot(111).plot([0], [0])
        self.canvas = FigureCanvasTkAgg(self.plt, self)
        # self.canvas.xlabel('Tiki')
        # self.canvas.ylabel('Entropia')

        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

        # canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

