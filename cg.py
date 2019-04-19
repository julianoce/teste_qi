import Tkinter as tk
import numpy as np
import math

def rotacao(coordenadas, angulo):
	M = np.array([ [math.cos(angulo), -math.sin(angulo)],
				   [math.sin(angulo), math.cos(angulo)] ])

	T = []
	for xy in coordenadas:
		T.append((list(np.matmul(np.array(xy), M))))

	print(T)

	return T+[T[0]]


def translacao(coordenadas, xt=0, yt=0):
	T = [(x+xt, y+yt) for x, y in coordenadas]
	return T+[T[0]]


def escalonar(coordenadas, xt=0, yt=0)


figura = {
	'triangulo': [(0, 40), (20, 0), (40, 40)],
	# 'quadrado':  [(10, 100), (10, 10), (100, 10), (100, 100)]
}

cv = tk.Canvas(tk.Tk(),height="500",width="500",bg="white")
cv.pack()

for f in figura:
	cv.create_line(figura[f]+[figura[f][0]])
	r = rotacao(figura[f], 45)
	cv.create_line(translacao(r, 120, 120))
	# cv.create_line(translacao(figura[f], 100))

tk.mainloop()