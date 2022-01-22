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
👷‍♀️ En construcción 💪