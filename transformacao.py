import numpy as np
import math


def translacao(coordenadas, m=0, n=0):
	M = np.array([[1, 0, m],
				  [0, 1, n],
				  [0, 0, 1]])

	r = []
	for c in coordenadas:
		r.append(list(np.matmul(M, np.array(c))))
	
	return r

def isometrica(objeto):
	M = np.array([[0.707,  0.408, 0, 0],
				  [  0,    0.816, 0, 0],
				  [0.707, -0.408, 0, 0],
				  [  0,      0,   0, 1]])

	coordenadas = objeto["vertices"]

	c = np.array(list(coordenadas.values()))

	e = []
	for i in range(len(coordenadas)):
		e.append(coordenadas["v{}".format(i+1)])


	r = np.matmul(e, M).tolist()


	for i in range(len(r)):
		objeto["vertices"]["v{}".format(i+1)] = r[i][:2]+[r[i][3]]

	return objeto


def escalonamento(coordenadas, m=1, n=1):
	M = np.array([[m, 0, 0],
				  [0, n, 0],
				  [0, 0, 1]])

	r = []
	for c in coordenadas:
		r.append(list(np.matmul(M, np.array(c))))
	return r

		
def rotacao(coordenadas, rad):
	angulo = math.radians(rad)
	M = np.array([ [math.cos(angulo), -math.sin(angulo), 0],
				   [math.sin(angulo),  math.cos(angulo), 0],
				   [               0,                 0, 1] ])
	r = []
	for c in coordenadas:
		r.append(list(np.matmul(np.array(c), M)))

	return r


def reflexao_eixo(coordenadas, eixo):
	if eixo == 'x':
		return escalonamento(coordenadas, n=-1)
	
	return escalonamento(coordenadas, m=-1)


def reflexao_reta(coordenadas):
	M = np.array([[0, 0, 1],
				  [0, 1, 0],
				  [1, 0, 0]])

	r = []
	for c in coordenadas:
		r.append(list(np.matmul(M, np.array(c))))
	return r
