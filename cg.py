import tkinter as tk
import numpy as np
import math

def rotacao(coordenadas, rad):
	angulo = math.radians(rad)
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


reta = {
	"vertices": {
		"v1": [0,0], 
		"v2": [0, 40]
	},
	"faces": {
		"f1": ["v1", "v2"]
	}
}

triangulo = {
	"vertices": {
		"v1": [0, 40], 
		"v2": [20, 0], 
		"v3": [40, 40]
	},
	"faces": {
		"f1": ["v1", "v2", "v3"]
	}
}

quadrado = {
	"vertices": {
		"v1": [0, 0], 
		"v2": [40, 0], 
		"v3": [40, 40], 
		"v4": [0, 40]
	},
	"faces": {
		"f1": ["v1", "v2", "v3", "v4"]
	}
}
	
pentagono = {
	"vertices": {
		"v1": [0,0],
		"v2": [-19,14],
		"v3": [-12,36],
		"v4": [12,36],
		"v5": [19,14],
	},
	"faces": {
		"f1": ["v1", "v2", "v3", "v4", "v5"]
	}
}

hexagono = {
	"vertices": {
		"v1": [0,0],
		"v2": [-20,0],
		"v3": [-30,17],
		"v4": [-20,34],
		"v5": [0,34],
		"v6": [10,17],
	},
	"faces": {
		"f1": ["v1", "v2", "v3", "v4", "v5", "v6"]
	}
}

heptagono = {
	"vertices": {
		"v1": [0,0],
		"v2": [-16,8],
		"v3": [-19,24],
		"v4": [-9,38],
		"v5": [9,38],
		"v6": [19,24],
		"v7": [16,8],
	},
	"faces": {
		"f1": ["v1", "v2", "v3", "v4", "v5", "v6", "v7"]
	}
}

octogono = {
	"vertices": {
		"v1": [0,0],
		"v2": [-16,0],
		"v3": [-26,10],
		"v4": [-26,26],
		"v5": [-16,36],
		"v6": [0,36],
		"v7": [10,26],
		"v8": [10,10],
	},
	"faces": {
		"f1": ["v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8"]
	}
}

estrela = {
	"vertices": {
		"v1": [0,0],
		"v2": [14, -2],
		"v3": [20, -13],
		"v4": [26, -2],
		"v5": [40,0],
		"v6": [30, 8],
		"v7": [33,20],
		"v8": [20, 13],
		"v9": [6,20],
		"v10": [10,8],
	},
	"faces": {
		"f1": ["v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9", "v10"]
	}
}

nave = {
	"vertices": {
		"v1": [0,0],
		"v2": [10, 20],
		"v3": [0, 40],
		"v4": [40, 20]
	},
	"faces": {
		"f1": ["v1", "v2", "v3", "v4"]
	}
}

seta = {
	"vertices": {
		"v1": [0,0],
		"v2": [0,20],
		"v3": [25,20],
		"v4": [25,30],
		"v5": [40,10],
		"v6": [25,-10],
		"v7": [25,0]
	},
	"faces": {
		"f1": ["v1", "v2", "v3", "v4", "v5", "v6", "v7"]
	}
}

casa = {
	"vertices": {
		"v1": [0,0],
		"v2": [0,20],
		"v3": [40,20],
		"v4": [40,0],
		"v5": [20, -20]
	},
	"faces": {
		"f1": ["v1", "v2", "v3", "v4", "v5"]
	}
}



class Interface:
	def __init__(self, master):
		self.root = root
		self.root.wm_title('Teste de QI')
		self.cv = tk.Canvas(self.root,height="500",width="500",bg="white")
	
	def plotar_figura(self, figura, posicao_x, posicao_y):
		for f in figura["faces"]:
			face = figura["faces"][f]
			vertices = [figura["vertices"][v] for v in face]
			self.cv.create_line(translacao(vertices+[vertices[0]], posicao_x, posicao_y))
	
	def rotacionar(self, figura, angulo):
		for f in figura["faces"]:
			face = figura["faces"][f]
			vertices = [figura["vertices"][v] for v in face]
			return rotacao(vertices+[vertices[0]], angulo)
	
	
	def primeira_pergunta(self):
		self.cv.create_text(100,20,fill="black",font="Times 15", text="Pergunta 1:")
		self.plotar_figura(triangulo,50,50)
		self.mais_1 = self.plotar_figura(reta, 130,50)
		self.mais_2 = self.rotacionar(reta, 90)
		self.cv.create_line(self.mais_2, 130, 50)
		# self.cv.create_text(120,70,fill="black",font="Times 30", text="+")
		self.plotar_figura(quadrado,180,50)
		# self.cv.create_text(240,70,fill="black",font="Times 30", text="=")
		self.plotar_figura(heptagono,290,50)
		self.cv.pack(side="top", fill="both", expand=True)
	
	def quinta_pergunta(self):
		self.cv.create_text(100,20,fill="black",font="Times 15", text="Pergunta 5:")
		self.plotar_figura(estrela,50,70)
		self.plotar_figura(seta,130,65)
		self.plotar_figura(casa,200,70)

		self.plotar_figura(casa,50,130)
		self.plotar_figura(estrela,130,130)
		self.plotar_figura(seta,200,130)

		self.plotar_figura(seta,50,190)
		self.plotar_figura(casa,130,190)
		self.cv.create_text(220,190,fill="black",font="Times 30", text="?")

		self.cv.pack(side="top", fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    main = Interface(root)

main.quinta_pergunta()

root.mainloop()
