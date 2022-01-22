#!/usr/bin/env python
import math

#conversión de unidades de medida
def kmH_to_MS(kmh):
    print("convirtiendo de Kilómetros por Hora a Metros por Segundo")
    mph = 0.277778 * kmh
    return mph
def Km_to_M(km):
    print("convirtiendo de Kilómetros a Metros")
    m = km * 1000
    return m

def rad_to_grados(radianes):
    print("convirtiendo de radianes a grados")
    grados = radianes * (180/math.pi)
    return grados

def grados_to_rad(grados):
    print("convirtiendo de radianes a grados")
    radianes = grados * (math.pi/180)
    return radianes

def velocidadY(v0,alfa):
    print("calculando velocidad del proyectil en el Eje Y")
    alfa = grados_to_rad(alfa) #transformando valores para calculo
    result = v0 * math.sin(alfa) 
    return result

def velocidadX(v0,alfa):
    print("calculando velocidad del proyectil en el Eje X")
    alfa = grados_to_rad(alfa) #transformando valores para calculo
    result = v0 * math.cos(alfa) 
    return result

def hmax(v0y,g):
    print("calculando altura maxima alcanzada, considerando la aceleración de gravedad como 9.8")
    #ecuacion vfy^2 = v0y^2+2g*HMAX
    # 0 =v0y^2+ 2(-9.8) () G negativo
    #0=v0y^2 - 19.6*HMAX
    #19.6hmax= v0y
    #hmax= v0y/19.6
    v0y = math.pow(v0y,2)
    hmax= v0y/(2*g)
    return hmax

def tiempoLanzamiento(v0y,g):
    #ecuacion vy=v0y-gT
    # 0=v0y-9.8T
    #9.8T= v0y
    #v0y/9.8=t
    print("calculando tiempo que tardó en lanzarse el proyectil")
    tiempo =v0y/g
    return tiempo

def xmax(v0x,t):
    #ecuacion x=vx*2t
    print("calculando distancia recorrida de proyectil")
    xmax =v0x*(2.44)
    return(xmax)














