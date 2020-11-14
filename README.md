
# TP_N3_Sonar_python_arduino

![logo python](https://anthoncode.com/wp-content/uploads/2019/01/python-logo-png.png)

## Requisitos
* una plaqueta Arduino Uno (por ahora solo funciona con este modelo)
* una computadora con puerto usb
* cable conector usb tipo A/B (el de las impresoras) 
* un sensor de ultrasonido modelo hc-sr04
* un servo motor, cualquier modelo y potencia, se recomienda uno de poco torque ya que solo sostendra al sensor de ultrasonido
Este proyecto pretende controlar un arduino a travez del protocolo "Firmdata" con un script python para poder crear un sonar. Echo con un servomotor y un sensor de distancia conectados a la placa arduino Uno.
* el editor de codigo de su preferencia, yo utilize Pycharm de jetbrains https://www.jetbrains.com/es-es/pycharm/

## Instalacion
Para poder implementar este proyecto debe sergir las siguientes instrucciones

### Instalacion entorno Arduino y carga del sketch StandardFirmata
1. descargue e instale el entorno de desarrollo arduino de https://www.arduino.cc/en/software
2. abra el programa.
3. valla a archivo -> ejemplos -> firmata -> StandardFirmata, se abrira una nueva ventana con un programa ya cargado, este le permitira comunicar su computadora con el arduiono a travez del protocolo firmata.
![libreria firmata](http://echidna.es/wp-content/uploads/2020/10/BuscarStandarfirmata-600x586.png)
4. En la ventana nueva valla a la pestaña herramientas -> placa -> arduino uno
![placa arduino uno](http://echidna.es/wp-content/uploads/2020/10/SeleccionarPlaca.png)
5. conecte la plaqueta arduino uno a la computadora con el cable de impresora
6. En la ventana nueva ventana valla a herramientas -> puerto y seleccione el puerto al que esta conectada su plaqueta Arduino uno
![puerto](http://echidna.es/wp-content/uploads/2020/10/SeleccionarPuerto.png)
7. finalmente oprima subri sketch (el programa arduino).
![subir programa](http://echidna.es/wp-content/uploads/2020/10/Captura-de-pantalla-2020-10-02-a-las-10.01.37.png)
8. espere a que el programa se cargue en la plaqueta arduino uno, vera un mensaje de exito en la parte inferior de la pantalla.

### Instalacion de Python
1. descargue e instale python  para su sistema operativo desde la pagina oficial https://www.python.org/downloads/ asegurese que agrege la ruta PATH en el instalador
![path python](https://datatofish.com/wp-content/uploads/2018/10/0001_add_Python_to_Path.png)

### Instalacion de git Bash
el terminal git bash viene incluido en el paquete git asegurese que este activa la ruta path en el instalador
![git bash](![path python](https://datatofish.com/wp-content/uploads/2018/10/0001_add_Python_to_Path.png))
asignar variable de entorno
![global path](https://miro.medium.com/max/495/1*dY-zXW1E8HEYQp5ADIp-IQ.png)

### descarga y uso del proyecto en cuestion
1. si tiene instalado puede git puede clonar el repositorio con el comando `git clone https://github.com/Andres-Fernandez-Caballero/TP_N3_Sonar_python_arduino.git` o descargando el proyecto desde el repositorio https://github.com/Andres-Fernandez-Caballero/TP_N3_Sonar_python_arduino y descomprimiendo el archivo zip.
2. abra un terminal de linea de comandos (recomiendo git bash, el terminal de windows suele dar error)dentro de la raiz del proyecto descargado utilizando el atajo
3. dentro del terminal ingrese el siguiente codigo `source venv/Scripts/activate` esto activara el entorno virtual, para desactivarlo dentro del terminal ingrese el siguiente comando `deactivate` 
 4. conecte el sensor de ultrasonido de la siguiente manera vcc a 5v corriente continua, gnd a negativo, el pin trigger a uno de los 13 pines digitales enumerados en la plaqueta arduino uno, el pin echo a un pin digital distinto al del pin trigger
 5. conecte el servo motor de la siguiente manera vcc (cable rojo generalmente) a 5v, gnd (cable negro generalmente) a negativo, señal( cable blanco o amarillo, el que queda...) a uno de los pines pwm del arduino uno, estos pines estan identificados con el dibujo de una onda al lado del numero de pin digital.
6. ejecute en el terminal el comando `python main.py` y siga las instrucciones del terminal, el resultado sera que el servomotor ira de 0 a 180 grados y cada 5 grados dara una distancia dependiedo de los obstaculos encontrados.
 
####fuentes:
imagenes de instalacion arduino
http://echidna.es/a-programar/instalar-standardfirmata/

imagenes de instalacion git bash
https://medium.com/laboratoria-how-to/c%C3%B3mo-instalar-git-368c78187b51` y el programa ejetutara una rutina de pruena, que es hasta donde se llego con esta entrega
