import tkinter as tk
from interface import Interface


root = tk.Tk()

main = Interface(root)

# main.primeira_pergunta()
# main.segunda_pergunta()
# main.terceira_pergunta()
main.tela_inicial()
# main.quinta_pergunta()

root.mainloop()
