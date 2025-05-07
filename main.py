#code in progress


import customtkinter as ctk #https://customtkinter.tomschimansky.com/
import json #https://www.w3schools.com/python/python_json.asp
from PIL import Image

win = ctk.CTk()
win.title("GERENCIADOR DE TAREFAS ~ v1.0 ")
win.geometry("1200x800")
win.resizable(False,False)

def adicionar1():
    print("botão adicionar clicado!")
    win2 = ctk.CTk()
    win2.title("CONFGURE SEUS LEMBRETES")
    win2.geometry("400x400")
    win2.resizable(False, False)
    btn2_font1 = ctk.CTkFont(weight="bold")
    btn2 = ctk.CTkButton(win2, text="", fg_color="#effd44", cursor="hand2", width=50,
                        height=50, hover_color="#dfea44", command=None)
    btn2.place(x=10, y=10)
    btn3 = ctk.CTkButton(win2, text="", fg_color="#fda5e7", cursor="hand2", width=50,
                        height=50, hover_color="#dc91c9", command=None)
    btn3.place(y=10, x=65)

btn1_font1 = ctk.CTkFont(size=35, weight="bold")
btn1 = ctk.CTkButton(win, text="+", font=btn1_font1, fg_color="green", text_color="white",
                    hover_color="dark green", cursor="hand2", width=100, height=100,
                    command=adicionar1)
btn1.place(x=20, y=20)

def remover1():
    print("botão remover clicado!")


btn_remove = ctk.CTkButton(win, text="-", font=btn1_font1, fg_color="red", text_color="white",
                    hover_color="dark red", cursor="hand2", width=100, height=100,
                    command=remover1)
btn_remove.place(x=140,y=20)

def sair():
    win3 = ctk.CTk()
    win3.title("Deseja realmente sair?")
    win3.resizable(False, False)
    win3.geometry("300x300")
    

image1 = ctk.CTkImage(Image.open("listadetarefas/assents/quit-icon.png"), size=(100, 100))
btn_quit = ctk.CTkButton(win, text="", image=image1, fg_color="transparent", hover=False, 
                        cursor="hand2", command=sair)
btn_quit.place(x=1070, y=20)


win.mainloop()
