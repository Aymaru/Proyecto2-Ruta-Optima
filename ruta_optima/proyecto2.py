import cargador as mapa
import config as cons

class Nodo():
    """Una clase de nodo para A * Pathfinding"""

    def __init__(self, padre=None, posicion=None):
        self.padre = padre
        self.posicion = posicion

        self.g = 0  #  costo de la ruta desde el NODO_INICIO hasta NODO_ACTUAL (acumulado)
        self.h = 0  #  función heurística que estima el costo de la ruta más óptima desde NODO_INICIO hasta NODO_META
        self.f = 0  #  función de evaluación

    def __eq__(self, other):
        return self.posicion == other.posicion

def pathfinder(grafo,nodo_inicio,nodo_meta):

    

    print("Hello World")

def main():
    camino_optimo = pathfinder(mapa.grafo_rumania,cons.NODO_INICIO,cons.NODO_META)
    print(camino_optimo)

if __name__ == '__main__':
    main()
