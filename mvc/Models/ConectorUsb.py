# los metodos dentro de esta clase se encargan de la coneccion a los puertos usb #
import serial.tools.list_ports


class ConectorUsb:
    __DESCRIPCION_PUERTO__ = 1
    __NOMBRE_PUERTO__ = 0

    @staticmethod
    def getAllPorts():
        return list(serial.tools.list_ports.comports())

    @staticmethod
    def getArduinoPorts():

        puertos_arduinos = []

        ports = list(serial.tools.list_ports.comports())

        for port in ports:
            if 'Arduino' in port[ConectorUsb.__DESCRIPCION_PUERTO__]:
                puertos_arduinos.append(port)

        return puertos_arduinos

    @staticmethod
    def getNombre(puerto):
        return puerto[ConectorUsb.__NOMBRE_PUERTO__]

    @staticmethod
    def getDescripcion(puerto):
        return puerto[ConectorUsb.__DESCRIPCION_PUERTO__]
