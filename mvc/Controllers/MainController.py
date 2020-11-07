from mvc.Views.VistaConsola import VistaConsola
from mvc.Models.Sonar import Sonar
from mvc.Models.ConectorUsb import ConectorUsb


class MainController:

    pines_digitales_disponibles = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    pines_rpm_disponibles = [3, 5, 7]

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
            self.sonar.conectar(puerto[ConectorUsb.__NOMBRE_PUERTO__])
            self.vista.mostrar("Arduino conectado al puerto " + puerto[ConectorUsb.__NOMBRE_PUERTO__])
        elif cantidad_puertos > 1:
            pass  # TODO: hacer la vista para manejar mas de un puerto conectado

    def __asignar__(self, leyenda, lista_pines):

        validado = False
        while validado:
            try:
                pin = self.vista.asignarPin(leyenda, lista_pines)
                if pin in self.pines_digitales_disponibles:
                    self.pines_digitales_disponibles.remove(pin)
                if pin in self.pines_rpm_disponibles:
                    self.pines_rpm_disponibles.remove(pin)
                validado = True
                return pin
            except (TypeError, ValueError, Exception) as e:
                print(e.args)

    def iniciar(self):

        self.vista.iniciar()

        # TODO: arreglar los try/catch de ingreso de pines
        trigger_pin = self.__asignar__('Ingrese pin correspondiente al trigger', self.pines_digitales_disponibles)
        echo_pin = self.__asignar__('Ingrese pin correspondiente al trigger', self.pines_digitales_disponibles)
        servo_pin = self.__asignar__("Ingrese pin correspondiente al trigger", self.pines_rpm_disponibles)

      #  self.sonar = Sonar(trigger_pin, echo_pin, servo_pin)

        print( trigger_pin, echo_pin, servo_pin)
        #self.__conectar_arduino_A_USB__()

       # self.vista.mostrar(str(self.sonar.getDistancia()))
