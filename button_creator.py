# this package is to handle creating each of the Checkbutton objects
from tkinter import *

stage = Tk()
class createCheckbutton:
    # initiate class fields
    def __init__(self, app_data):
        self.pad_X = 15
        self.pad_Y = 15
        self.apps = app_data
        self.ctrl = IntVar()
        self.button = self.make_button()

    # how is the app_data parameter being presented?
    def debug_func(self):
        print(self.apps)

    def _func(self):
        print("demo function triggered")
        print(self.ctrl.get())

    # for each app, return a functioning button
    def make_button(self):
        return Checkbutton(stage, text=self.apps['name'], variable=self.ctrl, command=self._func)

    def start_GUI(self):
        stage.mainloop()