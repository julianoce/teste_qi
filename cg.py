import Tkinter as tk
import numpy as np
import math

def rotacao(coordenadas, angulo):
	M = np.array([ [math.cos(angulo), -math.sin(angulo)],
				   [math.sin(angulo), math.cos(angulo)] ])

	return [list(l) for l in np.matmul(np.array(coordenadas), M)]


def translacao(coordenadas, xt=0, yt=0):
	T = [(x+xt, y+yt) for x, y in coordenadas]
	return T+[T[0]]


def escalonar(coordenadas, xt=1, yt=1):
	M = np.array([[xt, 0],[0, yt]])

	return [list(l) for l in np.matmul(np.array(coordenadas), M)]


def reflexao_eixo(coordenadas, xt=1, yt=1):
	return escalonar(coordenadas, xt, yt)


def reflexao_reta(coordenadas):
	M = np.array([[0, 1],[1, 0]])

	return [list(l) for l in np.matmul(np.array(coordenadas), M)]


figura = {
	# 'reta': [[0,0], [0, 40]],
	# 'triangulo': [[0, 40], [20, 0], [40, 40],
	# 'quadrado':  [[0, 0], [40, 0], [40, 40], [0, 40],
	# 'pentagono': [[0, 0], [0, 20], [20, 30], [40,10], [20, -10]],
	'hexagono': [[0, 0], [0, 20], [20, 30], [40,20], [40,0], [20, -10]]
}

cv = tk.Canvas(tk.Tk(),height="500",width="500",bg="white")
cv.pack()

for f in figura:
	cv.create_line(figura[f]+[figura[f][0]])
	r = rotacao(figura[f], 90)
	r.append(r[0])
	# r = reflexao_reta(figura[f])
	# cv.create_line(translacao(r, 120, 120))
	cv.create_line(translacao(figura[f], 100, 100))

tk.mainloop()