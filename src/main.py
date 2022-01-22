#!/usr/bin/env python
import sys,os, json, logging
from datetime import datetime
from modules import calc, draw



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('log/registro.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

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
            logger.debug(f"OS error {err}")
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

def get_result(entry, answer):
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
        "t":T
        })

        now = str(datetime.now())
        resumen =f"""{now} Resumen:
                valores iniciales:

                velocidad de lanzamiento: {v0}
                angulo de lanzamiento: {alpha}

                Formato de entrada : {answer}

                Resultados obtenidos:
                Velocidad de lanzamiento en X{X}
                Velocidad de lanzamiento en Y{Y}
                Altura máxima alcanzada h_max{H}
                Distancia recorrida x_max {D} 
                Tiempo transcurrido t {T}\n\n\n """
        logger.debug(resumen)
        print(resumen)
        return results

def menu():
    
    while True:
        entry=[{}]
        answer = input("¿Los datos serán ingresados manualmente o mendiante la lectura json?\n PAra responder escribe 'manual' o 'json'")
        
        if(answer.lower()=='json'):
            entry = list(readJsonFile())
            print("Calculando cantidad de proyectiles ...", len(entry))
            
            return get_result(entry, answer)
            

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
            return get_result(entry, answer)
        else:
            print("no logro procesar, intente nuevamente")
    

    
    


if __name__ == "__main__":
    f = open("salida/output.txt","a")
    resultados= menu()
    f.write('\n'+str(resultados))
    f.close()
    print("Toda la información ha sido almacenada en salida/output.txt \n El log de la aplicación se encuentra en registro.log")
    simulacion=input("¿Desea visualizar lanzamiento de proyectil de forma grafica?\n Escriba si / no\n")
    if(simulacion.lower()=='si'):
        print("Ejecutando... por favor, cierre la ventana al terminar \n")
        #ejemplo parametros(velocidad en x, velocidad en y, tiempo recorrido, distancia total)
        
        #print(type(resultados[0]['vx']),resultados[0]['vy'],resultados[0]['t'],resultados[0]['x_max'])
        
        vx = float(resultados[0]['vx'])
        vy = float(resultados[0]['vy'])
        t = float(resultados[0]['t'])
        x_max =float(resultados[0]['x_max'])
        alpha = float(resultados[0]['alpha'])

        draw.simulacion(vx,vy, alpha,t)
        sys.exit() 
    elif(simulacion.lower()=='no'):
        print("ok ... \n")
        sys.exit()              
    else:
        print("valor inesperado, se cierra el programa \n")
        sys.exit()
    
    

