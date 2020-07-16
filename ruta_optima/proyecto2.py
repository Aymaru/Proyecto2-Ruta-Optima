import cargador as mapa
import config as cons

class Nodo():
    """Una clase de nodo para A * Pathfinding"""

    def __init__(self, actual=None, padre=None):
        self.padre = padre
        self.actual = actual

        self.g = 0  #  costo de la ruta desde el NODO_INICIO hasta NODO_ACTUAL (acumulado)
        self.h = 0  #  función heurística que estima el costo de la ruta más óptima desde NODO_INICIO hasta NODO_META
        self.f = 0  #  función de evaluación

    def __eq__(self, other):
        return self.actual == other.actual

valores_heuristica = {
"Arad":366,
"Bucarest":0,
"Craiova":160,
"Dobreta":242,
"Eforie":161,
"Fagaras":176,
"Giorgiu":77,
"Hirsova":151,
"Iasi":256,
"Lugoj":244,
"Mehadia":241,
"Neamt":264,
"Oradea":380,
"Pitesti":100,
"Rimnicu Vilcea":193,
"Sibiu":253,
"Timisoara":329,
"Urziceni":80,
"Vaslui":199,
"Zerind":374 }


def main():
    camino_optimo = a_estrella(mapa.grafo_rumania,cons.NODO_INICIO,cons.NODO_META)
    print(camino_optimo)


def a_estrella(grafo,inicial,destino):
    
    nodo_inicial = Nodo(inicial)
    nodo_destino = Nodo(destino)

    lista_abiertos = []
    lista_cerrados = []

    # Agregar nodo inicial
    lista_abiertos.append(nodo_inicial)

    # Recorrer hasta encontrar el objetivo.
    while len(lista_abiertos) > 0:

        # Se obtiene el nodo actual
        nodo_actual = lista_abiertos[0]
        indice_actual = 0
        for index, item in enumerate(lista_abiertos):
            if item.f < nodo_actual.f:
                nodo_actual = item
                indice_actual = index
    
        # Se saca el actual de la lista de abiertos y se agrega a la lista de cerrados
        lista_abiertos.pop(indice_actual)
        lista_cerrados.append(nodo_actual)
        print("procesando nodo actual")
        # Se verifica si se llego al destino
        if nodo_actual == nodo_destino:
            camino = []
            actual = nodo_actual
            while actual is not None: 
                camino.append(actual.actual) # Escribe los nodos que recorrio para llegar al destino
                actual = actual.padre
            return camino[::-1] # Devuelve el camino al reves

        # Generar hijos
        lista_hijos = []
        for vecino in list(grafo.adj[nodo_actual.actual]):
            hijo = Nodo(vecino,nodo_actual)
            lista_hijos.append(hijo)

        # Recorre los hijos
        for hijo in lista_hijos:
            
            for nodo_cerrado in lista_cerrados:
                if hijo == nodo_cerrado:
                    continue
            
            hijo.g = nodo_actual.g + grafo.adj[nodo_actual.actual][hijo.actual]["distancia"]#calculamos g
            hijo.h = valores_heuristica[nodo_actual.actual]#calculamos h
            hijo.f = hijo.g + hijo.h#calculamos f

            for nodo_abierto in lista_abiertos:
                if hijo == nodo_abierto and hijo.g > nodo_abierto.g:
                    continue
            
            lista_abiertos.append(hijo)

if __name__ == '__main__':
    main()

