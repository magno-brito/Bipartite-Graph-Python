import customtkinter 

customtkinter.set_appearance_mode("Dark") #escolhe o tema (dark, light)
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x400")

def login():
    print("Test")

def monstrar_problema():
    label = customtkinter.CTkLabel(
    master=frame, 
    font=("Arial",18),
    text= "Se houver empregos J e candidatos A e cada  candidato puder\n fazer alguns trabalhos, como podemos atribuir esses empregos aos\n candidatos para que o máximo de candidatos obtenha o trabalho"
    )
    label.pack(pady=24, padx=10)
    

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)
label = customtkinter.CTkLabel(
    master=frame, 
    font=("Arial",26),
    text="Grafos Bipartidos"
    )
label.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame,font=("Arial",18), text="Problema", command=monstrar_problema)
button.pack(pady=10,padx=10)

button = customtkinter.CTkButton(master=frame, font=("Arial",18),text="Antes", command=login)
button.pack(pady=10,padx=10)

button = customtkinter.CTkButton(master=frame,font=("Arial",18), text="Depois", command=login)
button.pack(pady=12,padx=0)

root.mainloop()
