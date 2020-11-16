# define una clase plaqueta que reperesenta el modelo de una plaqueta Arduino #

from Arduino import Arduino
import time

_BAUD_SPEED = 115200

_STATE_LOW = "LOW"
_STATE_HIGH = "HIGH"

_PINES_DIGITALES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
_PINES_RPM = [3, 5, 6, 9, 10, 11]


class Sonar(object):

    def __init__(self):
        # objeto Arduino desde la libreria pyfirmata
        self._arduino = None

        # pines controladores
        self._trigger = None  # digital_output
        self._echo = None  # digital_input
        self._servo = None  # digital_rpm

        # lista de pines disponibles
        self._pines_digitales_disponibles = _PINES_DIGITALES
        self._pines_rpm_disponibles = _PINES_RPM

    def _restar_pines_disponibles(self, pin):
        if pin in self.pines_digitales_disponibles:
            self.pines_digitales_disponibles.remove(pin)
        if pin in self._pines_rpm_disponibles:
            self._pines_rpm_disponibles.remove(pin)

    # getters y setters
    @property
    def servo(self):
        return self._servo

    @servo.setter
    def servo(self, pin_servo):
        self._servo = pin_servo
        self._restar_pines_disponibles(pin_servo)

    @property
    def trigger(self):
        return self._trigger

    @trigger.setter
    def trigger(self, pin_trigger):
        self._trigger = pin_trigger
        self._restar_pines_disponibles(pin_trigger)

    @property
    def echo(self):
        return self._echo

    @echo.setter
    def echo(self, pin_echo):
        self._echo = pin_echo
        self._restar_pines_disponibles(pin_echo)

    @property
    def pines_digitales_disponibles(self):
        return self._pines_digitales_disponibles

    @property
    def pines_rpm_disponibles(self):
        return self._pines_rpm_disponibles

    def conectar(self, puerto_arduino):  # obsoleto
        self._arduino = Arduino(_BAUD_SPEED, puerto_arduino)
        self._arduino.Servos.attach(self._servo)  # TODO: por alguna razon no es dinamico este metodo

    def getDistancia(self):
        # me aseguro que los pines esten iniciados sino arrojo una exepcion
        if self._trigger is None or self._echo is None:
            raise Exception("pines no iniciados")
        if self._arduino is None:
            raise Exception("Arduino no conectado")

        #  disparo el ultrasonido
        self._disparar(self.trigger)

        # mido la duracion del pulso HIGH en el pin echo
        duracion = self._arduino.pulseIn_set(self._echo, _STATE_HIGH)  # duracion = miliseg

        distancia = duracion / 29. / 2.  # cm ( esta ecuancion no me cierra pero da la medica correcta)

        velocidad_sonido = 34400  # cm/seg
        # distancia = velocidad_sonido * duracion / 2

        """
         Este if arregla un pequeño bug
         las primeras mediciones devuelve valores negativos hasta que se estabiliza el sensor
         """
        """
        if distancia <= 0:
            distancia = self.getDistancia()
        """
        return distancia  # cm

    def mover(self, angulo):
        # me aseguro que los pines esten iniciados sino arrojo una exepcion
        if self.servo is None:
            raise Exception("pin no iniciado")
        if self._arduino is None:
            raise Exception("Arduino no conectado")

        self._arduino.Servos.write(self._servo, angulo)  # muevo el servo al angulo indicado
        posicion = self._arduino.Servos.read(self._servo)  # recupero la posicion del angulo
        # self.arduino.Servos.detach(self.servo)  # libero el servo
        return posicion

    def _digitalWrite(self, pin, state):
        self._arduino.digitalWrite(int(pin), state)

    # devuelve un intriger 1 si es verdadero y 0 si es falso
    def _digitalRead(self, pin):
        return self._arduino.digitalRead(int(pin))

    @staticmethod
    def _delay(time_seg):
        time.sleep(time_seg)

    def _disparar(self, trigger_pin):
        #  disparo el ultrasonido
        self._digitalWrite(self._trigger, _STATE_LOW)
        Sonar._delay(4e-6)  # 4 microsegundos
        self._digitalWrite(self._trigger, _STATE_HIGH)
        Sonar._delay(1e-5)  # 10 microsegundos
        self._digitalWrite(self._trigger, _STATE_LOW)

