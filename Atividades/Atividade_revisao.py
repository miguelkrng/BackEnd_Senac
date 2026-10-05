import customtkinter as ctk
# ctk.set_appearance_mode("Dark")


# class Contador_app(ctk.CTk):
    
#     def __init__(self):
#         super().__init__()
#         self.contador = 0 
#         self.title("Contador") 
#         self.geometry('400x320') 
#         self.resizable(False, False)
#         self.contador_label = ctk.CTkLabel(self, text=str(self.contador))
#         self.contador_label.pack(padx = 13, pady = 22)
#         aumentar_btn = ctk.CTkButton(self, text="+1 no contador", fg_color="#30cc7e", hover_color="#25a771", width=150, height=40, command= self.aumentar_contador)
#         diminuir_btn = ctk.CTkButton(self, text="-1 no contador", fg_color="#cc3057", hover_color="#a7253b", width=150, height=40, command= self.diminuir_contador)
#         aumentar_btn.pack(padx=10, pady=(15,10))
#         diminuir_btn.pack(padx=10, pady=(15,10))
        
#     def aumentar_contador(self):

#         self.contador += 1
#         self.contador_label.configure(text=str(self.contador))

#     def diminuir_contador(self):
#         if self.contador > 0:
#             self.contador -= 1 
#         self.contador_label.configure(text=str(self.contador))


# if __name__ == "__main__":
#     app = Contador_app()
#     app.mainloop()
    
# =====================================================================================

# class App_verificar_numero(ctk.CTk):
#     def __init__(self):
#         super().__init__()
        
#         self.title("Verificador") 
#         self.geometry('400x520') 
#         self.resizable(False, False)
        
#         self.numero_label = ctk.CTkLabel(self, text="Informe um número ", text_color="#000000")
#         self.numero_label.pack(padx = 13, pady = 22)
#         self.numero_entry = ctk.CTkEntry(self, placeholder_text="Ex: 120", width=360, height=50,)
#         self.numero_entry.pack(pady=10,padx=30)
#         self.verificar_btn = ctk.CTkButton(self, text="Verificar número", command = self.verificar_numero)
#         self.verificar_btn.pack(padx=10, pady=(15,10))
        
#     def verificar_numero(self):
#         self.numero_get = self.numero_entry.get()
#         try:
#             self.numero_float = float(self.numero_get)
#             self.numero_label.configure(text="Número aceito!", text_color="#23da84")
#         except ValueError:
#             self.numero_label.configure(text="Digite um número!!", text_color="#d80f3a")
            
# if __name__ == "__main__":
#     app = App_verificar_numero()
#     app.mainloop()

# ===========================================================

# ctk.set_appearance_mode("Dark")

# class CardUsuario(ctk.CTkFrame):
#     def __init__(self, master, nome, **kwargs):
#         super().__init__(master, **kwargs)

#         self.nome = nome

#         self.lbl_nome = ctk.CTkLabel(self, text=f"Usuário: {self.nome}", font=("Arial", 14))
#         self.lbl_nome.pack(side="left", padx=15, pady=10)

#         self.btn_remover = ctk.CTkButton(
#             self, 
#             text="Remover", 
#             fg_color="#EF446F", 
#             hover_color="#B91C43",
#             width=80,
#             command=self.destroy
#         )
#         self.btn_remover.pack(side="right", padx=15, pady=10)


# class AppPrincipal(ctk.CTk):

#     def __init__(self):
#         super().__init__()

#         self.title("Exercício 3 - Card Usuário")
#         self.geometry("400x250")

#         self.card1 = CardUsuario(self, nome="Ana Alice")
#         self.card1.pack(fill="x", padx=20, pady=10)

#         self.card2 = CardUsuario(self, nome="Fernanda Coxta")
#         self.card2.pack(fill="x", padx=20, pady=10)

# if __name__ == "__main__":
#     app = AppPrincipal()
#     app.mainloop()
    
# ============================================================================

# ctk.set_appearance_mode("Dark")

# class App_termos(ctk.CTk):
#     def __init__(self):
#         super().__init__()

#         self.title("Leit")
#         self.geometry("350x220")
#         self.resizable(False, False)

#         # Variável booleana reativa
#         self.var_aceito = ctk.BooleanVar(value=False)

#         self.chk_termos = ctk.CTkCheckBox(
#             self, 
#             text="Aceito os termos", 
#             variable=self.var_aceito
#         )
#         self.chk_termos.pack(pady=(30, 15))

#         self.btn_enviar = ctk.CTkButton(self, text="Enviar", command=self.validar_termos)
#         self.btn_enviar.pack(pady=10)

#         self.lbl_status = ctk.CTkLabel(self, text="", font=("Arial", 14, "bold"))
#         self.lbl_status.pack(pady=10)

#     def validar_termos(self):
#         if self.var_aceito.get():
#             self.lbl_status.configure(text="Acesso liberado!!!! :D", text_color="#10B981")  # Verde
#         else:
#             self.lbl_status.configure(text="Aceite os termos primeiro!", text_color="#EF4444")  # Vermelho

# if __name__ == "__main__":
#     app = App_termos()
#     app.mainloop()
    
# ==========================================================================================

ctk.set_appearance_mode("Dark")

class AppLista(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Lista")
        self.geometry("400x450")
        self.frame_topo = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_topo.pack(fill="x", padx=20, pady=(20, 10))

        self.entry_item = ctk.CTkEntry(self.frame_topo, placeholder_text="Digite um item...")
        self.entry_item.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.btn_adicionar = ctk.CTkButton(self.frame_topo, text="Adicionar", command=self.adicionar_item)
        self.btn_adicionar.pack(side="right")

        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="Itens Cadastrados")
        self.scroll_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    def adicionar_item(self):
        texto = self.entry_item.get().strip()

        if texto:
            novo_label = ctk.CTkLabel(self.scroll_frame, text=f"• {texto}", anchor="w", font=("Arial", 13))
            novo_label.pack(fill="x", padx=10, pady=5)

            self.entry_item.delete(0, "end")

if __name__ == "__main__":
    app = AppLista()
    app.mainloop()