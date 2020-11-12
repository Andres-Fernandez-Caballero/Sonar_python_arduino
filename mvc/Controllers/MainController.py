import time

from mvc.Models.Sonar import Sonar
from mvc.Models.ConectorUsb import ConectorUsb
from mvc.Views.VistaConsola import VistaConsola


class MainController:
    pines_digitales_disponibles = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    pines_rpm_disponibles = [3, 5, 6, 9, 10, 11]

    def __init__(self):
        self.vista = VistaConsola()
        self.sonar = Sonar()

    def __conectar_arduino_A_USB__(self):
        #TODO: hacer que la vista pregunte por reintentar conexion o no
        puertos_arduino_disponibles = ConectorUsb.getArduinoPorts()
        cantidad_puertos = len(puertos_arduino_disponibles)

        if cantidad_puertos == 0:
            self.vista.mostrar_alerta("El Arduino no esta Conectado a ningun puerto")
            exit(-0)
        elif cantidad_puertos == 1:
            puerto = puertos_arduino_disponibles[0]

            self.vista.mostrar("Conectando...")
            try:
                #self.sonar = Sonar(puerto[ConectorUsb.__NOMBRE_PUERTO__])
                self.sonar.conectar(puerto[ConectorUsb.__NOMBRE_PUERTO__])
            except Exception as e:
                self.vista.mostrar_alerta(e.args)

            # self.sonar.conectar(puerto[ConectorUsb.__NOMBRE_PUERTO__]) # obsoleto
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
        trigger_pin = self.vista.asignar('Ingrese pin correspondiente al Trigger'
                                         , self.sonar.pines_digitales_disponibles)

        self.vista.mostrar_alerta('pin ingresado ' + repr(trigger_pin))
        self.sonar.asignar_trigger(trigger_pin)

        echo_pin = self.vista.asignar('Ingrese pin correspondiente al Echo'
                                      , self.sonar.pines_digitales_disponibles)

        self.vista.mostrar_alerta('pin ingresado ' + repr(echo_pin))
        self.sonar.asignar_echo(echo_pin)

        """
        servo_pin = self.__asignar__("Ingrese pin correspondiente al Servo", self.sonar.pines_rpm_disponibles)
        self.sonar.asignar_echo(servo_pin)
        """
    def iniciar(self):

        self.vista.iniciar()

        self.__conectar_arduino_A_USB__()

        self.__cargar_pines__()
        print('iniciando lectura de distancia')

        while True:
            try:
                lectura = self.sonar.getDistancia()
                self.vista.mostrar(lectura)
                time.sleep(1)
            except Exception as e:
                print(e.args)
