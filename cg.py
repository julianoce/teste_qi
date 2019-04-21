import tkinter as tk
from interface import Interface

tempo_jogo = 60



root = tk.Tk()

main = Interface(root)

# main.primeira_pergunta()
# main.segunda_pergunta()
# main.terceira_pergunta()
main.tela_inicial()
# main.quinta_pergunta()


root.mainloop()
