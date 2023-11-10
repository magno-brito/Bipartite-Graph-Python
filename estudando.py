import customtkinter
from matplotlib.figure import Figure
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, Label
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTk




customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title("Magno estudando pra entender")
root.geometry("600x350")

data_addedLabel = data_addedSolucao = data_addedProblema = False


canvas1 = customtkinter.CTkCanvas(
    root, 
    width=220, 
    height=700,
    bg="#00033D"
    )
canvas1.grid(row=1, column=0)

canvas2 = customtkinter.CTkCanvas(
    root, 
    width=1200, 
    height=700,
    bg="grey"
    )
canvas2.grid(row=1, column=10)
canvas2.create_window(10,20, anchor="nw")


#-----------------------------Funções--------------------------------------

def put_canvas1(elemento, x, y):
    canvas1.create_window(x,y, anchor="nw", window=elemento)

def monstrar_problema():
    global data_addedLabel
    if not data_addedLabel:
        label = customtkinter.CTkLabel(
            root,
            font=("Arial", 30),
            bg_color="grey",
            text="Se houver empregos J e candidatos A e cada  candidato puder\n fazer alguns trabalhos, como podemos atribuir esses empregos aos\n candidatos para que o máximo de candidatos obtenha o trabalho"

        )
        canvas2.create_window(60,50, anchor="nw", window=label)
        data_addedLabel = True

def mostrarGrafo():
    global data_addedSolucao
    if not data_addedSolucao:
        # Create a standard Tkinter Frame inside canvas2 to hold the graph
        graph_frame = Frame(canvas2, bg="grey")
        graph_frame.grid(row=0, column=0, sticky="nsew")

        fig = Figure(figsize=(4, 4), dpi=50)
        ax = fig.add_subplot(111)
        ax.margins(0.11)

        G = nx.complete_graph(5)  # Replace with your desired graph creation
        pos = nx.spring_layout(G)
        nx.draw(G, pos=pos, with_labels=True, font_size=10, node_size=500, ax=ax)

        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0)  # Remove sticky="nsew"

        data_addedSolucao = True




    




def limpar_canva():
    canvas2.delete("all")
    global data_addedLabel
    global data_addedSolucao
    data_addedLabel = False
    data_addedSolucao = False



    


#-------------------------------------------------------------------


label = customtkinter.CTkLabel(
    root,
    font=("Arial", 26),
    text="Grafos Bipartidos",
    bg_color="#00033D"
)

put_canvas1(label,15,10)

botaoA = customtkinter.CTkButton(
    root, 
    width=130, 
    height=30, 
    text="Mostrar Problema",
    hover_color="green",
    command=monstrar_problema
    )

put_canvas1(botaoA,50, 80)

botaoB = customtkinter.CTkButton(
    root,
    width=130,
    height=30,
    text="Grafo Inicial",
    command=monstrar_problema,
    hover_color="green"
    )

put_canvas1(botaoB,50, 140)


botaoC = customtkinter.CTkButton(
    root, 
    width=130,
    height=30,
    text="Grafo final",
    command=mostrarGrafo,
    hover_color="green")

put_canvas1(botaoC,50, 200)


botaoD = customtkinter.CTkButton(
    root, 
    width=130,
    height=30,
    hover_color="green",
    text="Grafo Geral")

put_canvas1(botaoD,50, 260)


botaoLimpar = customtkinter.CTkButton(
    root, 
    width=130,
    height=30,
    text="Limpar",
    hover_color="green",
    command=limpar_canva)

put_canvas1(botaoLimpar,50, 620)






root.mainloop()