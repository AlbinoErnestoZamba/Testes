import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage

# Criando a Janela
janela = tk.Tk() 
janela.title("My app")
janela.configure(bg = "#F0F0F0")
janela.geometry("500x600")

#Fonte
fonte_topo = font.Font(family = "Garamond", size = 24, weight = "bold")
rotulo_topo = tk.Label(janela, text = "MyTarefas", font = fonte_topo, bg = "#F0F0F0", fg = "#333").pack(pady = 20)

#Campo para entrada
frame = tk.Frame(janela, bg = "#F0F0F0")
frame.pack(pady=10)
entrada_tarefa = tk.Entry(frame, font = ("Garamond", 14), relief = tk.FLAT, bg = "white", fg = "grey", width = 30)
entrada_tarefa.pack(side = tk.LEFT, padx = 10)
botao_adicionar = tk.Button(frame, text = "Adicionar Tarefa", bg = "#4CAF50", fg = "white", height = 1, width = 15, font = ("Roboto", 11))
botao_adicionar.pack(side = tk.LEFT, padx = 10)

#Criar Freme com lista e rolagem
frame_lista_tarefas = tk.Frame(janela, bg = "white")
frame_lista_tarefas.pack(fill = tk.BOTH, expand= "true", padx = 10, pady = 10)

canvas = tk.Canvas(frame_lista_tarefas, bg = "white")
canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = "true")

rolagem = ttk.Scrollbar(frame_lista_tarefas, orient = "vertical", command = canvas.yview)
rolagem.pack(side = tk.RIGHT, fill = tk.Y)

canvas.configure(yscrollcommand = rolagem.set)
canvas_interior = tk.Frame(canvas, bg = "white")
canvas.create_window((0, 0), window = canvas_interior, anchor = "nw")
def ajustar_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas_interior.bind("<Configure>", ajustar_scrollregion)
# Aqui em cima você pode adicionar o restante da sua interface gráfica, como widgets, etc.
janela.mainloop()
