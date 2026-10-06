
# contador = 0
# print (contador)

# def aumentar_contador():
#     global contador
#     contador += 1

# def diminuir_contador():
#     global contador
#     contador -= 1 

# aumentar_contador()
# print(contador)
import customtkinter as ctk
ctk.set_appearance_mode("dark")

# class AppLogin(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         self.title("Acesso ao Sistema")
#         self.geometry("400x350")
#         self.label = ctk.CTkLabel(self, text="Login de Usuário")
#         self.label.pack(padx=10,  pady=5)
#         self.feedback_label = ctk.CTkLabel(self, text="")
#         self.feedback_label.pack(pady=8)
#         self.usu_entry = ctk.CTkEntry(self, placeholder_text="Digite seu usuário")
#         self.usu_entry.pack(pady=8)
#         self.senha_entry = ctk.CTkEntry(self, placeholder_text="Digite sua senha", show="*")
#         self.senha_entry.pack(pady=8)
#         self.login_btn = ctk.CTkButton(self, text="Entrar", width=300, height=50, command=self.autenticar)
#         self.login_btn.pack(pady=(25, 12))

#     def autenticar(self):
#         user = self.usu_entry.get().strip()
#         senha = self.senha_entry.get()

#         if user == "admin" and senha == "1234":
#             self.feedback_label.configure(text="Acesso permitido!", text_color="#44EFC4")
#         else:
#             self.feedback_label.configure(text="Usuário ou Senha incorretos.", text_color="#EF4F44")

# if __name__ == "__main__":
#     app = AppLogin()
#     app.mainloop()

# ==============================================

# import customtkinter as ctk
# ctk.set_appearance_mode("dark")

# class SidebarFrame(ctk.CTkFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__()
#         self.titulo =  ctk.CTkLabel(self, text="Menu principal", font=ctk.CTkFont(size=20, weight="bold"))
#         self.titulo.grid(row=0, column= 0, padx=20, pady=25)

#         self.dash_btn = ctk.CTkButton(self, text="Dashboard 📶", height=42, corner_radius=10, fg_color= "transparent", text_color="gray70")
#         self.dash_btn.grid(row=1, column=0, padx=15, pady=5)
#         self.rel_btn = ctk.CTkButton(self, text="Relatórios 📋", height=42, corner_radius=10, fg_color= "transparent", text_color="gray70")
#         self.rel_btn.grid(row=2, column=0, padx=15, pady=5)
#         self.config_btn = ctk.CTkButton(self, text="Configurações ⚙️", height=42, corner_radius=10, fg_color= "transparent", text_color="gray70")
#         self.config_btn.grid(row=3, column=0, padx=15, pady=5)

# class App(ctk.CTk):
    # def __init__(self):
    #     super().__init__()
#         self.sidebar = SidebarFrame
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# ======================================================

class AppConversor(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Conversor de Temperatura")
        self.geometry("350x250")
        self.resizable(False, False)
        self.celsius_entry = ctk.CTkEntry(self, placeholder_text="Digite uma temperatura em celsius (Ex: 30)", width=260)
        self.celsius_entry.pack(padx=5, pady=30)
        self.converter_btn = ctk.CTkButton(self, text="Converter para Fahrenheit", height=30, command = self.converter_temperatura)
        self.converter_btn.pack(pady=5)
        self.resultado_label = ctk.CTkLabel(self, text="")
        self.resultado_label.pack(pady=8)
        
    def converter_temperatura(self):
        Celsius = self.celsius_entry.get().strip()
        try:
            C = int(Celsius)
            resultado = (C*1.8)+32
            self.resultado_label.configure(text=f"Resultado: {resultado} ºF", text_color="white")
        except ValueError:
            self.resultado_label.configure(text=f"Entrada inválida! Digite um número.", text_color="#e71313")

if __name__ == "__main__":
    app = AppConversor()
    app.mainloop()