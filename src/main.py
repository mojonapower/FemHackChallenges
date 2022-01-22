#!/usr/bin/env python
import sys
import os

def readJsonFile():
    while(True):
        try:
            ruta='entrada/'
            file=input('Por favor ingrese el nombre del archivo de entrada a utilizar, recuerde indicar la extension del archivo')
            f=open(ruta+file)
            body = f.readline()
            print("contenido de archivo encontrado \n", body)
            answer = input("Es correcto el cuerpo del archivo? Escriba si / no ")
            print(answer)
            if(answer.lower()=='si'):
                print("Perfecto")
                break
            if(answer.lower()=='no'):
                print("analizaremos nuevamente ...")
                    
            if(answer.lower() != 'si' or answer.lower() != 'no'):
                print("valor inesperado, intentelo nuevamente")
            

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
    readJsonFile()

