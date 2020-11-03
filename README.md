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
