

class Model(object):
    def __init__(self, value=0):
        self.value = value
        self.done = False

    def increaseValue(self, amount=1):
        self.value += amount

    def decreaseValue(self, amount=1):
        self.value -= amount