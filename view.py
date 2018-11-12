import tkinter

class View(object):
    def __init__(self):
        self.window = tkinter.Tk()

        self.valueString = tkinter.StringVar()
        self.valueString.set(0)
        self.label = tkinter.Label(self.window, textvariable=self.valueString)
        self.label.pack()

        self.b1 = tkinter.Button(self.window, text = "+")
        self.b1.pack(side = tkinter.RIGHT)

        self.b2 = tkinter.Button(self.window, text = "-")
        self.b2.pack(side = tkinter.LEFT)
    
    def setLabel(self, value):
        self.valueString.set(value)
        print(value)

    def run(self):
        self.window.update_idletasks()
        self.window.update()