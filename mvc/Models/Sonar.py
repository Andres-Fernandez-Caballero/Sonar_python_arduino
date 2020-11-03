# define una clase plaqueta que reperesenta el modelo de una plaqueta Arduino #

from pyfirmata import Arduino, util
import time

__STATE_LOW__ = 0
__STATE_HIGH__ = 1


class Sonar:
    def __init__(self, pin_trigger, pin_echo, pin_servo):
        self.trigger = pin_trigger
        self.echo = pin_echo
        self.servo = pin_servo
        self.arduino = None

        iterador = util.Iterator(self.arduino)
        iterador.start()

    def conectar(self, puerto_arduino):
        self.arduino = Arduino(puerto_arduino)

    def getDistancia(self):
        #  disparo el ultrasonido
        self.__digitalWrite__(self.trigger, __STATE_LOW__)
        Sonar.__delay__(0.002)  # 2000 microsegundos
        self.__digitalWrite__(self.trigger, __STATE_HIGH__)
        Sonar.__delay__(1.5e-5)  # 15 microsegundos
        self.__digitalWrite__(self.trigger, __STATE_LOW__)
        Sonar.__delay__(1e-5)  # 10 microsegundos

        #  espero el eco
        while True:
            pulso_inicio = time.time()
            if self.__digitalRead__(self.echo) == __STATE_HIGH__:
                break
        while True:
            pulso_fin = time.time()
            if self.__digitalRead__(self.echo) == __STATE_LOW__:
                break

        duracion = pulso_fin - pulso_inicio

        velocidad_sonido = 34300  # cm/seg
        distancia = velocidad_sonido * duracion / 2

        return distancia  # cm

    def mover(self, angulo):
        pin_mode = 'd:' + str(self.servo) + ':s' # en base a la documentacion pyfirmata d:digital, numero_pin, s:servo

        servo = self.arduino.get_pin(pin_mode)

        servo.write(angulo)

    def __digitalWrite__(self, pin, state):
        self.arduino.digital[int(pin)].write(state)

    def __digitalRead__(self, pin):
        return self.arduino.digital[int(pin)].read()

    @staticmethod
    def __delay__(time_seg):
        time.sleep(time_seg)