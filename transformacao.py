import numpy as np
import math
from math import sqrt


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
	vertices = coordenadas.keys()
	r = np.matmul(c, M).tolist()

	for c, v, ri in zip(c, vertices, r):
		objeto["vertices"][v] = ri[:2]+[ri[3]]
		

	return objeto

def isometrica_z(objeto):
	M = np.array([[sqrt(3/6),  1/sqrt(6), sqrt(2/6), 0],
				  [  0,    2/sqrt(6), -sqrt(2/6), 0],
				  [-sqrt(3/6), 1/sqrt(6), sqrt(2/6), 0],
				  [  0,      0,   0, 1]])

	# N = np.array([[1, 0, 0, 0],
	# 			  [0, 1, 0, 0],
	# 			  [0, 0, 0, 0],
	# 			  [0, 0, 0, 1]])

	coordenadas = objeto["vertices"]

	c = np.array(list(coordenadas.values()))
	vertices = coordenadas.keys()
	r = np.matmul(c, M).tolist()

	# h = np.matmul(r, N).tolist()

	for c, v, ri in zip(c, vertices, r):
		objeto["vertices"][v] = ri[:3]
		
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


def normal(v1,v2):
	print(v1)
	print(v2)
	i = ((v1[1]*v2[2]) - (v1[2]*v2[1]))
	j = ((v1[2]*v2[0]) - (v1[0]*v2[2]))
	k = ((v1[0]*v2[1]) - (v1[1]*v2[0]))
	return [i,j,k]

def back_face(objeto):
	resp = list()
	for f in objeto["faces"]:
		n = normal(objeto["vertices"][objeto["faces"][f][0]],objeto["vertices"][objeto["faces"][f][2]])
		print("face ",end="")
		print(f)
		print("normal ",end="")
		print(n)
		if (n[2]>0):
			resp.append(f)
	print(resp)
	return resp