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
    btn2 = ctk.CTkButton(win2, text="", fg_color="#effd44", cursor="hand2", width=50,
                        height=50, hover_color="#dfea44", command=None)
    btn2.place(x=10, y=10)
    btn3 = ctk.CTkButton(win2, text="", fg_color="#fda5e7", cursor="hand2", width=50,
                        height=50, hover_color="#dc91c9", command=None)
    btn3.place(x=65,y=10)
    btn4 = ctk.CTkButton(win2, text="", fg_color="#e86529", cursor="hand2", width=50,
                        height=50, hover_color="#c75928", command=None)
    btn4.place(x=120, y=10)
    btn5 = ctk.CTkButton(win2, text="", fg_color="#d9f284", cursor="hand2", width=50,
                        height=50, hover_color="#c2d878", command=None)
    btn5.place(x=175, y=10)
    etr1_variavel= ctk.StringVar()
    etr1 = ctk.CTkEntry(win2, placeholder_text="Digite seu lembrete...", 
                        width=300, height=100, textvariable=etr1_variavel)
    etr1.place(x=10, y=75)

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
    lbl1_font1 = ctk.CTkFont(weight="bold", size=23)
    lbl1 = ctk.CTkLabel(win3, text="Salvar e sair?", font=lbl1_font1).pack()
    def sair():
        pass
    btn2 = ctk.CTkButton()

"""
btn_quit_font1 = ctk.CTkFont(weight="bold")
btn_quit1 = ctk.CTkButton(win, text="Sair", font=btn_quit_font1)

"""

win.mainloop()
