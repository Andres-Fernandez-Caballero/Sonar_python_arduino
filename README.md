# TP_N3_Sonar_python_arduino
Este proyecto pretende controlar un arduino a travez del protocolo "Firmdata" con un script python para poder crear un sonar. Echo con un servomotor y un sensor de distancia conectados a la placa arduino Uno.

![logo python](https://anthoncode.com/wp-content/uploads/2019/01/python-logo-png.png)

## Instalacion
Para poder implementar este proyecto debe sergir las siguientes instrucciones
1. si tiene instalado puede git puede clonar el repositorio con el comando `git clone https://github.com/Andres-Fernandez-Caballero/TP_N3_Sonar_python_arduino.git` o descargando el proyecto desde el repositorio https://github.com/Andres-Fernandez-Caballero/TP_N3_Sonar_python_arduino y descomprimiendo el archivo zip.
2. abra un terminal de linea de comandos dentro de la raiz del proyecto descargado
3. dentro del terminal ingrese el siguiente codigo `source venv/Scripts/activate` esto activara el entorno virtual, para desactivarlo dentro del terminal ingrese el siguiente comando `deactivate` 
 4. conecte el sensor de ultrasonido de la siguiente manera vcc a 5v corriente continua, gnd a negativo, el pin trigger a uno de los 13 pines digitales enumerados en la plaqueta arduino uno, el pin echo a un pin digital distinto al del pin trigger
 5. conecte el servo motor de la siguiente manera vcc (cable rojo generalmente) a 5v, gnd (cable negro generalmente) a negativo, señal( cable blanco o amarillo, el que queda...) a uno de los pines pwm del arduino uno, estos pines estan identificados con el dibujo de una onda al lado del numero de pin digital.
 
 ### instrucciones para version v_alfa_0.1
 1. en la raiz del proyecto abra el archivo main.py
 2. modifique la linea  `18        sonar = Sonar(3, 4, 5)` e ingrese los numeros de pines conectados a la plaqueta arduino en el siguiente orden pin trigger, pin echo pin servo
 3. guarde los cambios
 4. en el terminal ingrese la siguiente orden `python main.py` y el programa ejetutara una rutina de pruena, que es hasta donde se llego con esta entrega
