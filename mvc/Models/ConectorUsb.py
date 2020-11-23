# los metodos dentro de esta clase se encargan de la coneccion a los puertos usb #
import serial.tools.list_ports


class ConectorUsb:
    _DESCRIPCION_PUERTO = 1
    _NOMBRE_PUERTO = 0

    @staticmethod
    def get_all_ports():
        return list(serial.tools.list_ports.comports())

    @staticmethod
    def get_arduino_ports():

        puertos_arduinos = []

        ports = list(serial.tools.list_ports.comports())

        for port in ports:
            if 'Arduino' in port[ConectorUsb._DESCRIPCION_PUERTO]:
                puertos_arduinos.append(port)

        return puertos_arduinos

    @staticmethod
    def get_nombre(puerto):
        return puerto[ConectorUsb._NOMBRE_PUERTO]

    @staticmethod
    def get_descripcion(puerto):
        return puerto[ConectorUsb._DESCRIPCION_PUERTO]
