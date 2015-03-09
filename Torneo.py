# -*- encoding: utf-8 -*-
from funciones import Imprimir

__author__ = 'fredy'
import random


def Torneo(funcion_penalizada):
    tam=len(funcion_penalizada)
    for x in funcion_penalizada:
        x.append(random.randint(0,tam-1))

    #se asigno una pareja al azar para producir el torneo.
    Imprimir(funcion_penalizada)
    seleccionados=[]
    for y in funcion_penalizada:
        h=y[-1]
        funcion_penalizada[h]
        if y[-4] < funcion_penalizada[h][-4]:
            seleccionados.append(y[:-1])
        else:
            seleccionados.append(funcion_penalizada[h][:-1])
    return seleccionados