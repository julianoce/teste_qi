import Tkinter as tk
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
		return escalonar(face, m=-1)
	
	return escalonar(face, n=-1)


def reflexao_reta(coordenadas):
	M = np.array([[0, 0, 1],
				  [0, 1, 0],
				  [1, 0, 0]])

	r = []
	for c in coordenadas:
		r.append(list(np.matmul(M, np.array(c))))
	return r
