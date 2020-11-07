# VistaConsola provee una clase encargada de generar entradas y salidas de consola a mode de vista #


def validarentradas(entrada, pines_disponibles):
    if not entrada.isnumeric():
        raise TypeError("Debe ingresarse un tipo de valor entero entre " + repr(pines_disponibles))
    elif not int(entrada) in pines_disponibles:
        raise ValueError("campos fuera de rango")
    else:
        return int(entrada)


class VistaConsola:

    def __init__(self):
        self.isActiva = None

    def iniciar(self):
        self.isActiva = True
        self.mostrar("Bienvenido al sonar")

    def mostrar(self, mensaje):
        print(mensaje)

    def asignar(self, leyenda, pines_disponibles):
        texto_input = leyenda + '\npines disponibles ' + repr(pines_disponibles) + ' -> '
        entrada = input(texto_input)
        return validarentradas(entrada, pines_disponibles)
