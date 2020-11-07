
from mvc.Models.Sonar import Sonar
from mvc.Models.ConectorUsb import ConectorUsb
from mvc.Views.VistaConsola import VistaConsola


class MainController:
    pines_digitales_disponibles = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    pines_rpm_disponibles = [3, 5, 6, 9, 10, 11]

    def __init__(self):
        self.vista = VistaConsola()
        self.sonar = None

    def __conectar_arduino_A_USB__(self):
        #TODO: hacer que la vista pregunte por reintentar conexion o no
        puertos_arduino_disponibles = ConectorUsb.getArduinoPorts()
        cantidad_puertos = len(puertos_arduino_disponibles)
        if cantidad_puertos == 0:
            self.vista.mostrar("El Arduino no esta Conectado a ningun puerto")
        elif cantidad_puertos == 1:
            puerto = puertos_arduino_disponibles[0]
            self.vista.mostrar("Conectando...")
            self.sonar.conectar(puerto[ConectorUsb.__NOMBRE_PUERTO__])
            self.vista.mostrar("Arduino conectado al puerto " + puerto[ConectorUsb.__NOMBRE_PUERTO__])
        elif cantidad_puertos > 1:
            pass  # TODO: hacer la vista para manejar mas de un puerto conectado

    def __asignar__(self, leyenda, lista_pines):

        validado = False
        while not validado:
            try:
                pin = self.vista.asignar(leyenda, lista_pines)

                validado = True
                return pin
            except (TypeError, ValueError, Exception) as e:
                print(e.args)

    def __cargar_pines__(self):
        trigger_pin = self.__asignar__('Ingrese pin correspondiente al Trigger', self.sonar.pines_digitales_disponibles)
        self.sonar.asignar_trigger(trigger_pin)

        echo_pin = self.__asignar__('Ingrese pin correspondiente al Echo', self.sonar.pines_digitales_disponibles)
        self.sonar.asignar_echo(echo_pin)

        servo_pin = self.__asignar__("Ingrese pin correspondiente al Servo", self.sonar.pines_rpm_disponibles)
        self.sonar.asignar_echo(servo_pin)

    def iniciar(self):

        self.vista.iniciar()
        self.sonar = Sonar()

        self.__cargar_pines__()

        self.__conectar_arduino_A_USB__()

        while True:
            try:
                distancia = self.sonar.getDistancia()
                self.vista.mostrar('Distancia = ' + repr(distancia))
            except Exception as e:
                print(e.args)
