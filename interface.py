import tkinter as tk
from transformacao import *
import time

class Interface:
	def __init__(self, master):
		self.root = master
		self.root.wm_title('Teste de QI')
		self.pontuacao = 0
		self.cv = tk.Canvas(self.root,height="350",width="350",bg="white")
		

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

		self.cont = 0

	def casa3d(self):
		return {
					"vertices": {
						"v1": [0,  0,   0, 1],
						"v2": [0,  20,  0, 1],
						"v3": [40, 20,  0, 1],
						"v4": [40, 0,   0, 1],
						"v5": [20, -20, 0, 1],
						"v6": [0,  0,   20, 1],
						"v7": [0,  20,  20, 1],
						"v8": [40, 20,  20, 1],
						"v9": [40, 0,   20, 1],
						"v10": [20, -20, 20, 1],

					},
					"faces": {
						"f1": ["v4", "v3", "v2", "v1", "v5"],
						"f2": ["v6","v7","v8","v9","v10"],
						"f3": ["v2","v7","v8","v3"],
						"f4": ["v3","v8","v9","v4"],
						"f5": ["v6","v1","v2","v7"],
						"f6": ["v10","v9","v4","v5"],
						"f7": ["v5","v10","v6","v1"]
					}
					# "faces": {
					# 	"f1": ["v1", "v2", "v3", "v4", "v5"],
					# 	"f2": ["v6","v7","v8","v9","v10"],
					# 	"f3": ["v2","v3","v8","v7"],
					# 	"f4": ["v3","v8","v9","v4"],
					# 	"f5": ["v1","v2","v7","v6"],
					# 	"f6": ["v4","v5","v10","v9"],
					# 	"f7": ["v1","v5","v10","v6"]
					# }
				}


	def draw(self, coordenadas, color="black"):
		self.cv.create_line([(x,y) for x, y, _ in coordenadas+[coordenadas[0]]], fill=color)

	
	def plotar_figura(self, figura, posicao_x, posicao_y, color="black"):
		for f in figura["faces"]:
			face = figura["faces"][f]
			T = translacao( [figura["vertices"][v] for v in face] , posicao_x, posicao_y)
			vertices = [(x, y) for x, y, _ in T]
			self.cv.create_line(vertices+[vertices[0]], fill=color)
	

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


	def escalonar_figura_3d(self, figura, x, y):
		coordenadas = figura["vertices"]
		vertices = list(coordenadas.keys())
		c = np.array(list(coordenadas.values()))
		T = escalonamento(c, x, y)
		for v in range(len(vertices)):
			figura["vertices"][vertices[v]] = T[v]

		return figura	


	def rotacionar_figura_3d(self, figura, rad):
		coordenadas = figura["vertices"]
		vertices = list(coordenadas.keys())
		c = np.array(list(coordenadas.values()))
		T = rotacao(c, rad)
		for v in range(len(vertices)):
			figura["vertices"][vertices[v]] = T[v]

		return figura			

	def desenhar_faces(self,figura,faces,posicao_x,posicao_y):
		for f in faces:
			face = figura["faces"][f]
			T = translacao( [figura["vertices"][v] for v in face] , posicao_x, posicao_y)
			vertices = [(x, y) for x, y, _ in T]
			if (self.cont%3 == 0):
				self.cont += 1
				color = "gray39"
			elif (self.cont%3 == 1):
				self.cont += 1
				color = "gray45"
			else:
				self.cont += 1
				color = "gray50"
			self.cv.create_polygon(vertices, fill=color)
			# self.cv.create_line(vertices+[vertices[0]], fill=color)

	
	def fechar_janela(self):
		self.root.destroy()


	def tela_inicial(self):
		c = isometrica(self.casa3d())
		d = isometrica_z(self.casa3d())
		p = back_face(d)
		self.desenhar_faces(c, p, 100, 100)

		fig = isometrica(self.casa3d())
		self.plotar_figura(fig, 200, 100, "green4")
		fig_r = self.rotacionar_figura_3d(isometrica(self.casa3d()), 180)
		self.plotar_figura(self.escalonar_figura_3d(fig_r, 2, 2), 152, 290, "gray70")
		self.plotar_figura(self.escalonar_figura_3d(fig, 2, 2), 200, 250, "blue")

		self.cv.create_text(170,30,fill="blue",font="Helvetica 30", text="Teste De QI")
		self.comecar = tk.Button(self.cv, text = 'Começar', width = 7, command=self.primeira_pergunta)
		self.comecar_window = self.cv.create_window(100, 180, window=self.comecar)
		self.fechar = tk.Button(self.cv, text = 'Fechar', width = 7, command=self.fechar_janela)
		self.fechar_window = self.cv.create_window(230, 180, window=self.fechar)
		self.cv.pack(side="top", fill="both", expand=True)
	
	def primeira_pergunta(self):
		self.cv.delete("all")
		self.start_time = time.time()
		self.cv.create_text(70,20,fill="blue",font="Times 15", text="Pergunta 1:")

		#linha 01
		self.plotar_figura(self.triangulo,30,50)

		self.plotar_figura(self.reta, 120,55)
		reta_90 = self.rotacionar(self.reta, 90)
		self.draw(translacao(reta_90,105,70))

		self.plotar_figura(self.quadrado,170,50)

		self.draw(translacao(reta_90,235,65))
		self.draw(translacao(reta_90,235,75))

		self.plotar_figura(self.heptagono,305,50)

		#linha 02
		self.plotar_figura(self.hexagono, 60,120)

		self.draw(translacao(reta_90, 105, 135))

		self.plotar_figura(self.triangulo, 170, 110)

		self.draw(translacao(reta_90,235,130))
		self.draw(translacao(reta_90,235,140))

		self.plotar_figura(self.triangulo, 285, 110)

		# #linha 03
		self.plotar_figura(self.octogono, 60,180)

		self.draw(translacao(reta_90,105,200))

		self.plotar_figura(self.triangulo, 170, 170)

		self.draw(translacao(reta_90,235,190))
		self.draw(translacao(reta_90,235,200))

		self.cv.create_text(305,190,fill="black",font="Times 30", text="?")

		# respostas
		# a
		a = [self.heptagono["vertices"][v] for v in self.heptagono["faces"]["f1"]]
		a = translacao(escalonamento(escalonamento(a, 0.6, 1), 1.2,1.2), 50, 255)
		self.draw(a, "blue")

		# b
		b = [self.quadrado["vertices"][v] for v in self.quadrado["faces"]["f1"]]
		b = translacao(b, 115, 260)
		self.draw(b, "blue")

		# c
		c = [self.pentagono["vertices"][v] for v in self.pentagono["faces"]["f1"]]
		c = translacao(escalonamento(c, 1.1, 1.1), 215, 260)
		self.draw(c, "blue")

		# d
		d = [self.hexagono["vertices"][v] for v in self.hexagono["faces"]["f1"]]
		d = translacao(rotacao(escalonamento(d, 1.15, 1.15), 90), 280, 268)
		self.draw(d, "blue")

		self.resposta_a = tk.Button(self.cv, text = 'A', width = 3, command = self.segunda_pergunta)
		self.resposta_a_window = self.cv.create_window(50, 320, window=self.resposta_a)

		self.resposta_b = tk.Button(self.cv, text = 'B', width = 3, command = self.segunda_pergunta)
		self.resposta_b_window = self.cv.create_window(135, 320, window=self.resposta_b)

		self.resposta_c = tk.Button(self.cv, text = 'C', width = 3, command = self.resposta_certa_1)
		self.resposta_c_window = self.cv.create_window(215, 320, window=self.resposta_c)

		self.resposta_d = tk.Button(self.cv, text = 'D', width = 3, command = self.segunda_pergunta)
		self.resposta_d_window = self.cv.create_window(300, 320, window=self.resposta_d)
		self.cv.pack(side="top", fill="both", expand=True)
				
	def resposta_certa_1(self):
		self.pontuacao += 1
		self.segunda_pergunta()



	def segunda_pergunta(self):
		self.cv.delete("all")
		self.cv.create_text(70,20,fill="blue",font="Times 15", text="Pergunta 2:")

		reta_90 = self.rotacionar(self.reta, 90)

		#linha 01
		retangulo = translacao(self.escalonar(self.quadrado, 1.6, 1), 30, 55)
		self.draw(retangulo)

		self.plotar_figura(self.reta, 125,53)
		chapeu = translacao(escalonamento(self.rotacionar(self.triangulo, 180), 0.5,0.5), 135, 87)
		self.cv.create_line([(x,y) for x, y, _ in chapeu])

		self.plotar_figura(self.triangulo, 165, 50)

		self.draw(translacao(reta_90,235,68))
		self.draw(translacao(reta_90,235,78))

		self.plotar_figura(self.casa, 288, 68)

		#linha 02
		triangulo_30 = translacao(self.rotacionar(self.triangulo, 30), 25, 120)
		self.draw(triangulo_30)

		self.draw(translacao(reta_90,105,135))
		chapeu = translacao(escalonamento(self.rotacionar(self.triangulo, 270), 0.5,0.5), 137, 125)
		self.cv.create_line([(x,y) for x, y, _ in chapeu])

		retangulo = translacao(self.escalonar(self.quadrado, 1.6, 1), 150, 115)
		self.draw(retangulo)

		self.draw(translacao(reta_90,235,128))
		self.draw(translacao(reta_90,235,138))	

		self.plotar_figura(self.seta, 287, 125)

		#linha 03
		triangulo_330 = translacao(self.rotacionar(self.triangulo, 330), 60, 160)
		self.draw(triangulo_330)

		self.draw(translacao(reta_90,105,195))
		chapeu = translacao(escalonamento(self.rotacionar(self.triangulo, 90), 0.5,0.5), 103, 205)
		self.cv.create_line([(x,y) for x, y, _ in chapeu])

		triangulo_30 = translacao(self.rotacionar(self.triangulo, 30), 155, 180)
		self.draw(triangulo_30)

		self.draw(translacao(reta_90,235,188))
		self.draw(translacao(reta_90,235,198))

		self.cv.create_text(305,195,fill="black",font="Times 30", text="?")

		# alternativas

		# a
		a = [self.seta["vertices"][v] for v in self.seta["faces"]["f1"]]
		a = reflexao_eixo(a, "y")
		a = translacao(a, 70, 265)
		self.draw(a, "blue")

		# b
		retangulo = translacao(self.escalonar(self.quadrado, 1, 0.6), 115, 275)
		triangulo = translacao(self.escalonar(self.triangulo, 1, 0.6), 115, 251)
		self.draw(retangulo, "blue")
		self.draw(triangulo, "blue")

		# c
		c = translacao(escalonamento(self.rotacionar(self.quadrado, 45), 0.8, 0.8), 193, 275) # c
		self.draw(c, "blue")

		#d
		d = [self.casa["vertices"][v] for v in self.casa["faces"]["f1"]]
		d = reflexao_eixo(d, "x")
		d = translacao(d, 280, 280)
		self.draw(d, "blue")

		self.resposta_a = tk.Button(self.cv, text = 'A', width = 3, command = self.terceira_pergunta)
		self.resposta_a_window = self.cv.create_window(50, 320, window=self.resposta_a)

		self.resposta_b = tk.Button(self.cv, text = 'B', width = 3, command = self.terceira_pergunta)
		self.resposta_b_window = self.cv.create_window(135, 320, window=self.resposta_b)

		self.resposta_c = tk.Button(self.cv, text = 'C', width = 3, command = self.resposta_certa_2)
		self.resposta_c_window = self.cv.create_window(215, 320, window=self.resposta_c)

		self.resposta_d = tk.Button(self.cv, text = 'D', width = 3, command = self.terceira_pergunta)
		self.resposta_d_window = self.cv.create_window(300, 320, window=self.resposta_d)


		self.cv.pack(side="top", fill="both", expand=True)

	def resposta_certa_2(self):
		self.pontuacao += 1
		self.terceira_pergunta()


	def terceira_pergunta(self):
		self.cv.delete("all")
		self.cv.create_text(70,20,fill="blue",font="Times 15", text="Pergunta 3:")
		
		#linha 01
		nave_90 = translacao(self.rotacionar(self.nave, 90), 65, 90)
		self.draw(nave_90)

		nave_45 = translacao(self.rotacionar(self.nave, 45), 150, 60)
		self.draw(nave_45)

		self.plotar_figura(self.nave, 250, 50)

		#linha 02
		nave_180 = translacao(self.rotacionar(self.nave, 180), 105, 150)
		self.draw(nave_180)
		
		nave_135 = translacao(self.rotacionar(self.nave, 135), 170, 150)
		self.draw(nave_135)
		
		nave_90 = translacao(self.rotacionar(self.nave, 90), 250, 150)
		self.draw(nave_90)
		
		#linha 03
		nave_270 = translacao(self.rotacionar(self.nave, 270), 105, 170)
		self.draw(nave_270)
		
		nave_225 = translacao(self.rotacionar(self.nave, 225), 200, 195)
		self.draw(nave_225)

		self.cv.create_text(270,190,fill="black",font="Times 30", text="?")

		#respostas
		# a
		a = translacao(nave_135, -120, 150)
		self.draw(a, "blue")

		# b
		b = [self.nave["vertices"][v] for v in self.nave["faces"]["f1"]]
		b = translacao(b, 115, 260)
		self.draw(b, "blue")

		# c
		c = translacao(nave_270, 130, 90)
		self.draw(c, "blue")

		# d
		d = translacao(nave_180, 215, 150)
		self.draw(d, "blue")


		self.resposta_a = tk.Button(self.cv, text = 'A', width = 3, command = self.quarta_pergunta)
		self.resposta_a_window = self.cv.create_window(50, 320, window=self.resposta_a)

		self.resposta_b = tk.Button(self.cv, text = 'B', width = 3, command = self.quarta_pergunta)
		self.resposta_b_window = self.cv.create_window(135, 320, window=self.resposta_b)

		self.resposta_c = tk.Button(self.cv, text = 'C', width = 3, command = self.quarta_pergunta)
		self.resposta_c_window = self.cv.create_window(215, 320, window=self.resposta_c)

		self.resposta_d = tk.Button(self.cv, text = 'D', width = 3, command = self.resposta_certa_3)
		self.resposta_d_window = self.cv.create_window(300, 320, window=self.resposta_d)

		self.cv.pack(side="top", fill="both", expand=True)

	def resposta_certa_3(self):
		self.pontuacao += 1
		self.quarta_pergunta()



	def quarta_pergunta(self):
		self.cv.delete("all")
		self.cv.create_text(70,20,fill="blue",font="Times 15", text="Pergunta 4:")
		
		#quadrados da tela
		#linha 01
		self.plotar_figura(self.quadrado, 75, 50)
		self.plotar_figura(self.quadrado, 155, 50)
		self.plotar_figura(self.quadrado, 235, 50)

		#linha 02
		self.plotar_figura(self.quadrado, 75, 110)
		self.plotar_figura(self.quadrado, 155, 110)
		self.plotar_figura(self.quadrado, 235, 110)

		#linha 03 ---------------mudar a gambiarra do quadrado------------------
		q_vermelho = translacao(self.escalonar(self.quadrado,1,1),75,170)
		self.draw(q_vermelho, "red")
		self.plotar_figura(self.quadrado, 155, 170)

		#figuras no interior
		retangulo_v = self.escalonar(self.quadrado, 0.5, 1)
		retangulo_h = self.escalonar(self.quadrado, 1, 0.5)
		quadradinho = self.escalonar(self.quadrado, 0.5, 0.5)
		#linha 01
		self.draw(translacao(retangulo_v, 95, 50), "red")
		self.draw(translacao(quadradinho, 175, 50), "red")
		self.draw(translacao(quadradinho, 255, 70), "red")

		#linha 02
		self.draw(translacao(retangulo_h, 75, 130), "red")
		self.draw(translacao(quadradinho, 155, 130), "red")
		self.draw(translacao(quadradinho, 255, 130), "red")

		#linha 03
		#quadrado preenchido ao desenhar
		triangulo = translacao(self.rotacionar(self.triangulo_ret, 270), 195, 170)
		self.draw(triangulo, "red")
		
		self.cv.create_text(255,190,fill="black",font="Times 30", text="?")

		# respostas
		self.plotar_figura(self.quadrado, 30, 255)
		self.plotar_figura(self.quadrado, 115, 255)
		self.plotar_figura(self.quadrado, 195, 255)
		self.plotar_figura(self.quadrado, 280, 255)

		#a
		a = self.escalonar(self.hexagono,1,0.6)
		a = translacao(a, 60, 275)
		self.draw(a, "blue")

		#b
		self.draw(translacao(retangulo_v, 115, 255), "blue")

		#c - resposta certa
		triangulo = translacao(self.rotacionar(self.triangulo_ret, 90), 195, 295)
		self.draw(triangulo, "blue")

		#d
		d = self.escalonar(self.octogono,0.5,0.5)
		d = rotacao(d,30)
		d = translacao(d, 309, 255)
		self.draw(d, "blue")

		self.resposta_a = tk.Button(self.cv, text = 'A', width = 3, command = self.quinta_pergunta)
		self.resposta_a_window = self.cv.create_window(50, 320, window=self.resposta_a)

		self.resposta_b = tk.Button(self.cv, text = 'B', width = 3, command = self.quinta_pergunta)
		self.resposta_b_window = self.cv.create_window(135, 320, window=self.resposta_b)

		self.resposta_c = tk.Button(self.cv, text = 'C', width = 3, command = self.resposta_certa_4)
		self.resposta_c_window = self.cv.create_window(215, 320, window=self.resposta_c)

		self.resposta_d = tk.Button(self.cv, text = 'D', width = 3, command = self.quinta_pergunta)
		self.resposta_d_window = self.cv.create_window(300, 320, window=self.resposta_d)
		
		self.cv.pack(side="top", fill="both", expand=True)

	def resposta_certa_4(self):
		self.pontuacao += 1
		self.quinta_pergunta()


	
	def quinta_pergunta(self):
		self.cv.delete("all")
		self.cv.create_text(70,20,fill="blue",font="Times 15", text="Pergunta 5:")
		
		#linha 01
		self.plotar_figura(self.estrela,75,66)
		self.plotar_figura(self.seta,155,60)
		self.plotar_figura(self.casa,225,70)

		#linha 02
		self.plotar_figura(self.casa,75,130)
		self.plotar_figura(self.estrela,155,126)
		self.plotar_figura(self.seta,225,120)

		#linha 03
		self.plotar_figura(self.seta,75,180)
		self.plotar_figura(self.casa,155,190)
		self.cv.create_text(245,190,fill="black",font="Times 30", text="?")

		#respostas
		#a
		a = [self.estrela["vertices"][v] for v in self.estrela["faces"]["f1"]]
		a = reflexao_eixo(a, "x")
		a = translacao(a, 30, 290)
		self.draw(a, "blue")

		#b
		b = [self.estrela["vertices"][v] for v in self.estrela["faces"]["f1"]]
		b = translacao(b, 115, 280)
		self.draw(b, "blue")

		#c
		d = [self.seta["vertices"][v] for v in self.seta["faces"]["f1"]]
		d = translacao(d, 195, 272)
		self.draw(d, "blue")

		#d
		d = [self.casa["vertices"][v] for v in self.casa["faces"]["f1"]]
		d = reflexao_eixo(d, "x")
		d = translacao(d, 278, 280)
		self.draw(d, "blue")

		d = [self.seta["vertices"][v] for v in self.seta["faces"]["f1"]]
		d = escalonamento(rotacao(d,90), 0.7,0.7)
		d = translacao(d, 291, 290)
		self.draw(d, "blue")


		self.resposta_a = tk.Button(self.cv, text = 'A', width = 3, command = self.tela_final)
		self.resposta_a_window = self.cv.create_window(50, 320, window=self.resposta_a)

		self.resposta_b = tk.Button(self.cv, text = 'B', width = 3, command = self.resposta_certa_5)
		self.resposta_b_window = self.cv.create_window(135, 320, window=self.resposta_b)

		self.resposta_c = tk.Button(self.cv, text = 'C', width = 3, command = self.tela_final)
		self.resposta_c_window = self.cv.create_window(215, 320, window=self.resposta_c)

		self.resposta_d = tk.Button(self.cv, text = 'D', width = 3, command = self.tela_final)
		self.resposta_d_window = self.cv.create_window(300, 320, window=self.resposta_d)


		self.cv.pack(side="top", fill="both", expand=True)

	def resposta_certa_5(self):
		self.pontuacao +=1
		self.tela_final() 

	def tela_final(self): 
		self.cv.delete("all")
		self.final_time = time.time()
		self.tempo_total =  self.final_time - self.start_time
		self.cv.create_text(170,30,fill="blue",font="Helvetica 20", text="Você acertou "+str(self.pontuacao)+" pontos!")
		self.cv.create_text(170,90,fill="red",font="Helvetica 12", text="Tempo Total: "+str(round(self.tempo_total))+" segundos")

		c = isometrica(self.casa3d())
		d = isometrica_z(self.casa3d())
		p = back_face(d)
		self.desenhar_faces(self.escalonar_figura_3d(c, 2, 2), p, 135, 230)

		self.fechar = tk.Button(self.cv, text = 'Fechar', width = 7, command=self.fechar_janela)
		self.fechar_window = self.cv.create_window(170, 150, window=self.fechar)
		self.cv.pack(side="top", fill="both", expand=True)