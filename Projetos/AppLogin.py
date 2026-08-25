import customtkinter as ctk # `as ctk` chama o customtkinter por ctk
# CTK tem que ser chamado pra tudo que for visual


# CONFIGURAÇÕES DE APARÊNCIA
ctk.set_appearance_mode('dark') #modo de exibição
ctk.set_default_color_theme('blue')

# FUNÇÕES
def validar_login():
    usuario = campo_usuario.get().strip()
    senha = campo_senha.get().strip()
    if usuario == "cleyton" and senha == "eba123":
        resultado_login.configure(text = "")
        abrir_tela_home(usuario)
    else:
        resultado_login.configure(text = "Usuário ou senha incorretos", text_color = "#fa066c")

def abrir_tela_home(nome_usuario):
    frame_login.pack_forget()
    etiqueta_boas_vindas.configure(text=f"Bem vindo(a), {nome_usuario.capitalize()}!")
    frame_home.pack(fill = "both", expand = True, padx = 20, pady = 20)
    
def salvar_cadastro():
    nome = campo_nome.get().strip()
    email = campo_email.get().strip()
    endereco = campo_endereco.get().strip()
    if not nome or not email or not endereco:
        status_cadastro.configure(text="Preencha todos os campos!", text_color="#df2f2f")
        return
    status_cadastro.configure(text=f"Dados de {nome} salvos com sucesso!", text_color="#ffffff")
    campo_nome.delete(0, 'end')
    campo_email.delete(0, 'end')
    campo_endereco.delete(0, 'end')

def deslogar():
    campo_usuario.delete(0, 'end')
    campo_senha.delete(0, 'end')
    resultado_login.configure(text="")
    frame_home.pack_forget()
    frame_login.pack(fill="both", expand=True, padx=20, pady=20)

#  TELA PRINCIPAL
aparencia = ctk.CTk()
aparencia.title("Sistema de Gestão") #título da janela
aparencia.geometry('400x520') #tamanho da janela
aparencia.resizable(False, False)

# TELA DE LOGIN
frame_login = ctk.CTkFrame(aparencia)
frame_login.pack(fill = "both", expand = True, padx = 20, pady = 20)
ctk.CTkLabel(frame_login, text="Acesso ao sistema", font=("Segoe UI", 20, "bold")).pack(pady=(30, 20))

# label/etiqueta
etiqueta_usuario = ctk.CTkLabel(frame_login, text = "Usuário ou E-mail:")
etiqueta_usuario.pack(anchor="w", padx=30, pady=(5,0)) #define questões de aparencia da etiqueta

# entry/entrada/campo # placeholder/segura lugar
campo_usuario = ctk.CTkEntry(frame_login, width = 280, height= 30,placeholder_text="Digite o seu Usuário ou E-mail")
campo_usuario.pack(pady = 5)

# SENHA
etiqueta_senha = ctk.CTkLabel(frame_login, text = "Senha:")
etiqueta_senha.pack(anchor="w", padx=30, pady=(5,0)) 
campo_senha = ctk.CTkEntry(frame_login, width = 280, height= 30,placeholder_text="Digite a sua senha numérica", show = '*')
campo_senha.pack(pady = 5)

# button/butão
botao_login = ctk.CTkButton(frame_login, fg_color="#9330cc", hover_color="#ac5adb", text = "Login", width=150, height=40, command = validar_login)
botao_login.pack(pady = (20,10))
resultado_login = ctk.CTkLabel(frame_login, text=" ", font=("Segoe UI", 12))
resultado_login.pack(pady = 10)

#TELA HOME
frame_home = ctk.CTkFrame(aparencia)

etiqueta_boas_vindas = ctk.CTkLabel(frame_home, text=" ", font=("Segoi UI", 18, "bold"))
etiqueta_boas_vindas.pack(pady=(15,10))

ctk.CTkLabel(frame_home, text="Cadastro/Edição de informações", font=("Segoi UI", 14)).pack(pady=(0,15))

campo_nome = ctk.CTkEntry(frame_home, placeholder_text="Nome completo", width=180)
campo_nome.pack(pady=6)
campo_email = ctk.CTkEntry(frame_home, placeholder_text="Email principal", width=180)
campo_email.pack(pady=6)
campo_endereco = ctk.CTkEntry(frame_home, placeholder_text="Endereço principal", width=180)
campo_endereco.pack(pady=6)
botao_salvar = ctk.CTkButton(frame_home, text="Salvar", fg_color="#9330CC",hover_color="#AC5ADB", width=150, height=40, command= salvar_cadastro)
botao_salvar.pack(pady=(15,5))

status_cadastro = ctk.CTkLabel(frame_home, text=" ", font=("Segoi UI", 15))
status_cadastro.pack(pady=5)

botao_sair = ctk.CTkButton(frame_home, text="Log-out", fg_color="#1d1d1c", hover_color="#474747", command=deslogar, width=150, height=40)
botao_sair.pack(pady=5)

# INICIO DA APLICAÇÃO
aparencia.mainloop()