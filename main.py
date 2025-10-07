import customtkinter as ctk  # https://customtkinter.tomschimansky.com/
import json
import os

win1 = ctk.CTk()
win1.title("GERENCIADOR DE TAREFAS ~ v1.0")
win1.geometry("1200x800")
win1.resizable(False, False)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

ARQUIVO_TAREFAS = "tarefas.json"

# Se o arquivo não existir, cria um vazio
if not os.path.exists(ARQUIVO_TAREFAS):
    with open(ARQUIVO_TAREFAS, "w") as f:
        json.dump([], f)

def salvar_tarefas(lista_tarefas):
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:
        json.dump(lista_tarefas, f, indent=4, ensure_ascii=False)

def carregar_tarefas():
    try:
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

tarefas = carregar_tarefas()


frm_tarefas = ctk.CTkScrollableFrame(win1, width=1100, height=650)
frm_tarefas.place(x=50, y=150)

def atualizar_interface():
    for widget in frm_tarefas.winfo_children():
        widget.destroy()

    for i, tarefa in enumerate(tarefas):
        cor = tarefa.get("cor", "#3a3a3a")
        texto = tarefa.get("texto", "")

        frm = ctk.CTkFrame(frm_tarefas, fg_color=cor, corner_radius=12)
        frm.pack(fill="x", padx=10, pady=8)

        lbl = ctk.CTkLabel(frm, text=texto, font=("Helvetica", 18, "bold"), anchor="w")
        lbl.pack(side="left", padx=10, pady=10, expand=True, fill="x")

        btn_concluir = ctk.CTkButton(frm, text="✔", width=40, fg_color="green",
                                     hover_color="darkgreen", command=lambda i=i: concluir_tarefa(i))
        btn_concluir.pack(side="right", padx=5)

        btn_excluir = ctk.CTkButton(frm, text="✖", width=40, fg_color="red",
                                    hover_color="darkred", command=lambda i=i: remover_tarefa(i))
        btn_excluir.pack(side="right", padx=5)


def concluir_tarefa(i):
    tarefas[i]["texto"] = "✅ " + tarefas[i]["texto"]
    salvar_tarefas(tarefas)
    atualizar_interface()

def remover_tarefa(i):
    del tarefas[i]
    salvar_tarefas(tarefas)
    atualizar_interface()

def adicionar1():
    win2 = ctk.CTkToplevel(win1)
    win2.title("CONFIGURE SEU LEMBRETE ~ v1.0")
    win2.geometry("400x400")
    win2.resizable(False, False)

    etr1_variavel = ctk.StringVar()
    cor_escolhida = {"valor": "#3a3a3a"}

    def salvar_lembrete():
        texto = etr1_variavel.get().strip()
        if texto:
            nova_tarefa = {"texto": texto, "cor": cor_escolhida["valor"]}
            tarefas.append(nova_tarefa)
            salvar_tarefas(tarefas)
            atualizar_interface()
        win2.destroy()

    def escolher_cor(cor):
        cor_escolhida["valor"] = cor
        btn_salvar.configure(state="normal", fg_color="green")

    cores = ["#effd44", "#fda5e7", "#e86529", "#d9f284"]
    x = 10
    for cor in cores:
        ctk.CTkButton(win2, text="", fg_color=cor, width=50, height=50,
                      command=lambda c=cor: escolher_cor(c)).place(x=x, y=10)
        x += 55

    etr1 = ctk.CTkEntry(win2, placeholder_text="Digite seu lembrete...",
                        width=300, height=100, textvariable=etr1_variavel,
                        font=("Helvetica", 17, "bold"))
    etr1.place(x=10, y=100)

    btn_salvar = ctk.CTkButton(win2, text="Salvar", command=salvar_lembrete,
                               width=100, height=40, state="disabled")
    btn_salvar.place(x=150, y=250)


btn_font = ctk.CTkFont(size=35, weight="bold")

btn_add = ctk.CTkButton(win1, text="+", font=btn_font, fg_color="green", text_color="white",
                        hover_color="darkgreen", cursor="hand2", width=100, height=100,
                        command=adicionar1)
btn_add.place(x=20, y=20)

btn_remove_all = ctk.CTkButton(win1, text="-", font=btn_font, fg_color="red", text_color="white",
                               hover_color="darkred", cursor="hand2", width=100, height=100,
                               command=lambda: [tarefas.clear(), salvar_tarefas(tarefas), atualizar_interface()])
btn_remove_all.place(x=140, y=20)

atualizar_interface()

win1.mainloop()
