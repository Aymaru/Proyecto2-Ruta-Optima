import networkx as nx

Grafo = nx.Graph() #Crear el nuevo grafo

#Agregar los nodos del grafo
Grafo.add_node("Arad")      
Grafo.add_node("Bucarest")
Grafo.add_node("Craiova")
Grafo.add_node("Dobreta")
Grafo.add_node("Eforie")
Grafo.add_node("Fagaras")
Grafo.add_node("Giorgiu")
Grafo.add_node("Hirsova")
Grafo.add_node("Iasi")
Grafo.add_node("Lugoj")
Grafo.add_node("Mehadia")
Grafo.add_node("Neamt")
Grafo.add_node("Oradea")
Grafo.add_node("Pitesti")
Grafo.add_node("Rimnicu Vilcea")
Grafo.add_node("Sibiu")
Grafo.add_node("Timisoara")
Grafo.add_node("Urziceni")
Grafo.add_node("Vaslui")
Grafo.add_node("Zerind")

#Agregar las aristas del grafo.
#aristas de Arad
Grafo.add_edge("Arad","Zerind",distancia=75,estado_de_carretera=6,peligrosidad=5)
Grafo.add_edge("Arad","Sibiu",distancia=99,estado_de_carretera=7,peligrosidad=2)
Grafo.add_edge("Arad","Timisoara",distancia=118,estado_de_carretera=5,peligrosidad=3)
#aristas de Bucarest
Grafo.add_edge("Bucarest","Fagaras",distancia=211,estado_de_carretera=7,peligrosidad=2)
Grafo.add_edge("Bucarest","Urziceni",distancia=85,estado_de_carretera=9,peligrosidad=2)
Grafo.add_edge("Bucarest","Giorgiu",distancia=90,estado_de_carretera=8,peligrosidad=1)
Grafo.add_edge("Bucarest","Pitesti",distancia=101,estado_de_carretera=8,peligrosidad=1)

#aristas de Craiova 3
Grafo.add_edge("Craiova","Rimnicu Vilcea",distancia=146,estado_de_carretera=8,peligrosidad=1)
Grafo.add_edge("Craiova","Pitesti",distancia=138,estado_de_carretera=6,peligrosidad=4)
Grafo.add_edge("Craiova","Dobreta",distancia=120,estado_de_carretera=7,peligrosidad=3)

#aristas de Dobreta 2
Grafo.add_edge("Dobreta","Mehadia",distancia=75,estado_de_carretera=4,peligrosidad=3)

#aristas de Eforie 1
Grafo.add_edge("Eforie","Hirsova",distancia=86,estado_de_carretera=7,peligrosidad=3)

#aristas de Fagaras 2
Grafo.add_edge("Fagaras","Sibiu",distancia=99,estado_de_carretera=7,peligrosidad=2)

#aristas de Hirsova 
Grafo.add_edge("Hirsova","Urziceni",distancia=98,estado_de_carretera=7,peligrosidad=4)

#aristas de Iasi
Grafo.add_edge("Iasi","Neamt",distancia=87,estado_de_carretera=5,peligrosidad=3)
Grafo.add_edge("Iasi","Vaslui",distancia=92,estado_de_carretera=7,peligrosidad=4)

#aristas de Lugoj
Grafo.add_edge("Lugoj","Timisoara",distancia=111,estado_de_carretera=6,peligrosidad=3)
Grafo.add_edge("Lugoj","Mehadia",distancia=70,estado_de_carretera=4,peligrosidad=4)

#aristas de Oradea
Grafo.add_edge("Oradea","Zerind",distancia=71,estado_de_carretera=6,peligrosidad=4)
Grafo.add_edge("Oradea","Sibiu",distancia=151,estado_de_carretera=6,peligrosidad=3)

#aristas de Pitesti
Grafo.add_edge("Pitesti","Rimnicu Vilcea",distancia=97,estado_de_carretera=7,peligrosidad=2)

#aristas de Rimnicu Vilcea
Grafo.add_edge("Rimnicu Vilcea","Sibiu",distancia=80,estado_de_carretera=6,peligrosidad=2)

#aristas de Urziceni
Grafo.add_edge("Urziceni","Vaslui",distancia=142,estado_de_carretera=5,peligrosidad=2)


print(Grafo.number_of_nodes()) #20
print(Grafo.number_of_edges()) #23
