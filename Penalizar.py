# -*- encoding: utf-8 -*-
__author__ = 'fredy'


def Penalizar(funcion_evaluada,tabla,peso_max):
    for x in funcion_evaluada:
        count=1
        pena=0
        if x[-2]>int(peso_max):
            #Se paso de peso maximo
            pena=-1000
        for y in x:
            try:
                if y[0]==1:
                    max=y[1]
                    existencia = tabla[count][2]
                    if max>existencia:
                        #Se pasa del numero de existencias por lo tanto debe ser penalizado.
                        pena=pena-1000
            except TypeError,e:
                pass #termino de recorrer el cromosoma y encntro el costo o la importancia
                pena=pena+0
            count=count+1
        x.append(pena+x[-1])
    return funcion_evaluada