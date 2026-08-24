import customtkinter as ctk # `as ctk` chama o customtkinter por ctk
# CTK tem que ser chamado pra tudo que for visual


# CONFIGURAÇÕES DE APARÊNCIA
ctk.set_appearance_mode('dark') #modo de exibição

# FUNÇÕES
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    if usuario == "cleyton" and senha == "eba123":
        resultado_login.configure(text = "login efetuado com sucesso!", text_color = "#03fc94")
    else:
        resultado_login.configure(text = "login incorreto D:", text_color = "#fa0612")

#  TELA PRINCIPAL
aparencia = ctk.CTk()
aparencia.title("Sistema de Login") #título da janela
aparencia.geometry('300x300') #tamanho da janela

#  CAMPOS DA TELA

# label/etiqueta
etiqueta_usuario = ctk.CTkLabel(aparencia, text = "Usuário ou E-mail:")
etiqueta_usuario.pack(pady = 10) #define questões de aparencia da etiqueta

# entry/entrada/campo # placeholder/segura lugar
campo_usuario = ctk.CTkEntry(aparencia, width = 200, height= 30,placeholder_text="Digite o seu Usuário ou E-mail...")
campo_usuario.pack(pady = 5)

# SENHA
etiqueta_senha = ctk.CTkLabel(aparencia, text = "Senha:")
etiqueta_senha.pack(pady = 10) 
campo_senha = ctk.CTkEntry(aparencia, width = 200, height= 30,placeholder_text="Digite a sua senha...", show = '*')
campo_senha.pack(pady = 5)

# button/butão
botao_login = ctk.CTkButton(aparencia, text = "Login", command = validar_login)
botao_login.pack(pady = 5)
resultado_login = ctk.CTkLabel(aparencia, text=" ")
resultado_login.pack(pady = 10)


# INICIO DA APLICAÇÃO
aparencia.mainloop()