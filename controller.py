

class Controller(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Add callbacks
        self.view.b1.config(command = self.model.increaseValue)
        self.view.b2.config(command = self.model.decreaseValue)

    def run(self):
        while not self.model.done:
            self.view.setLabel(self.model.value)
            self.view.run()