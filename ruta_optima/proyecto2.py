import cargador as cargador
import config as cons
import nodo as n

def calcular_indicador(actual,maximo,minimo):
    return (actual-minimo) / (maximo-minimo)

def IP(actual): ##Calcula el indicador de peligrosidad
    return calcular_indicador(actual,cons.PELIGROSIDAD_MIN,cons.PELIGROSIDAD_MAX)
    
def IEC(actual): ##Calcula el indicador de estado de la carretera
    return calcular_indicador(actual,cons.ESTADO_CARRETA_MAX,cons.ESTADO_CARRETA_MIN)

def ID(actual): ##Calcula el indicador de Distancia
    return calcular_indicador(actual,cons.DISTANCIA_LINEAL_MAX,cons.DISTANCIA_LINEAL_MIN)

def calcular_costo(grafo,actual,siguiente):
    CID = ID(grafo[actual][siguiente]["distancia"])
    CIEC = IEC(grafo[actual][siguiente]["estado_de_carretera"])
    CIP = IP(grafo[actual][siguiente]["peligrosidad"])
    return cons.PESO_ID * CID + cons.PESO_IEC * CIEC + cons.PESO_IP * CIP

def calcular_heuristica(actual):
    CID = ID(cons.VALORES_HEURISTICA[actual])
    CIEC = IEC(cons.ESTADO_CARRETA_MAX)
    CIP = IP(cons.PELIGROSIDAD_MIN)
    return cons.PESO_ID * CID + cons.PESO_IEC * CIEC + cons.PESO_IP * CIP

def a_estrella(grafo,inicial,destino):
    
    nodo_inicial = n.Nodo(inicial)
    nodo_destino = n.Nodo(destino)

    lista_abiertos = []  # nodos por evaluar
    lista_cerrados = []  # nodos ya evaluados

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
            hijo = n.Nodo(vecino,nodo_actual)
            lista_hijos.append(hijo)

        # Recorre los hijos
        for hijo in lista_hijos:
            
            for nodo_cerrado in lista_cerrados:
                if hijo == nodo_cerrado:
                    continue
            
            hijo.g = nodo_actual.g + calcular_costo(grafo,nodo_actual.actual,hijo.actual)
            hijo.h = calcular_heuristica(hijo.actual)
            hijo.f = hijo.g + hijo.h

            for nodo_abierto in lista_abiertos:
                if hijo == nodo_abierto and hijo.g > nodo_abierto.g:
                    continue
            
            lista_abiertos.append(hijo)

def main():
    camino_optimo = a_estrella(cargador.grafo_rumania,cons.NODO_INICIO,cons.NODO_META)
    print(camino_optimo)

if __name__ == '__main__':
    main()

