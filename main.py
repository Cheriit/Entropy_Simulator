import configparser

from Window import Window

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')
    gui = Window(config)

    gui.mainloop()
