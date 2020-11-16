import time

from mvc.Models.Sonar import Sonar
from mvc.Models.ConectorUsb import ConectorUsb
from mvc.Views.VistaConsola import VistaConsola
from funciones.tiempo import pausa


class MainController:
    pines_digitales_disponibles = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    pines_rpm_disponibles = [3, 5, 6, 9, 10, 11]

    def __init__(self):
        self.vista = VistaConsola()
        self.sonar = Sonar()

    def _conectar_arduino_a_usb(self):
        # TODO: hacer que la vista pregunte por reintentar conexion o no
        puertos_arduino_disponibles = ConectorUsb.get_arduino_ports()
        cantidad_puertos = len(puertos_arduino_disponibles)

        if cantidad_puertos == 0:
            self.vista.mostrar_alerta("El Arduino no esta Conectado a ningun puerto")
            exit(-0)  # finalizo el programa con codigo 0
        elif cantidad_puertos == 1:
            puerto = puertos_arduino_disponibles[0]

            self.vista.mostrar("Conectando...")
            try:
                self.sonar.conectar(ConectorUsb.get_nombre(puerto))
            except Exception as e:
                self.vista.mostrar_alerta(e.args)
                exit(0)  # salgo del programa con codigo 0

            # self.sonar.conectar(puerto[ConectorUsb.__NOMBRE_PUERTO__]) # obsoleto
            self.vista.mostrar("Arduino conectado al puerto " + ConectorUsb.get_nombre(puerto))
        elif cantidad_puertos > 1:
            pass  # TODO: hacer la vista para manejar mas de un puerto conectado

    def _asignar(self, leyenda, lista_pines):

        # validado = False
        while True:
            try:
                pin = self.vista.asignar(leyenda, lista_pines)
                self.vista.mostrar_success('pin ingresado ' + repr(pin))
                # validado = True
                return pin
            except (TypeError, ValueError, Exception) as e:
                print(e.args)

    def _cargar_pines(self):

        # Asignacion de la posicion del pin correspondiente al Trigger del ultrasonido
        trigger_pin = self._asignar('Ingrese pin correspondiente al Trigger', self.sonar.pines_digitales_disponibles)
        self.sonar.trigger = trigger_pin

        # Asignacion de la posicion del pin correspondiente al Echo del ultrasonido
        echo_pin = self._asignar('Ingrese pin correspondiente al Echo', self.sonar.pines_digitales_disponibles)
        self.sonar.echo = echo_pin

        # Asignacion de la posicion del pin correspondiente al servo-motor
        servo_pin = self._asignar("Ingrese pin correspondiente al Servo", self.sonar.pines_rpm_disponibles)
        self.sonar.servo = servo_pin

    def iniciar_sonar(self):
        try:
            self.sonar.mover(0) # coloco el servo en la posicion inicial
            while True:
                for angulo in range(0, 180, 45):

                    distancia = self.sonar.getDistancia()
                    self.vista.set_sonar(angulo, distancia)
                    pausa(1)
                    distancia = self.sonar.getDistancia()
                    self.vista.set_sonar(angulo, distancia)
                    pausa(1)
                    distancia = self.sonar.getDistancia()
                    self.vista.set_sonar(angulo, distancia)

                    self.sonar.mover(angulo)
                    pausa(1)

        except Exception as e:
            self.vista.mostrar_alerta(e.args)

    def prueba_distancia(self):
        try:
            while True:
                distancia = self.sonar.getDistancia()
                self.vista.mostrar_info(distancia)
        except Exception as e:
            self.vista.mostrar_alerta(e.args)

    def iniciar(self):

        self.vista.iniciar()

        self._cargar_pines()

        self._conectar_arduino_a_usb()

        self.iniciar_sonar()

        # self.prueba_distancia()










