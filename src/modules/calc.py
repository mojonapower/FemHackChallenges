#!/usr/bin/env python
import math, logging
from datetime import datetime


now = str(datetime.now())

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('log/registro.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)



#conversión de unidades de medida
def kmH_to_MS(kmh):
    logger.debug(f"{now} convirtiendo de Kilómetros por Hora a Metros por Segundo")
    mph = 0.277778 * kmh
    logger.debug(f"resultado obtenido {mph}")
    return mph
def Km_to_M(km):
    logger.debug(f"{now} convirtiendo de Kilómetros a Metros")
    m = km * 1000
    logger.debug(f"resultado obtenido {m}")
    return m

def rad_to_grados(radianes):
    logger.debug(f"{now} convirtiendo de radianes a grados")
    grados = radianes * (180/math.pi)
    logger.debug(f"resultado obtenido {grados}")

    return grados

def grados_to_rad(grados):
    logger.debug(f"{now} convirtiendo de radianes a grados")
    radianes = grados * (math.pi/180)
    logger.debug(f"resultado obtenido {radianes}")

    return radianes

def velocidadY(v0,alfa):
    logger.debug(f"{now} calculando velocidad del proyectil en el Eje Y")
    alfa = grados_to_rad(alfa) #transformando valores para calculo
    result = v0 * math.sin(alfa) 
    logger.debug(f"resultado obtenido {result}")
    return result

def velocidadX(v0,alfa):
    logger.debug(f"{now} calculando velocidad del proyectil en el Eje X")
    alfa = grados_to_rad(alfa) #transformando valores para calculo
    result = v0 * math.cos(alfa) 
    logger.debug(f"resultado obtenido {result}")

    return result

def hmax(v0y,g):
    logger.debug(f"{now} calculando altura maxima alcanzada, considerando la aceleración de gravedad como 9.8")
    #ecuacion vfy^2 = v0y^2+2g*HMAX
    # 0 =v0y^2+ 2(-9.8) () G negativo
    #0=v0y^2 - 19.6*HMAX
    #19.6hmax= v0y
    #hmax= v0y/19.6
    v0y = math.pow(v0y,2)
    hmax= v0y/(2*g)
    logger.debug(f"resultado obtenido {hmax}")

    return hmax

def tiempoLanzamiento(v0y,g):
    #ecuacion vy=v0y-gT
    # 0=v0y-9.8T
    #9.8T= v0y
    #v0y/9.8=t
    logger.debug(f"{now} calculando tiempo que tardó en lanzarse el proyectil")
    tiempo =v0y/g
    logger.debug(f"resultado obtenido {tiempo}")

    return tiempo

def xmax(v0x,t):
    logger.debug(f"{now} calculando distancia que recorrió proyectil ")
    #ecuacion x=vx*2t
    xmax =v0x*(2.44)
    logger.debug(f"resultado obtenido {xmax}")
    return(xmax)














