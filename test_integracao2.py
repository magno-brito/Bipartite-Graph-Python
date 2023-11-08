import tkinter
import customtkinter
import networkx as nx

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from tkinter import Tk, Label
from PIL import Image, ImageTk

#sudo apt-get install python3-pil python3-pil.imagetk

#-----------------------------------------------------------------

#-----------------------------------------------------------------


root = customtkinter.CTk()
root.title("Embedding in Tk")

#call fig ax exactly once
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)


ax.margins(0.11)

#------------------------------------------------------------------
#call the graphing module
G = nx.random_geometric_graph(20, 0.125, seed=896803)
#draw the graph, note the ax=ax at the end, this is the critical part, matplotlib needs to know onto which axis the graph is drawn
#otherwise it will just draw it in the spyder backend, without a care for your other elements

nx.draw(G, pos=nx.circular_layout(G), node_size=4000, with_labels=True, font_size=20,ax=ax)


canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#------------------------------------------------------------------

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = customtkinter.CTkButton(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

root.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.