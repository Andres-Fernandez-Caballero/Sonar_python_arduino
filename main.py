# main class #
from mvc.Models.ConectorUsb import  ConectorUsb
from mvc.Models.Sonar import Sonar

def main():
    #controller = MainController()
    #controller.iniciar()

    # TODO: prueba de metodos de clase Sonar (eliminar despues)
    lista = ConectorUsb.getArduinoPorts()
    puerto = lista[0]
    print(ConectorUsb.getNombre(puerto))

    sonar = Sonar(3, 4, 5)

    sonar.conectar(ConectorUsb.getNombre(puerto))

    sonar.mover(90)

if __name__ == '__main__':
    main()
