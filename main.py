# main class #
from mvc.Models.ConectorUsb import  ConectorUsb
from mvc.Models.Sonar import Sonar


def main():
    #controller = MainController()
    #controller.iniciar()

    # TODO: prueba de metodos de clase Sonar (eliminar despues)
    lista = ConectorUsb.getArduinoPorts()

    if len(lista) != 0:
        puerto = lista[0]

        print(ConectorUsb.getNombre(puerto))

        sonar = Sonar(3, 4, 5)

        sonar.conectar(ConectorUsb.getNombre(puerto))

        sonar.mover(90)
    else:
        print("no hay arduinos conectados")


if __name__ == '__main__':
    main()
