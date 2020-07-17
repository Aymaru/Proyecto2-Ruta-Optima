import networkx as nx

grafo_rumania = nx.Graph() 

#Agregar los nodos del grafo
grafo_rumania.add_node("Arad")      
grafo_rumania.add_node("Bucarest")
grafo_rumania.add_node("Craiova")
grafo_rumania.add_node("Dobreta")
grafo_rumania.add_node("Eforie")
grafo_rumania.add_node("Fagaras")
grafo_rumania.add_node("Giorgiu")
grafo_rumania.add_node("Hirsova")
grafo_rumania.add_node("Iasi")
grafo_rumania.add_node("Lugoj")
grafo_rumania.add_node("Mehadia")
grafo_rumania.add_node("Neamt")
grafo_rumania.add_node("Oradea")
grafo_rumania.add_node("Pitesti")
grafo_rumania.add_node("Rimnicu Vilcea")
grafo_rumania.add_node("Sibiu")
grafo_rumania.add_node("Timisoara")
grafo_rumania.add_node("Urziceni")
grafo_rumania.add_node("Vaslui")
grafo_rumania.add_node("Zerind")

#Agregar las aristas del grafo.
#aristas de Arad
grafo_rumania.add_edge("Arad","Zerind",distancia=75,estado_de_carretera=6,peligrosidad=5)
grafo_rumania.add_edge("Arad","Sibiu",distancia=99,estado_de_carretera=7,peligrosidad=2)
grafo_rumania.add_edge("Arad","Timisoara",distancia=118,estado_de_carretera=5,peligrosidad=3)

#aristas de Bucarest
grafo_rumania.add_edge("Bucarest","Fagaras",distancia=211,estado_de_carretera=7,peligrosidad=2)
grafo_rumania.add_edge("Bucarest","Urziceni",distancia=85,estado_de_carretera=9,peligrosidad=2)
grafo_rumania.add_edge("Bucarest","Giorgiu",distancia=90,estado_de_carretera=8,peligrosidad=1)
grafo_rumania.add_edge("Bucarest","Pitesti",distancia=101,estado_de_carretera=8,peligrosidad=1)

#aristas de Craiova 3
grafo_rumania.add_edge("Craiova","Rimnicu Vilcea",distancia=146,estado_de_carretera=8,peligrosidad=1)
grafo_rumania.add_edge("Craiova","Pitesti",distancia=138,estado_de_carretera=6,peligrosidad=4)
grafo_rumania.add_edge("Craiova","Dobreta",distancia=120,estado_de_carretera=7,peligrosidad=3)

#aristas de Dobreta 2
grafo_rumania.add_edge("Dobreta","Mehadia",distancia=75,estado_de_carretera=4,peligrosidad=3)

#aristas de Eforie 1
grafo_rumania.add_edge("Eforie","Hirsova",distancia=86,estado_de_carretera=7,peligrosidad=3)

#aristas de Fagaras 2
grafo_rumania.add_edge("Fagaras","Sibiu",distancia=99,estado_de_carretera=7,peligrosidad=2)

#aristas de Hirsova 
grafo_rumania.add_edge("Hirsova","Urziceni",distancia=98,estado_de_carretera=7,peligrosidad=4)

#aristas de Iasi
grafo_rumania.add_edge("Iasi","Neamt",distancia=87,estado_de_carretera=5,peligrosidad=3)
grafo_rumania.add_edge("Iasi","Vaslui",distancia=92,estado_de_carretera=7,peligrosidad=4)

#aristas de Lugoj
grafo_rumania.add_edge("Lugoj","Timisoara",distancia=111,estado_de_carretera=6,peligrosidad=3)
grafo_rumania.add_edge("Lugoj","Mehadia",distancia=70,estado_de_carretera=4,peligrosidad=4)

#aristas de Oradea
grafo_rumania.add_edge("Oradea","Zerind",distancia=71,estado_de_carretera=6,peligrosidad=4)
grafo_rumania.add_edge("Oradea","Sibiu",distancia=151,estado_de_carretera=6,peligrosidad=3)

#aristas de Pitesti
grafo_rumania.add_edge("Pitesti","Rimnicu Vilcea",distancia=97,estado_de_carretera=7,peligrosidad=2)

#aristas de Rimnicu Vilcea
grafo_rumania.add_edge("Rimnicu Vilcea","Sibiu",distancia=80,estado_de_carretera=6,peligrosidad=2)

#aristas de Urziceni
grafo_rumania.add_edge("Urziceni","Vaslui",distancia=142,estado_de_carretera=5,peligrosidad=2)

#print(grafo_rumania.number_of_nodes()) #20
#print(grafo_rumania.number_of_edges()) #23