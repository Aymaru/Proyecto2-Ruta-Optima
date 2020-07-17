#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Nodo():
    """Una clase de nodo para A* ruta optima"""

    def __init__(self, actual=None, padre=None):
        self.padre = padre
        self.actual = actual
        self.g = 0  #  costo de la ruta desde el NODO_INICIO hasta NODO_ACTUAL (acumulado)
        self.h = 0  #  función heurística que estima el costo de la ruta más óptima desde NODO_INICIO hasta NODO_META  
        self.f = 0  #  función de evaluación

    def __eq__(self, other):
        return self.actual == other.actual