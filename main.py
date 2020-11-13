# main class #
from mvc.Controllers.MainController import MainController
from mvc.Models.ConectorUsb import ConectorUsb
from mvc.Models.Sonar import Sonar
from Arduino import Arduino


def main():
    controller = MainController()
    controller.iniciar()


if __name__ == '__main__':
    main()
