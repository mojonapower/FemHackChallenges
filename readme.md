# Desafío Computerwoman HackHoman Hackathon

## Descripción del Desafío

Imagina que eres Jean Jennings Bartik y tienes una buena computadora. Desea una manera fácil de enviar la información sobre esas trayectorias balísticas y cómo calcularlas lo más rápido posible con una CLI simple.

Entonces, su tarea sería diseñar la siguiente CLI (interfaz de línea de comandos) que permita a sus compañeros hacer lo siguiente:

Introduce los siguientes datos:
Velocidad inicial (v0)
Ángulo de lanzamiento (alfa)
Preguntar si los resultados quieren guardarse en un archivo
Seleccione la forma de introducir los datos (JSON o Manual)
Calcular la altura máxima del proyectil (h_max)
h_max = ( v0 * v0 ) / ( 2 * g ) 

Calcular la distancia máxima recorrida
x_max = 2 * v0 * sin(alfa) / g

Guarde los datos calculados (Entradas + Resultados) en un archivo

## Instalación

⚠️ Importante: el proyecto está realizado con python 3.8 pero de ser el caso, puedes cambiar facilmente `python_version` en el archivo pipfile

Por favor, asegurarse  de que tienes `python 3+` instalado dentro de tu sistema, luego ejecute los siguientes comandos:
```sh
$ pipenv install (instalar pip packages)
$ pipenv run cli (ejecutar cli )
$ pipenv run test (ejecutar test unitarios)
```

## Ejemplo de Ejecución
En la raiz del proyecto hay un archivo llamado `entrada.json.example` que contiene la estructura que debe tener el archivo de entrada para poder ser leído por el programa.

La entrada es un Json array que permite ingresar desde 1 a n elementos posibles
```
[{"v0":15, "alpha":53}]
```
Para que el archivo de lectura sea efectivamente detectado debe encontrarse dentro de la carpeta entrada

### Ejecutar proyecto
Para ejecutar el script por favor segurarse que tiene su entorno virtual activado
```sh
$ pipenv shell
$ pipenv run cli 
```
Durante la ejecución le preguntará si desea ingresar la información de forma manual o mediante la lectura de archivo Json.

```sh
'Los datos serán ingresados manualmente o mendiante la lectura json?
 Para responder escribe "manual" o "json"'
```

a) En el primer caso, le solicirtará ingresar datos sales como la velocidad inicial y el ángulo de inclinación en el que fue lanzado el proyectil. Debe ingresar los datos considerando que las unidades de medidas consideradas son m/s y ángulo en grados respectivamente 

b) Por otro lado, si selecciona la segunda opción, deberá indicar el nombre del archivo a leer. Para factores de prueba se encuentra un archivo llamado entrada.json

Posteriormente se realizará la entrega de los resultados

```sh
2022-01-22 19:39:03.690336 
Resumen:
        valores iniciales:

        velocidad de lanzamiento: 15
        angulo de lanzamiento: 53

        Formato de entrada : json

        Resultados obtenidos:
        Velocidad de lanzamiento en X9.027225347280726
        Velocidad de lanzamiento en Y11.979532650709393
        Altura máxima alcanzada h_max7.321898088235327
        Distancia recorrida x_max 22.026429847364973
        Tiempo transcurrido t 1.2224012908887134

```
Además le preguntará si acaso desea realizar una simulación del lanzamiento del proyectil (implementado con Vpython). En caso de ser afirmativa su respuesta se levantará un servidor en localhost:PORT (puerto variable)

## Registro de resultados

Todos los resultados se encuentran disponibles en la carpeta Salida en un archivo llamado output.txt

Adicionalmente, en la carpeta log se encuentra un archivo llamado registro.log en donde se encuentra la traza completa de la ejecución del script.











