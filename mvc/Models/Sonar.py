# define una clase plaqueta que reperesenta el modelo de una plaqueta Arduino #

from pyfirmata import Arduino, util
import time

__STATE_LOW__ = 0
__STATE_HIGH__ = 1

__PINES_DIGITALES__ = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
__PINES_RPM_DISPONIBLES__ = [3, 5, 6, 9, 10, 11]


class Sonar:

    def __init__(self):
        # objeto Arduino desde la libreria pyfirmata
        self.arduino = None

        # pines controladores
        self.trigger = None  # digital_output
        self.echo = None  # digital_input
        self.servo = None  # digital_rpm

        self.pines_digitales_disponibles = __PINES_DIGITALES__
        self.pines_rpm_disponibles = __PINES_RPM_DISPONIBLES__

        # hilo para las funciones rpm
        iterador = util.Iterator(self.arduino)
        iterador.start()

    def __restar_pines_disponibles__(self, pin):
        if pin in self.pines_digitales_disponibles:
            self.pines_digitales_disponibles.remove(pin)
        if pin in self.pines_rpm_disponibles:
            self.pines_rpm_disponibles.remove(pin)

    def asignar_trigger(self, pin_trigger):
        self.trigger = pin_trigger
        self.__restar_pines_disponibles__(pin_trigger)

    def asignar_echo(self, pin_echo):
        self.echo = pin_echo
        self.__restar_pines_disponibles__(pin_echo)

    def asignar_servo(self, pin_servo):
        self.servo = pin_servo
        self.__restar_pines_disponibles__(pin_servo)

    def conectar(self, puerto_arduino):
        self.arduino = Arduino(puerto_arduino)

    def prueba_blink(self, puerto_arduino):

        while True:
            self.__digitalWrite__(puerto_arduino, __STATE_HIGH__)
            self.__delay__(1)
            self.__digitalWrite__(puerto_arduino, __STATE_LOW__)
            self.__delay__(1)

    def getDistancia(self):
        # me aseguro que los pines esten iniciados sino arrojo una exepcion
        if self.trigger is None or self.echo is None:
            raise Exception("pines no iniciados")

        #  disparo el ultrasonido
        self.__digitalWrite__(self.trigger, __STATE_LOW__)
        Sonar.__delay__(1e-5)  # 2000 microsegundos
        self.__digitalWrite__(self.trigger, __STATE_HIGH__)
        Sonar.__delay__(1e-5)  # 15 microsegundos
        self.__digitalWrite__(self.trigger, __STATE_LOW__)
        Sonar.__delay__(1e-5)  # 10 microsegundos

        #  espero el eco

        while True:
            pulso_inicio = time.time()
            if self.__digitalRead__(self.echo) == __STATE_HIGH__\
                    or time.time() - pulso_inicio == 0.5:  # espera de 0,5 seg
                break
        while True:
            pulso_fin = time.time()
            if self.__digitalRead__(self.echo) == __STATE_LOW__\
                    or time.time() - pulso_inicio == 0.5:  # espera de 0,5 seg
                break

        duracion = pulso_fin - pulso_inicio

        velocidad_sonido = 34300  # cm/seg
        distancia = velocidad_sonido * duracion / 2

        return distancia  # cm

    def mover(self, angulo):
        # me aseguro que los pines esten iniciados sino arrojo una exepcion
        if self.servo is None:
            raise Exception("pin no iniciado")

        pin_mode = 'd:' + str(self.servo) + ':s'  # en base a la documentacion pyfirmata d:digital, numero_pin, s:servo

        servo = self.arduino.get_pin(pin_mode)

        servo.write(angulo)

    def __digitalWrite__(self, pin, state):
        self.arduino.digital[int(pin)].write(state)

    def __digitalRead__(self, pin):
        return self.arduino.digital[int(pin)].read()

    @staticmethod
    def __delay__(time_seg):
        time.sleep(time_seg)
