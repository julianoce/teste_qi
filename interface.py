import Tkinter as tk
from transformacao import *

class Interface:
	def __init__(self, master):
		self.root = master
		self.root.wm_title('Teste de QI')
		self.cv = tk.Canvas(self.root,height="500",width="500",bg="white")

		self.reta = {
			"vertices": {
				"v1": [0,  0, 1], 
				"v2": [0, 30, 1]
			},
			"faces": {
				"f1": ["v1", "v2"]
			}
		}

		self.triangulo = {
			"vertices": {
				"v1": [0, 40, 1], 
				"v2": [20, 0, 1], 
				"v3": [40, 40, 1]
			},
			"faces": {
				"f1": ["v1", "v2", "v3"]
			}
		}

		self.triangulo_ret = {
			"vertices": {
				"v1": [0, 40, 1], 
				"v2": [0, 0, 1], 
				"v3": [40, 40, 1]
			},
			"faces": {
				"f1": ["v1", "v2", "v3"]
			}
		}

		self.quadrado = {
			"vertices": {
				"v1": [0, 0, 1], 
				"v2": [40, 0, 1], 
				"v3": [40, 40, 1], 
				"v4": [0, 40, 1]
			},
			"faces": {
				"f1": ["v1", "v2", "v3", "v4"]
			}
		}
			
		self.pentagono = {
			"vertices": {
				"v1": [0,0,1],
				"v2": [-19,14,1],
				"v3": [-12,36,1],
				"v4": [12,36,1],
				"v5": [19,14,1],
			},
			"faces": {
				"f1": ["v1", "v2", "v3", "v4", "v5"]
			}
		}

		self.hexagono = {
			"vertices": {
				"v1": [0,0,1],
				"v2": [-20,0,1],
				"v3": [-30,17,1],
				"v4": [-20,34,1],
				"v5": [0,34,1],
				"v6": [10,17,1],
			},
			"faces": {
				"f1": ["v1", "v2", "v3", "v4", "v5", "v6"]
			}
		}

		self.heptagono = {
			"vertices": {
				"v1": [0,0,1],
				"v2": [-16,8,1],
				"v3": [-19,24,1],
				"v4": [-9,38,1],
				"v5": [9,38,1],
				"v6": [19,24,1],
				"v7": [16,8,1],
			},
			"faces": {
				"f1": ["v1", "v2", "v3", "v4", "v5", "v6", "v7"]
			}
		}

		self.octogono = {
			"vertices": {
				"v1": [0,0,1],
				"v2": [-16,0,1],
				"v3": [-26,10,1],
				"v4": [-26,26,1],
				"v5": [-16,36,1],
				"v6": [0,36,1],
				"v7": [10,26,1],
				"v8": [10,10,1],
			},
			"faces": {
				"f1": ["v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8"]
			}
		}

		self.estrela = {
			"vertices": {
				"v1": [0,0,1],
				"v2": [14, -2,1],
				"v3": [20, -13,1],
				"v4": [26, -2,1],
				"v5": [40,0,1],
				"v6": [30, 8,1],
				"v7": [33,20,1],
				"v8": [20, 13,1],
				"v9": [6,20,1],
				"v10": [10,8,1],
			},
			"faces": {
				"f1": ["v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9", "v10"]
			}
		}

		self.nave = {
			"vertices": {
				"v1": [0,0,1],
				"v2": [10, 20,1],
				"v3": [0, 40,1],
				"v4": [40, 20,1]
			},
			"faces": {
				"f1": ["v1", "v2", "v3", "v4"]
			}
		}

		self.seta = {
			"vertices": {
				"v1": [0,0,1],
				"v2": [0,20,1],
				"v3": [25,20,1],
				"v4": [25,30,1],
				"v5": [40,10,1],
				"v6": [25,-10,1],
				"v7": [25,0,1]
			},
			"faces": {
				"f1": ["v1", "v2", "v3", "v4", "v5", "v6", "v7"]
			}
		}

		self.casa = {
			"vertices": {
				"v1": [0,0,1],
				"v2": [0,20,1],
				"v3": [40,20,1],
				"v4": [40,0,1],
				"v5": [20, -20,1]
			},
			"faces": {
				"f1": ["v1", "v2", "v3", "v4", "v5"]
			}
		}


	def draw(self, coordenadas):
		self.cv.create_line([(x,y) for x, y, _ in coordenadas+[coordenadas[0]]])

	
	def plotar_figura(self, figura, posicao_x, posicao_y):
		for f in figura["faces"]:
			face = figura["faces"][f]
			T = translacao( [figura["vertices"][v] for v in face] , posicao_x, posicao_y)
			vertices = [(x, y) for x, y, _ in T]
			self.cv.create_line(vertices+[vertices[0]])
	

	def rotacionar(self, figura, angulo):
		for f in figura["faces"]:
			face = figura["faces"][f]
			vertices = [figura["vertices"][v] for v in face]
			return rotacao(vertices, angulo)


	def escalonar(self, figura, x, y):
		for f in figura["faces"]:
			face = figura["faces"][f]
			vertices = [figura["vertices"][v] for v in face]
			return escalonamento(vertices, x, y)
	
	
	def primeira_pergunta(self):
		self.cv.create_text(100,20,fill="black",font="Times 15", text="Pergunta 1:")

		#linha 01
		self.plotar_figura(self.triangulo,50,50)

		self.plotar_figura(self.reta, 130,55)
		self.reta_90 = self.rotacionar(self.reta, 90)
		self.draw(translacao(self.reta_90,115,70))

		self.plotar_figura(self.quadrado,180,50)

		self.draw(translacao(self.reta_90,250,65))
		self.draw(translacao(self.reta_90,250,75))

		self.plotar_figura(self.heptagono,330,50)

		#linha 02
		self.plotar_figura(self.hexagono, 80,120)

		self.draw(translacao(self.reta_90, 115, 135))

		self.plotar_figura(self.triangulo, 180, 110)

		self.draw(translacao(self.reta_90,250,130))
		self.draw(translacao(self.reta_90,250,140))

		self.plotar_figura(self.triangulo, 310, 110)

		# #linha 03
		self.plotar_figura(self.octogono, 80,180)

		self.draw(translacao(self.reta_90,115,200))

		self.plotar_figura(self.triangulo, 180, 170)

		self.draw(translacao(self.reta_90,250,190))
		self.draw(translacao(self.reta_90,250,200))

		self.cv.create_text(330,190,fill="black",font="Times 30", text="?")

		#respostas
		self.resposta_a = tk.Button(self.cv, text = 'A', width = 5)
		self.resposta_a_window = self.cv.create_window(60, 300, window=self.resposta_a)

		self.resposta_b = tk.Button(self.cv, text = 'B', width = 5)
		self.resposta_b_window = self.cv.create_window(200, 300, window=self.resposta_b)

		self.resposta_c = tk.Button(self.cv, text = 'C', width = 5)
		self.resposta_c_window = self.cv.create_window(60, 350, window=self.resposta_c)

		self.resposta_d = tk.Button(self.cv, text = 'D', width = 5)
		self.resposta_d_window = self.cv.create_window(200, 350, window=self.resposta_d)

		self.cv.pack(side="top", fill="both", expand=True)

	#fazer
	def segunda_pergunta(self):
		self.cv.create_text(100,20,fill="black",font="Times 15", text="Pergunta 2:")

		self.reta_90 = self.rotacionar(self.reta, 90)

		#linha 01
		self.retangulo = translacao(self.escalonar(self.quadrado, 1.6, 1), 30, 55)
		self.draw(self.retangulo)

		self.plotar_figura(self.reta, 125,53)
		self.chapeu = translacao(escalonamento(self.rotacionar(self.triangulo, 180), 0.5,0.5), 135, 87)
		self.draw(self.chapeu)

		self.plotar_figura(self.triangulo, 165, 50)

		self.draw(translacao(self.reta_90,235,68))
		self.draw(translacao(self.reta_90,235,78))

		self.plotar_figura(self.casa, 288, 68)

		#minha casa, nao tocar
		# self.retangulo = translacao(self.escalonar(self.quadrado, 1, 0.6), 285, 65)
		# self.cv.create_line(self.retangulo+self.retangulo[0])
		# self.triangulo = translacao(self.escalonar(self.triangulo, 1, 0.6), 285, 40)
		# self.cv.create_line(self.triangulo+self.triangulo[0])

		#linha 02
		self.triangulo_30 = translacao(self.rotacionar(self.triangulo, 30), 25, 120)
		self.draw(self.triangulo_30)

		self.draw(translacao(self.reta_90,105,135))
		self.chapeu = translacao(escalonamento(self.rotacionar(self.triangulo, 270), 0.5,0.5), 137, 125)
		self.draw(self.chapeu)

		self.retangulo = translacao(self.escalonar(self.quadrado, 1.6, 1), 150, 115)
		self.draw(self.retangulo)

		self.draw(translacao(self.reta_90,235,128))
		self.draw(translacao(self.reta_90,235,138))	

		self.plotar_figura(self.seta, 287, 125)

		#linha 03
		self.triangulo_330 = translacao(self.rotacionar(self.triangulo, 330), 60, 160)
		self.draw(self.triangulo_330)

		self.draw(translacao(self.reta_90,105,195))
		self.chapeu = translacao(escalonamento(self.rotacionar(self.triangulo, 90), 0.5,0.5), 103, 205)
		self.draw(self.chapeu)

		self.triangulo_30 = translacao(self.rotacionar(self.triangulo, 30), 155, 180)
		self.draw(self.triangulo_30)

		self.draw(translacao(self.reta_90,235,188))
		self.draw(translacao(self.reta_90,235,198))

		self.cv.create_text(305,195,fill="black",font="Times 30", text="?")

		# losango
		# self.losango = translacao(self.rotacionar(self.quadrado, 45), 90, 150)
		# self.cv.create_line(self.losango+self.losango[0])		

		#respostas
		self.resposta_a = tk.Button(self.cv, text = 'A', width = 5)
		self.resposta_a_window = self.cv.create_window(60, 300, window=self.resposta_a)

		self.resposta_b = tk.Button(self.cv, text = 'B', width = 5)
		self.resposta_b_window = self.cv.create_window(200, 300, window=self.resposta_b)

		self.resposta_c = tk.Button(self.cv, text = 'C', width = 5)
		self.resposta_c_window = self.cv.create_window(60, 350, window=self.resposta_c)

		self.resposta_d = tk.Button(self.cv, text = 'D', width = 5)
		self.resposta_d_window = self.cv.create_window(200, 350, window=self.resposta_d)
		self.cv.pack(side="top", fill="both", expand=True)


	def terceira_pergunta(self):
		self.cv.create_text(100,20,fill="black",font="Times 15", text="Pergunta 3:")
		
		#linha 01
		self.nave_90 = translacao(self.rotacionar(self.nave, 90), 50, 90)
		self.draw(self.nave_90)

		self.nave_45 = translacao(self.rotacionar(self.nave, 45), 120, 70)
		self.draw(self.nave_45)

		self.plotar_figura(self.nave, 200, 50)

		#linha 02
		self.nave_180 = translacao(self.rotacionar(self.nave, 180), 90, 150)
		self.draw(self.nave_180)
		
		self.nave_135 = translacao(self.rotacionar(self.nave, 135), 140, 155)
		self.draw(self.nave_135)
		
		self.nave_90 = translacao(self.rotacionar(self.nave, 90), 200, 150)
		self.draw(self.nave_90)
		
		#linha 03
		self.nave_270 = translacao(self.rotacionar(self.nave, 270), 94, 180)
		self.draw(self.nave_270)
		
		self.nave_225 = translacao(self.rotacionar(self.nave, 225), 170, 206)
		self.draw(self.nave_225)

		self.cv.create_text(220,190,fill="black",font="Times 30", text="?")

		#respostas
		self.resposta_a = tk.Button(self.cv, text = 'A', width = 5)
		self.resposta_a_window = self.cv.create_window(60, 300, window=self.resposta_a)

		self.resposta_b = tk.Button(self.cv, text = 'B', width = 5)
		self.resposta_b_window = self.cv.create_window(200, 300, window=self.resposta_b)

		self.resposta_c = tk.Button(self.cv, text = 'C', width = 5)
		self.resposta_c_window = self.cv.create_window(60, 350, window=self.resposta_c)

		self.resposta_d = tk.Button(self.cv, text = 'D', width = 5)
		self.resposta_d_window = self.cv.create_window(200, 350, window=self.resposta_d)
		self.cv.pack(side="top", fill="both", expand=True)


	def quarta_pergunta(self):
		self.cv.create_text(100,20,fill="black",font="Times 15", text="Pergunta 4:")
		
		#quadrados da tela
		#linha 01
		self.plotar_figura(self.quadrado, 50, 50)
		self.plotar_figura(self.quadrado, 130, 50)
		self.plotar_figura(self.quadrado, 210, 50)

		#linha 02
		self.plotar_figura(self.quadrado, 50, 120)
		self.plotar_figura(self.quadrado, 130, 120)
		self.plotar_figura(self.quadrado, 210, 120)

		#linha 03
		self.plotar_figura(self.quadrado, 50, 190)
		self.plotar_figura(self.quadrado, 130, 190)

		#figuras no interior
		#linha 01
		self.quadradinho = translacao(self.escalonar(self.quadrado, 0.5, 1), 70, 50)
		self.draw(self.quadradinho)

		self.quadradinho = translacao(self.escalonar(self.quadrado, 0.5, 0.5), 150, 50)
		self.draw(self.quadradinho)

		self.quadradinho = translacao(self.escalonar(self.quadrado, 0.5, 0.5), 230, 70)
		self.draw(self.quadradinho)

		#linha 02
		self.quadradinho = translacao(self.escalonar(self.quadrado, 1, 0.5), 50, 120)
		self.draw(self.quadradinho)

		self.quadradinho = translacao(self.escalonar(self.quadrado, 0.5, 0.5), 130, 140)
		self.draw(self.quadradinho)

		self.quadradinho = translacao(self.escalonar(self.quadrado, 0.5, 0.5), 230, 140)
		self.draw(self.quadradinho)

		#linha 03
		#quadrado preenchido ao desenhar
		self.triangulo = translacao(self.rotacionar(self.triangulo_ret, 270), 170, 190)
		self.draw(self.triangulo)
		self.cv.create_text(230,210,fill="black",font="Times 30", text="?")

		#respostas
		self.resposta_a = tk.Button(self.cv, text = 'A', width = 5)
		self.resposta_a_window = self.cv.create_window(60, 300, window=self.resposta_a)

		self.resposta_b = tk.Button(self.cv, text = 'B', width = 5)
		self.resposta_b_window = self.cv.create_window(200, 300, window=self.resposta_b)

		self.resposta_c = tk.Button(self.cv, text = 'C', width = 5)
		self.resposta_c_window = self.cv.create_window(60, 350, window=self.resposta_c)

		self.resposta_d = tk.Button(self.cv, text = 'D', width = 5)
		self.resposta_d_window = self.cv.create_window(200, 350, window=self.resposta_d)
		self.cv.pack(side="top", fill="both", expand=True)

	
	def quinta_pergunta(self):
		self.cv.create_text(100,20,fill="black",font="Times 15", text="Pergunta 5:")
		
		#linha 01
		self.plotar_figura(self.estrela,50,70)
		self.plotar_figura(self.seta,130,65)
		self.plotar_figura(self.casa,200,70)

		#linha 02
		self.plotar_figura(self.casa,50,130)
		self.plotar_figura(self.estrela,130,130)
		self.plotar_figura(self.seta,200,130)

		#linha 03
		self.plotar_figura(self.seta,50,190)
		self.plotar_figura(self.casa,130,190)
		self.cv.create_text(220,190,fill="black",font="Times 30", text="?")

		#respostas
		self.resposta_a = tk.Button(self.cv, text = 'A', width = 5)
		self.resposta_a_window = self.cv.create_window(60, 300, window=self.resposta_a)

		self.resposta_b = tk.Button(self.cv, text = 'B', width = 5)
		self.resposta_b_window = self.cv.create_window(200, 300, window=self.resposta_b)

		self.resposta_c = tk.Button(self.cv, text = 'C', width = 5)
		self.resposta_c_window = self.cv.create_window(60, 350, window=self.resposta_c)

		self.resposta_d = tk.Button(self.cv, text = 'D', width = 5)
		self.resposta_d_window = self.cv.create_window(200, 350, window=self.resposta_d)


		self.cv.pack(side="top", fill="both", expand=True)