import customtkinter
from matplotlib.figure import Figure
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, Label
import tkinter

customtkinter.set_appearance_mode("Dark")  # escolhe o tema (dark, light)
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x400")
root.title("Grafos bipartidos - Magno e Sofia")

data_addedLabel = data_addedSolucao = data_addedProblema = False


def login():
    print("Test")


def monstrar_problema():
    global data_addedLabel
    if not data_addedLabel:
        label = customtkinter.CTkLabel(
            master=frame,
            font=("Arial", 18),
            text="Se houver empregos J e candidatos A e cada  candidato puder\n fazer alguns trabalhos, como podemos atribuir esses empregos aos\n candidatos para que o máximo de candidatos obtenha o trabalho"
        )
        label.place(relx=0.1, rely=0.7)
        data_addedLabel = True


def mostrarGrafo():
    global data_addedSolucao
    if not data_addedSolucao:
        fig = Figure(figsize=(4, 4), dpi=50)  # Adjust the figsize to make the graph smaller
        ax = fig.add_subplot(111)
        ax.margins(0.11)

        G = nx.random_geometric_graph(20, 0.125, seed=896803)
        pos = nx.circular_layout(G)
        nx.draw(G, pos=pos, node_size=1000, with_labels=True, font_size=20, ax=ax)

        canvas = FigureCanvasTkAgg(fig, master=frame)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
        data_addedSolucao = True


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)
label = customtkinter.CTkLabel(
    master=frame,
    font=("Arial", 26),
    text="Grafos Bipartidos"
)
label.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, font=("Arial", 18), text="Problema", command=monstrar_problema)
button.place(relx=0.3, rely=0.1, anchor=tkinter.N)

button = customtkinter.CTkButton(master=frame, font=("Arial", 18), text="Antes", command=login)
button.place(relx=0.45, rely=0.1, anchor=tkinter.N)

button = customtkinter.CTkButton(master=frame, font=("Arial", 18), text="Depois", command=mostrarGrafo)
button.place(relx=0.60, rely=0.1, anchor=tkinter.N)

root.mainloop()
