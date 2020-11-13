# main class #
from mvc.Controllers.MainController import MainController
from mvc.Models.ConectorUsb import ConectorUsb
from mvc.Models.Sonar import Sonar
from Arduino import Arduino


def main():
    controller = MainController()
    controller.iniciar()

    """
     # esto anda #
    board = Arduino(115200, 'COM10')
    print('conectado !!!')

    board.Servos.attach(9)
    board.Servos.write(90)
    print(board.Servos.read(9))
    """


if __name__ == '__main__':
    main()
