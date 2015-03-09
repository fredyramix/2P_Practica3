# -*- encoding: utf-8 -*-
__author__ = 'fredy'
import random


def Mutacion(cruz,num_cromo,n):
    cruzados=cruz[:]
    num=random.randint(0,int(num_cromo)-1)
    num_articulo=random.randint(0,len(cruzados[0])-1)
    posicion=random.randint(0,1)
    #print "num=" + str(num)
    #print "numArt=" + str(num_articulo)
    #print "pos=" + str(posicion)
    cruzados[num][num_articulo][posicion]
    if posicion==0:
        #significa que la mutacion será si elegimos o no el articulo.
        if cruzados[num][num_articulo][posicion]==1:
            cruzados[num][num_articulo][posicion]=0
        else:
           cruzados[num][num_articulo][posicion]=1
           if cruzados[num][num_articulo][1]==0:
                cruzados[num][num_articulo][1]=1
    else:
        cruzados[num][num_articulo][posicion]=random.randint(1,int(n))
        if cruzados[num][num_articulo][0]==0:
            cruzados[num][num_articulo][0]=1
    return cruzados

