import customtkinter as ctk #https://customtkinter.tomschimansky.com/
import json #https://www.w3schools.com/python/python_json.asp

win1 = ctk.CTk()
win1.title("GERENCIADOR DE TAREFAS ~ v1.0")
win1.geometry("1200x800")
win1.resizable(False, False)


    
    
def adicionar1():
    print("botão adicionar clicado!")
    win2 = ctk.CTk()
    win2.title("CONFIGURE SEU LEMBRETE ~ v1.0")
    win2.geometry("400x400")
    win2.resizable(False, False)
    def cor_selecionada1_salvar():
        etr1_variavel.get()
        win2.destroy()
        frm1 = ctk.CTkFrame()
    def cor_selecionada1():
        btn3.configure(fg_color="gray", state="disabled")
        btn4.configure(fg_color="gray", state="disabled")
        btn5.configure(fg_color="gray", state="disabled")
        btn6 = ctk.CTkButton(win2, text="salvar", command=cor_selecionada1_salvar)
        btn6.place(x=100, y=200)

    def cor_selecionada2():
        btn2.configure(fg_color="gray", state="disabled")
        btn4.configure(fg_color="gray", state="disabled")
        btn5.configure(fg_color="gray", state="disabled")
    def cor_selecionada3():
        btn2.configure(fg_color="gray", state="disabled")
        btn3.configure(fg_color="gray", state="disabled")
        btn5.configure(fg_color="gray", state="disabled")
    def cor_selecionada4():
        btn2.configure(fg_color="gray", state="disabled")
        btn3.configure(fg_color="gray", state="disabled")
        btn4.configure(fg_color="gray", state="disabled")
    
    btn2 = ctk.CTkButton(win2, text="", fg_color="#effd44", cursor="hand2", width=50,
                        height=50, hover_color="#dfea44", command=cor_selecionada1)
    btn2.place(x=10, y=10)
    
    btn3 = ctk.CTkButton(win2, text="", fg_color="#fda5e7", cursor="hand2", width=50,
                        height=50, hover_color="#dc91c9", command=cor_selecionada2)
    btn3.place(x=65,y=10)
    
    btn4 = ctk.CTkButton(win2, text="", fg_color="#e86529", cursor="hand2", width=50,
                        height=50, hover_color="#c75928", command=cor_selecionada3)
    btn4.place(x=120, y=10)
    
    btn5 = ctk.CTkButton(win2, text="", fg_color="#d9f284", cursor="hand2", width=50,
                        height=50, hover_color="#c2d878", command=cor_selecionada4)
    btn5.place(x=175, y=10)
    
    etr1_variavel= ctk.StringVar()
    etr1 = ctk.CTkEntry(win2, placeholder_text="Digite seu lembrete...", 
                        width=300, height=100, textvariable=etr1_variavel, font=("Helvica", 17, "bold"))
    etr1.place(x=10, y=75) 

btn1_font1 = ctk.CTkFont(size=35, weight="bold")
btn1 = ctk.CTkButton(win1, text="+", font=btn1_font1, fg_color="green", text_color="white",
                    hover_color="dark green", cursor="hand2", width=100, height=100,
                    command=adicionar1)
btn1.place(x=20, y=20)



def remover1():
    print("botão remover clicado!")


btn_remove = ctk.CTkButton(win1, text="-", font=btn1_font1, fg_color="red", text_color="white",
                    hover_color="dark red", cursor="hand2", width=100, height=100,
                    command=remover1)
btn_remove.place(x=140,y=20)

win1.mainloop()
