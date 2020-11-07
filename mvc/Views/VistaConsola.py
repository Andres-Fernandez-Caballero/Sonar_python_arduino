# VistaConsola provee una clase encargada de generar entradas y salidas de consola a mode de vista #


def validarEntradas(entrada, pines_disponibles):
    if not entrada.isnumeric():
        raise TypeError("Debe ingresarse un tipo de valor entero entre " + repr(pines_disponibles))
    elif int(entrada) < pines_disponibles[0] or int(entrada) > pines_disponibles[(len(pines_disponibles)) - 1]:
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

    def asignarPin(self, leyenda, pines_disponibles):
        texto_imput = leyenda + '\npines disponibles ' + repr(pines_disponibles) + ' -> '
        entrada = input(texto_imput)

        return validarEntradas(entrada, pines_disponibles)
