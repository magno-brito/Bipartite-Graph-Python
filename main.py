import customtkinter
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, Label
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTk
import numpy as np
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image, ImageTk




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
    bg="white"
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
            font=("Arial", 25),
            bg_color="white",
            text_color="blue",
            text="Se houver empregos J e candidatos A e cada  candidato puder\n fazer alguns trabalhos, como podemos atribuir esses empregos aos\n candidatos para que o máximo de candidatos obtenha o trabalho"

        )
        canvas2.create_window(200,10, anchor="nw", window=label)
        data_addedLabel = True

def mostrar_grafo():

    fig = Figure(figsize=(6, 6), dpi=100)
    ax = fig.add_subplot(111)
    ax.margins(0.11)

    G = nx.random_geometric_graph(20, 0.125, seed=896803)
    nx.draw(G, pos=nx.circular_layout(G), node_size=4000, with_labels=True, font_size=20,ax=ax)

    canvas_width = canvas2.winfo_width()
    canvas_height = canvas2.winfo_height()

    center_x = canvas_width // 2
    center_y = canvas_height // 2


    canvas = FigureCanvasTkAgg(fig, master=canvas2)  # A tk.DrawingArea.
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0)
    canvas2.create_window(center_x, center_y, window=canvas_widget)

def mostrar_exemplo():

    fig = Figure(figsize=(6, 6), dpi=100)
    ax = fig.add_subplot(111)
    ax.margins(0.11)
    
    B = nx.Graph()
    B.add_nodes_from([1,2,3,4], bipartite=0) # Add the node attribute "bipartite"
    B.add_nodes_from(['a','b','c'], bipartite=1)
    B.add_edges_from([(1,'a'), (1,'b'), (2,'b'), (2,'c'), (3,'c'), (4,'a')])

    # Separate by group
    l, r = nx.bipartite.sets(B)
    pos = {}

    # Update position for node from each group
    pos.update((node, (1, index)) for index, node in enumerate(l))
    pos.update((node, (2, index)) for index, node in enumerate(r))

    node_colors = ['red' if  B.nodes[node]['bipartite'] == 0 else 'blue' for node in B.nodes()]

    nx.draw(
        B, 
        node_size=2000, 
        with_labels=True, 
        font_size=20,
        ax=ax,
        node_color = node_colors,
        pos=pos)    

    canvas_width = canvas2.winfo_width()
    canvas_height = canvas2.winfo_height()

    center_x = canvas_width // 2
    center_y = canvas_height // 2


    canvas = FigureCanvasTkAgg(fig, master=canvas2)  # A tk.DrawingArea.
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0)
    canvas2.create_window(center_x, center_y, window=canvas_widget)
    
#-------------------------------------------------------------------------------

def mostra_problema_antes_solucao(arquivo):
    #-------------------------------------------------#
    f = open("archives/{}.txt".format(arquivo))
    lines = f.read().split("\n")
    vetor = list()

    for i in lines:
        vetor.append(i.split("-"))

    print(vetor)


    for i in range(0,len(vetor)):
        print(i)
        if vetor[i][1]:
            vetor[i][1] = vetor[i][1].split()


    dicionario = dict()
    for item in vetor:
        chave = item[0].strip()
        valor = item[1]
        dicionario[chave] = valor


    lista = list(dicionario.keys())



    #-------------------------------------------------#

    G = nx.Graph()
    conjunto1 = list(dicionario.keys())
    conjunto2 = list()

    vetor = list(dicionario.values())
    for i in vetor:
        for p in i:
            if p not in conjunto2:
                conjunto2.append(p)


    print(conjunto2)
    print(conjunto1)
        
    G.add_nodes_from(conjunto1, bipartite=0)
    G.add_nodes_from(conjunto2, bipartite=1)

    for key, values in dicionario.items():
        for value in values:
            print(key, values)
            G.add_edge(key, value)

    corA = "white"
    corB = "white"

    pos = nx.bipartite_layout(G, conjunto1)
    pos.update((x, y * 3.5) for x, y in pos.items() if x in conjunto2)
    pos.update((x, y * 4.5) for x, y in pos.items() if x in conjunto1)

    
    fig, ax = plt.subplots(figsize=(9, 9), dpi=100)
    ax.margins(0.11)


    for node in conjunto2:
        path = "languages/" + node.lower() + ".png"
        img = plt.imread(path)
        imgbox = OffsetImage(img, zoom=0.25)
        imgbox.image.axes = plt.gca()
        ab = AnnotationBbox(imgbox, pos[node], frameon=False)
        plt.gca().add_artist(ab)

    for node in conjunto1:
        path = "people/" + node.lower() + ".png"
        img = plt.imread(path)
        imgbox = OffsetImage(img, zoom=0.25)
        imgbox.image.axes = plt.gca()
        ab = AnnotationBbox(imgbox, pos[node], frameon=False)
        plt.gca().add_artist(ab)

    connection_colors = {
        "Python": "Blue",
        "Java" : "Green",
        "PHP" : "Red",
        "C#" : "Purple",
        "C++": "Orange",
        "Js" : "Pink"
    }   

    edge_colors = [connection_colors[dicionario[u][dicionario[u].index(v)]] for u, v in G.edges()]

    nx.draw(
        G,
        pos=pos,
        ax=ax,
        with_labels=False,
        node_size=3000,
        node_color=[corA if node in conjunto1 else corB for node in G.nodes()],
        font_size=12,
        width=1.5,
        edge_color=edge_colors
    )
    print(conjunto1)
    print(conjunto2)
    #plt.show()


    canvas_width = canvas2.winfo_width()
    canvas_height = canvas2.winfo_height()

    center_x = canvas_width // 2
    center_y = canvas_height // 2


    canvas = FigureCanvasTkAgg(fig, master=canvas2)  # A tk.DrawingArea.
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0)
    canvas2.create_window(center_x, center_y, window=canvas_widget)

#------------------------------------------------------------------------#


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
    text="Grafo Exemplo",
    command=mostrar_exemplo,
    hover_color="green"
    )

put_canvas1(botaoB,50, 140)


botaoC = customtkinter.CTkButton(
    root, 
    width=130,
    height=30,
    text="Grafo Simples",
    command= lambda:mostra_problema_antes_solucao("grafo0"),
    hover_color="green")

put_canvas1(botaoC,50, 200)


botaoD = customtkinter.CTkButton(
    root, 
    width=130,
    height=30,
    hover_color="green",
    text="Grafo Maior",
    command= lambda:mostra_problema_antes_solucao("grafo1"))

put_canvas1(botaoD,50, 260)

botaoE = customtkinter.CTkButton(
    root, 
    width=130,
    height=30,
    hover_color="green",
    text="Solução",
    command= lambda: mostra_problema_antes_solucao("grafo1")
   )

put_canvas1(botaoE,50, 320)


botaoLimpar = customtkinter.CTkButton(
    root, 
    width=130,
    height=30,
    text="Limpar",
    hover_color="green",
    command=limpar_canva)

put_canvas1(botaoLimpar,50, 620)






root.mainloop()