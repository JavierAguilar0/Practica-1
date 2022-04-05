#Javier Arturo Aguilar Corona
#19110054
#6E1 Mecatronica
import random
import numpy as np
#import networkx as nx
#import graphviz
#lista de caballos
caballos=['a5','a4','a3','a2','a1','b5','b4','b3','b2','b1','c5','c4','c3','c2','c1','d5','d4','d3','d2','d1','e5','e4','e3','e2','e1']
caballos_a=caballos[0:5]
caballos_b=caballos[5:10]
caballos_c=caballos[10:15]
caballos_d=caballos[15:20]
caballos_e=caballos[20:25]
print('Competidores')
print('grupo 1:',caballos_a)
print('grupo 2:',caballos_b)
print('grupo 3:',caballos_c)
print('grupo 4:',caballos_d)
print('grupo 5:',caballos_e)
#velocidades al azar
velocidad=np.zeros((5,5))
dimension=velocidad.shape
for x in range(dimension[0]):
    for y in range(dimension[1]):
        velocidad[x,y]=random.randint(1, 100)
#velocidades acomodadas de menor a mayor
print('\nVelocidades acomodadas')
for x in range(5):
    velocidad[x].sort()
velocidad=velocidad[np.argsort(velocidad[:,-1])]
for x in range(5):
    print('grupo',5-x,':',velocidad[x])
#primeras 5 carreras
print('\nPrimeras 5 carreras')
for x in range(5):
    print('ganador grupo',5-x,velocidad[x,4])
#carrera 6
print('\nCarrera 6')
print('competidores: e1',velocidad[0,4],'d1',velocidad[1,4],'c1',velocidad[2,4],'b1',velocidad[3,4],'a1',velocidad[4,4])
print('El mas rapido: a1',velocidad[4,4])
#Carrera 7
print('\nSeptima carrera')
print('competidores: a5',velocidad[4,0],'a4',velocidad[4,1],'a3',velocidad[4,2],'a2',velocidad[4,3],'b1',velocidad[3,4])
if velocidad[3,4]>velocidad[4,0] and velocidad[3,4]>velocidad[4,1] and velocidad[3,4]>velocidad[4,2] and velocidad[3,4]>velocidad[4,3]:
    print('El segundo mas rapido: b1',velocidad[3,4])
elif velocidad[4,3]>velocidad[3,4]:
    print('El segundo mas rapido: a2',velocidad[4,3])
elif velocidad[3,4]==velocidad[4,3]:
    print('Empate entre b1',velocidad[3,4],'y a2',velocidad[4,3])
print('\nEl minimo de carreras para encontrar los dos mas rapidos fue de 7\n')
#quitar comillas en caso de tener pygraphviz y graphviz
"""grafo=nx.Graph()
grafo.add_node("Caballos")
grafo.add_node("Grupo 1")
grafo.add_node("Grupo 2")
grafo.add_node("Grupo 3")
grafo.add_node("Grupo 4")
grafo.add_node("Grupo 5")
grafo.add_node("Ganador 1")
grafo.add_node("Ganador 2")
grafo.add_node("Ganador 3")
grafo.add_node("Ganador 4")
grafo.add_node("Ganador 5")
grafo.add_node("El mas Rapido")
grafo.add_node("El segundo mas rapido")

grafo.add_edge("Caballos","Grupo 1")
grafo.add_edge("Caballos","Grupo 2")
grafo.add_edge("Caballos","Grupo 3")
grafo.add_edge("Caballos","Grupo 4")
grafo.add_edge("Caballos","Grupo 5")
grafo.add_edge("Grupo 1","Ganador 1")
grafo.add_edge("Grupo 2","Ganador 2")
grafo.add_edge("Grupo 3","Ganador 3")
grafo.add_edge("Grupo 4","Ganador 4")
grafo.add_edge("Grupo 5","Ganador 5")
grafo.add_edge("Ganador 1","El mas rapido")
grafo.add_edge("Ganador 2","El mas rapido")
grafo.add_edge("Ganador 3","El mas rapido")
grafo.add_edge("Ganador 4","El mas rapido")
grafo.add_edge("Ganador 5","El mas rapido")
grafo.add_edge("Ganador 2","El segundo mas rapido")
grafo.add_edge("Grupo 1","El segundo mas rapido")

g=nx.nx_agraph.to_agraph(grafo)
g.layout('dot')
g.draw('grafo.png')
nx.write_graphhml(g,"caballos.graphml")"""

grafo2={'caballos':{'grupo a':5,'grupo b':5,'grupo c':5,'grupo d':5,'grupo e':5},
      'grupo a':{'ganador 1':5,'segundo rapido':10},
      'grupo b':{'ganador 2':5},
      'grupo c':{'ganador 3':5},
      'grupo d':{'ganador 4':5},
      'grupo e':{'ganador 5':5},
      'ganador 1':{'mas rapido':5},
      'ganador 2':{'mas rapido':10,'segundo rapido':10},
      'ganador 3':{'mas rapido':15},
      'ganador 4':{'mas rapido':10},
      'ganador 5':{'mas rapido':5},
      'mas rapido':{},
      'segundo rapido':{}}

def grafito(grafo2,vertice,fin):
	distancia={}
	avanzado={}
	restante=grafo2
	infinito=9999999
	camino=[]

	for nodo in restante:
		distancia[nodo]=infinito
	distancia[vertice]=0

	while restante:
		nodominimo=None
		for nodo in restante:
			if nodominimo is None:
				nodominimo=nodo
			elif distancia[nodo]<distancia[nodominimo]:
				nodominimo=nodo

		for siguiente, peso in grafo2[nodominimo].items():
			if peso+distancia[nodominimo]<distancia[siguiente]:
				distancia[siguiente]=peso+distancia[nodominimo]
				avanzado[siguiente]=nodominimo
		restante.pop(nodominimo)

	actual=fin
	while actual!=vertice:
		try:
			camino.insert(0,actual)
			actual=avanzado[actual]
		except KeyError:
			print("No es posible continuar el camino")
			break
	camino.insert(0,vertice)
	if distancia[fin]!=infinito:
		print("La distancia más corta desde " + str.upper(vertice) + " hasta " + str.upper(fin) + " es " + str(distancia[fin]))
		print("El camino más corto es: " + str(camino))

grafito(grafo2, 'caballos', 'segundo rapido')