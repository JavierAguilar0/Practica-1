import random
import numpy as np
#lista de caballos
caballos_a=['a1','a2','a3','a4','a5']
caballos_b=['b1','b2','b3','b4','b5']
caballos_c=['c1','c2','c3','c4','c5']
caballos_d=['d1','d2','d3','d4','d5']
caballos_e=['e1','e2','e3','e4','e5']
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
print('El mas rapido: a1',velocidad[4,4])
#Carrera 7
print('\nSeptima carrera')
if velocidad[3,4]>velocidad[4,0] and velocidad[3,4]>velocidad[4,1] and velocidad[3,4]>velocidad[4,2] and velocidad[3,4]>velocidad[4,3]:
    print('El segundo mas rapido: b1',velocidad[3,4])
elif velocidad[4,3]>velocidad[3,4]:
    print('El segundo mas rapido: a2',velocidad[4,3])
elif velocidad[3,4]==velocidad[4,3]:
    print('Empate entre b1',velocidad[3,4],'y a2',velocidad[4,3])
print('\n')
    
grafo={'caballos':{'grupo a':5,'grupo b':5,'grupo c':5,'grupo d':5,'grupo e':5},
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

def grafito(grafo,vertice,fin):
	distancia={}
	avanzado={}
	restante=grafo
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

		for siguiente, peso in grafo[nodominimo].items():
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

grafito(grafo, 'caballos', 'segundo rapido')