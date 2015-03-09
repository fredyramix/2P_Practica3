# -*- encoding: utf-8 -*-
__author__ = 'fredy'


def SeleccionMejor(seleccionados,best666):
    seleccionados.sort(key=lambda x: x[-1])

    if len(best666)==0:
        best=seleccionados[0][:]
        return best[:]
    else:
        if seleccionados[0][-1] < best666[-1]:
            best666=seleccionados[0][:]
            return best666[:]
        else:
            return best666[:]