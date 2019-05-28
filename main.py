import configparser

from Window import Window

# class GuiView()
if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')
    gui = Window(config)

    # atoms = []
    # for i in range(3):
    #     atoms.append(Atom(1, 1, 1, 1, 1, config['Atom']))
    # print(atoms[1].access_atom())
    # print(atoms[0])

    # container = Container(config['Container'], config['Atom'])

    # for i in range(5):
    #     print(container.atoms[i].access_atom())
    #
    # for i in range(5):
    #     container.atoms[i].move()
    #
    # for i in range(5):
    #     print(container.atoms[i].access_atom())
    #
    # print(container)
    #
    # window = Window(config)
    # while True:
    #     gui.update_idletasks()
    #     gui.update()

    gui.mainloop()
