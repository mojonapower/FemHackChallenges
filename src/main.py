#!/usr/bin/env python
import sys
import os
import json
from modules import calc

def readJsonFile():
    while(True):
        try:
            ruta='entrada/'
            file=input('Por favor ingrese el nombre del archivo de entrada a utilizar, recuerde indicar la extension del archivo \n')
            f=open(ruta+file)
            body = json.load(f)
            print("contenido de archivo encontrado \n", body)
            answer = input("Es correcto el cuerpo del archivo? Escriba si / no  \n")
            print(answer)
            if(answer.lower()=='si'):
                print("Perfecto \n")
                return(body)
            if(answer.lower()=='no'):
                print("analizaremos nuevamente ... \n")
                    
            if(answer.lower() != 'si' or answer.lower() != 'no'):
                print("valor inesperado, intentelo nuevamente \n")
            #crear validaciones si estructura de JSON no es compatible :D
            

        #manejo de excepciones iniciales
        except OSError as err:
            print("OS error: {0}".format(err))
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise
        except NameError(dato):
            print('An exception flew by!, you entered',dato, "but it's not expected" )
            raise



def menu():
    entry = list(readJsonFile())
    print("Calculando cantidad de proyectiles ...", len(entry))
    """ 
    Para realizar el cálculo primero definiremos el orden
    variables disponibles:
        - angulo de lanzamiento
        - velocidad inicial
    Se requiere conseguir:
        - altura máxima alcanzada del proyectil
        - distancia máxima recorrida
    
    Para ello, conseguiremos inicialmente la velocidad en cada uno de los ejes implicados
    velocidad en eje X e Y, luego para efectos de calcular la distancia máxima recorrida, 
    conseguiremos el tiempo y finalmente calcularemos la altura y distancia recorrida

    """
    for i in entry:
        #velocidad en ejes X e Y
        v0 = i['v0']
        alfa =i['alfa']
        Y = calc.velocidadY(v0, alfa)
        X = calc.velocidadX(v0, alfa)
        #tiempo en recorrer trayectoria
        T = calc.tiempoLanzamiento(Y,9.8)
        #altura maxima
        H = calc.hmax(Y,9.8)
        #distancia recorrida
        D = calc.xmax(X,T)
        print(f"""Resultados obtenidos:
        velocidad de lanzamiento: {v0}
        angulo de lanzamiento: {alfa}
        Velocidad de lanzamiento en X{X}
        Velocidad de lanzamiento en Y{Y}
        Altura máxima alcanzada h_max{H}
        Distancia recorrida x_max {D} """)


if __name__ == "__main__":
    menu()
    

