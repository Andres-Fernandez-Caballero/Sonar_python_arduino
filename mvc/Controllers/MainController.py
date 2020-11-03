from mvc.Views.VistaConsola import VistaConsola
from mvc.Models.Sonar import Sonar
from mvc.Models.ConectorUsb import ConectorUsb


class MainController:
    def __init__(self):
        self.vista = VistaConsola()
        self.sonar = None

    def __conectar_arduino_A_USB__(self):
        puertos_arduino_disponibles = ConectorUsb.getArduinoPorts()
        cantidad_puertos = len(puertos_arduino_disponibles)
        if cantidad_puertos == 0:
            self.vista.mostrar("El Arduino no esta Conectado a ningun puerto")
        elif cantidad_puertos == 1:
            puerto = puertos_arduino_disponibles[0]
            self.sonar.conectar(puerto[ConectorUsb.NOMBRE_PUERTO])
            self.vista.mostrar("Arduino conectado al puerto " + puerto[ConectorUsb.NOMBRE_PUERTO])
        elif cantidad_puertos > 1:
            pass  # TODO: hacer la vista para manejar mas de un puerto conectado

    def iniciar(self):

        self.vista.iniciar()

        # TODO: arreglar los try/catch de ingreso de pines
        try:
            trigger_pin = self.vista.asignarTriggerPin()
        except (ValueError, Exception):
            trigger_pin = self.vista.asignarTriggerPin()
        try:
            echo_pin = self.vista.asignarEchoPin()
        except (ValueError, Exception):
            echo_pin = self.vista.asignarEchoPin()
        try:
            servo_pin = self.vista.asignarServoPin()
        except (ValueError, Exception):
            servo_pin = self.vista.asignarServoPin()

        self.vista.mostrar("Pines Cargados")

        self.sonar = Sonar(trigger_pin, echo_pin, servo_pin)

        self.__conectar_arduino_A_USB__()

        self.vista.mostrar(str(self.sonar.getDistancia()))
