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

        # validado = False
        while True:
            try:
                pin = self.vista.asignar(leyenda, lista_pines)
                self.vista.mostrar_success('pin ingresado ' + repr(pin))
                # validado = True
                return pin
            except (TypeError, ValueError, Exception) as e:
                print(e.args)

    def __cargar_pines__(self):

        # Asignacion de la posicion del pin correspondiente al Trigger del ultrasonido
        trigger_pin = self.__asignar__('Ingrese pin correspondiente al Trigger', self.sonar.pines_digitales_disponibles)
        self.sonar.asignar_trigger(trigger_pin)

        # Asignacion de la posicion del pin correspondiente al Echo del ultrasonido
        echo_pin = self.__asignar__('Ingrese pin correspondiente al Echo', self.sonar.pines_digitales_disponibles)
        self.sonar.asignar_echo(echo_pin)

        # Asignacion de la posicion del pin correspondiente al servo-motor
        servo_pin = self.__asignar__("Ingrese pin correspondiente al Servo", self.sonar.pines_rpm_disponibles)
        self.sonar.asignar_servo(servo_pin)

    def iniciarSonar(self):
        try:
            self.sonar.mover(0) # posiciono el sonar en el inicio
            while True:
                for angulo in range (0, 181, 45):
                    self.sonar.mover(angulo)
                    self.sonar.__delay__(1.5)
                    distancia = self.sonar.getDistancia()
                    self.vista.set_sonar(angulo, distancia)

        except Exception as e:
            self.vista.mostrar_alerta(e.args)

    def iniciar(self):

        self.vista.iniciar()

        self.__cargar_pines__()

        self.__conectar_arduino_A_USB__()

        self.iniciarSonar()










