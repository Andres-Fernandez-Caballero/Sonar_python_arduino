# define una clase plaqueta que reperesenta el modelo de una plaqueta Arduino #

from Arduino import Arduino
import time

__BAUD_SPEED__ = 115200

__STATE_LOW__ = "LOW"
__STATE_HIGH__ = "HIGH"

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

        # lista de pines disponibles
        self.pines_digitales_disponibles = __PINES_DIGITALES__
        self.pines_rpm_disponibles = __PINES_RPM_DISPONIBLES__

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

    def conectar(self, puerto_arduino):  # obsoleto
        self.arduino = Arduino(__BAUD_SPEED__, puerto_arduino)

    def getDistancia(self):
        # me aseguro que los pines esten iniciados sino arrojo una exepcion
        if self.trigger is None or self.echo is None:
            raise Exception("pines no iniciados")

        self.__disparar__(self.trigger)

        # mido la duracion del pulso HIGH en el pin echo
        duracion = self.arduino.pulseIn(self.echo, __STATE_HIGH__)  # duracion = miliseg

        distancia = duracion / 29. / 2.  # cm ( esta ecuancion no me cierra pero da la medica correcta)

        velocidad_sonido = 34400  # cm/seg
        # distancia = velocidad_sonido * duracion / 2

        """
         Este if arregla un pequeño bug
         las primeras mediciones devuelve valores negativos hasta que se estabiliza el sensor
         """
        if distancia < 0:
            distancia = self.getDistancia()
        return distancia  # cm

    def mover(self, angulo):
        # me aseguro que los pines esten iniciados sino arrojo una exepcion
        if self.servo is None:
            raise Exception("pin no iniciado")
        if self.arduino is None:
            raise Exception("Arduino no conectado")
        board = self.arduino
        board.Servos.attach(self.servo) # TODO: aca rompe
        # self.arduino.Servos.write(self.servo, angulo)  # muevo el servo al angulo indicado
        # posicion = self.arduino.Servos.read(self.servo)  # recupero la posicion del angulo
        # self.arduino.Servos.detach(self.servo)  # libero el servo
        # return posicion

    def __digitalWrite__(self, pin, state):
        self.arduino.digitalWrite(int(pin), state)

    # devuelve un intriger 1 si es verdadero y 0 si es falso
    def __digitalRead__(self, pin):
        return self.arduino.digitalRead(int(pin))

    @staticmethod
    def __delay__(time_seg):
        time.sleep(time_seg)

    def __disparar__(self, trigger_pin):
        # hago una lectura para limpuar la basura en echo
        self.__digitalWrite__(self.echo, __STATE_LOW__)
        self.arduino.pinMode(self.echo, "INPUT")

        #  disparo el ultrasonido
        self.__digitalWrite__(self.trigger, __STATE_LOW__)
        Sonar.__delay__(4e-6)  # 4 microsegundos
        self.__digitalWrite__(self.trigger, __STATE_HIGH__)
        Sonar.__delay__(1e-5)  # 10 microsegundos
        self.__digitalWrite__(self.trigger, __STATE_LOW__)

