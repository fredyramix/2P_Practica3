# -*- encoding: utf-8 -*-
__author__ = 'fredy'
from funciones import *
from Evaluar import *
from Penalizar import *
def main():
    tabla=LeerArticulos() #obtener la tabla de articulos
    #all contiene la forma: {1:[3,4,5]} donde 1 es su llave o numero de articulo 3 es su peso, 4 su importancia y 5 la cantidad.
    print tabla
    #Definir primera generacion aleatoria donde tomaremos el numero maximo de la cantidad de productos para que sea
    #nuestro tamaño del cromosoma
    num_cromo=raw_input("Introduzca el numero de cromosomas:\n")
    peso_max=raw_input("Ingrese el peso maximo de la caja:\n")
    primera=PrimeraGeneracionAleatoria(tabla,num_cromo)
    Imprimir(primera)
    num_gen=raw_input("Ingrese el numero de generaciones:\n")
    c=1
    print "Comienza algoritmo genetico esto puede llevar algunos minutos por favor espere..."
    while c!=num_gen:
        #comienza ciclo.
        #Evaluar funcion de x
        funcion_evaluada=EvaluarFX(primera,tabla)
        #Cromosoma = [ (1,3), (0,0) , (8,9).....n , peso , importancia ] ya multiplicando el peso y la importancia por el numero de existencias

        #Siguiente paso Penalizar !

        funcion_penalizada=Penalizar(funcion_evaluada,tabla,peso_max)

        for x in funcion_penalizada:
            print x

        raw_input("Esperad")

        c=c+1
    print "finalizado"


main()