# VistaConsola provee una clase encargada de generar entradas y salidas de consola a mode de vista #


def validarEntradas(entrada):
    if entrada < 2 or entrada > 13:
        raise ValueError("campos fuera de rango")


class VistaConsola:

    def __init__(self):
        self.isActiva = None

    def iniciar(self):
        self.isActiva = True
        self.mostrar("Bienvenido al sonar")

    def mostrar(self, mensaje):
        print(mensaje)

    def asignarTriggerPin(self):
        validarEntradas(int(input("Ingrese el pin asignado al Trigger (2-13)")))

    def asignarEchoPin(self):
        validarEntradas(int(input("Ingrese el pin asignado al Echo (2-13)")))

    def asignarServoPin(self):
        validarEntradas(int(input("Ingrese el pin asignado al Servo (2-13)")))
