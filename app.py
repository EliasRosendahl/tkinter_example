from model import Model
from view import View
from controller import Controller



def main():
    controller = Controller(Model(), View())
    controller.run()


if __name__ == "__main__":
    main()