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





if __name__ == "__main__":
    entry=[{}]
    answer = input("¿Los datos serán ingresados manualmente o mendiante la lectura json?\n PAra responder escribe 'manual' o 'json'")
    
    if(answer.lower()=='json'):
        entry = list(readJsonFile())

    elif(answer.lower()=='manual'):
        while True:
            
            print("El ingreso manual solamente implica el cálculo del lanzamiento de un proyectil, de lo contrario, recomiendo el ingreso de información mediante archivo json")
            try:
                v = float(input("Ingrese la velocidad en m/s"))
                a = float(input("Ingrese el angulo de lanzamiento en grados ° "))
                entry[0]['v0']=v
                entry[0]['alpha']=a
                print(f"datos entregados {entry}")
                break
            except ValueError:
                print("Oops! alguno de los datos ingresados no cumple con el formato esperado,  intente nuevamente")


    print("Calculando cantidad de proyectiles ...", len(entry))
    results = []
    for i in entry:
        #velocidad en ejes X e Y
        v0 = i['v0']
        alpha =i['alpha']
        Y = calc.velocidadY(v0, alpha)
        X = calc.velocidadX(v0, alpha)
        #tiempo en recorrer trayectoria
        T = calc.tiempoLanzamiento(Y,9.8)
        #altura maxima
        H = calc.hmax(Y,9.8)
        #distancia recorrida
        D = calc.xmax(X,T)
        
        results.append({"v0":v0,
        "alpha": alpha,
        "vx":X,
        "vy":Y,
        "h_max":H,
        "x_max":X,
        })

        '''
        print(f"""Resultados obtenidos:
        velocidad de lanzamiento: {v0}
        angulo de lanzamiento: {alpha}
        Velocidad de lanzamiento en X{X}
        Velocidad de lanzamiento en Y{Y}
        Altura máxima alcanzada h_max{H}
        Distancia recorrida x_max {D} """)
        '''
    print(results)
    

