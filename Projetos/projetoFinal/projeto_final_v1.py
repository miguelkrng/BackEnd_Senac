import sqlite3 
import customtkinter as ctk

ctk.set_appearance_mode("dark")

# =====================================================================
# 1. CAMADA DE BANCO DE DADOS (SQLite3)
# =====================================================================

class Database:
    @staticmethod
    def init_db():
        with sqlite3.connect("petvet.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    @staticmethod
    def register_user(name, email, password):
        try:
            with sqlite3.connect("petvet.db") as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                    (name.strip(), email.strip().lower(), password)
                )
                conn.commit()
                return True, "Cadastro realizado com sucesso!"
        except sqlite3.IntegrityError:
            return False, "Este email já está cadastrado!"
        except Exception as e:
            return False, f"Erro inesperado: {str(e)}"

    @staticmethod
    def authenticate_user(email, password):
        with sqlite3.connect("petvet.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, name, email FROM users WHERE email = ? AND password = ?",
                (email.strip().lower(), password)
            )
            user = cursor.fetchone()
            if user:
                return True, {"id": user[0], "name": user[1], "email": user[2]}
            return False, "Email ou senha incorretos."


# =====================================================================
# 2. DEFINIÇÃO DAS PALETAS DE CORES VIBRANTES
# =====================================================================
# Adicionados "card_dark" e "card_light" para o aspecto moderno de camadas

THEMES = {
    "🌸 Rosa Pastel": {
        "primary": "#E83E8C",
        "hover": "#C8236B",
        "accent": "#FFB6C1",
        "bg_dark": "#170D13",       # Fundo mais profundo
        "card_dark": "#281721",     # Card levemente elevado (aspecto moderno)
        "bg_light": "#FFE6F0",
        "card_light": "#FFFFFF",
    },
    "🌊 Azul Mar": {
        "primary": "#0059FF",
        "hover": "#0036E6",
        "accent": "#4DB8FF",
        "bg_dark": "#090E1A",
        "card_dark": "#10192B",
        "bg_light": "#DFE8FF",
        "card_light": "#FFFFFF",
    },
    "⚡ Amarelo Elétrico": {
        "primary": "#EAB308",
        "hover": "#CA8A04",
        "accent": "#FDE68A",
        "bg_dark": "#1A1812",
        "card_dark": "#2B281E",
        "bg_light": "#FFFBEB",
        "card_light": "#FFFFFF",
    },
    "🌿 Verde Floresta": {
        "primary": "#10B981",
        "hover": "#059669",
        "accent": "#6EE7B7",
        "bg_dark": "#0B1712",
        "card_dark": "#162B22",
        "bg_light": "#ECFDF5",
        "card_light": "#FFFFFF",
    },
    "🔮 Roxo Psíquico": {
        "primary": "#8B5CF6",
        "hover": "#7C3AED",
        "accent": "#C4B5FD",
        "bg_dark": "#130F1C",
        "card_dark": "#1F1A2E",
        "bg_light": "#F5F3FF",
        "card_light": "#FFFFFF",
    },
    "🔥 Vermelho Brasa": {
        "primary": "#DA1641",
        "hover": "#960505",
        "accent": "#FD4F66",
        "bg_dark": "#170B0E",
        "card_dark": "#2B161B",
        "bg_light": "#FDECEE",
        "card_light": "#FFFFFF",
    }
}

# =====================================================================
# Aplicação Final
# =====================================================================

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        Database.init_db()
        self.title("Sistema Boxstation - Centro de jogos")
        self.geometry("1100x700")
        self.minsize(950,650)
        self.current_theme_name = "🔥 Vermelho Brasa" #tema padrão
        self.theme_data = THEMES[self.current_theme_name]
        self.current_user = None
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        #SIDEBAR 
        self.sidebar_frame = ctk.CTkFrame(self, width=280, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_columnconfigure(7, weight=1)
        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="🎮 BOXSTATION 👾", font=ctk.CTkFont(size=36, weight="bold"))
        self.logo_label.grid(row=0,column=0,padx=30,pady=(40,5))
        self.subtitle_label = ctk.CTkLabel(self.sidebar_frame, text="Centro de jogos", font=ctk.CTkFont(size=14))
        self.subtitle_label.grid(row=1,column=0,padx=30,pady=(0,40))
        
        #Seletor de paleta
        self.theme_label = ctk.CTkLabel(self.sidebar_frame, text="Paleta de cores:", font=ctk.CTkFont(size=14))
        self.theme_label.grid(row=2, column=0,padx=30, pady=(10,0), sticky="w")
        self.theme_menu = ctk.CTkOptionMenu(
            self.sidebar_frame,
            values= list(THEMES.keys()),
            command= self.on_theme_change,
            height=40,
            font= ctk.CTkFont(size=14)
        )
        self.theme_menu.grid(row=3, column=0, padx=30, pady=(5,25), sticky="ew")
        
        #Seletor de luz
        self.mode_label = ctk.CTkLabel(self.sidebar_frame, text="Modo de Luz:", font=ctk.CTkFont(size=14))
        self.mode_label.grid(row=4, column=0, padx=30, pady=(10,0), sticky="w")
        self.mode_menu = ctk.CTkOptionMenu(
            self.sidebar_frame,
            values = ["Dark", "Light", "System"],
            height = 40,
            font=ctk.CTkFont(size=14),
        )
        self.mode_menu.grid(row=5, column=0,padx=30,pady=(5,25), sticky="ew")
        
        #Container principal 
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_container.grid_columnconfigure(0, weight=1)
        self.main_container.grid_rowconfigure(0, weight=1)
        
        self.frames = {}
        self.init_frames()
        self.apply_theme_colors()
        self.show_frames("LoginFrame")

    def init_frames(self): #inicia os frames(pagina) na pagina inicial
        for FrameClass in (LoginFrame, RegisterFrame, HomePlaceHolderFrame):
            page_name = FrameClass.__name__
            frame = FrameClass(parent=self.main_container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
    
    def show_frames(self, page_name, **kwargs): #mostra o frame de acordo com o selecionado
        frame = self.frames[page_name]
        if hasattr(frame, "on_show"):
            frame.on_show(**kwargs)
        frame.tkraise()
        
    def on_theme_change(self, selected_theme):
        self.current_theme_name = selected_theme
        self.theme_data = THEMES[selected_theme]
        self.apply_theme_colors()      
        
    def on_mode_change(self, mode): #muda as cores de acordo com o tema claro ou escuro
        ctk.set_appearance_mode(mode)
        self.apply_theme_colors()
        
    def apply_theme_colors(self):
        theme = self.theme_data
        self.configure(fg_color =(theme["bg_light"], theme["bg_dark"]))
        self.sidebar_frame.configure(fg_color = (theme["card_light"], theme["card_dark"]))
        for menu in [self.theme_menu, self.mode_menu]:
            menu.configure(
                fg_color=theme["primary"],
                button_color=theme["primary"],
                button_hover_color=theme["hover"],
                dropdown_fg_color=(theme["card_light"], theme["card_dark"]),
                dropdown_hover_color=theme["primary"]
            )
        for frame in self.frames.values():
            if hasattr(frame, "apply_theme"):
                frame.apply_theme(theme)
                
#Tela de login
class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
        
        self.card = ctk.CTkFrame(self, width=480, height=550, corner_radius=20, border_width=2)
        self.card.place(relx=0.5, rely=0.5, anchor="center")
        self.card.pack_propagate(False)
        
        self.title_label = ctk.CTkLabel(self.card, text="Entrar no BoxStation", font=ctk.CTkFont(size=28, weight="bold"))
        self.title_label.pack(pady=(50,10), padx=30)
        
        self.feedback_label = ctk.CTkLabel(self.card, text="", font=ctk.CTkFont(size=14))
        self.feedback_label.pack(pady=(0,20))
        
        self.email_entry = ctk.CTkEntry(
            self.card,
            width=360,
            height=50,
            font=ctk.CTkFont(size=26),
            placeholder_text="E-mail do Usuário",
            placeholder_text_color=("gray50", "gray60")
        )
        self.email_entry.pack(pady=10,padx=30)
        
        self.senha_entry = ctk.CTkEntry(
                    self.card,
                    width=360,
                    height=50,
                    font=ctk.CTkFont(size=26),
                    placeholder_text="Senha de Acesso",
                    placeholder_text_color=("gray50", "gray60"),
                    show="*"
                )
        self.senha_entry.pack(pady=10,padx=30)
        
        self.login_btn = ctk.CTkButton(
            self.card,
            text="Entrar",
            width= 360,
            height=50,
            font = ctk.CTkFont(size=16, weight="bold"),
            command= self.handle_login
        )
        self.login_btn.pack(pady=(30,15), padx=30)
        
        self.register_btn = ctk.CTkButton(
            self.card,
            text="Não tem conta? Crie uma agora!",
            font=ctk.CTkFont(size=14),
            fg_color="transparent",
            hover_color=("gray85", "gray25"),
            command= lambda: self.controller.show_frames("RegisterFrame")
        )
        self.register_btn.pack(pady=(0,25))

    def on_show(self, **kwargs):
        self.feedback_label.configure(text="")
        self.senha_entry.delete(0,"end")
        
    def handle_login(self): #verifica o email e a senha antes de entrar
        email = self.email_entry.get().strip()
        senha = self.senha_entry.get()
        
        if not email or not senha:
            self.feedback_label.configure(text="Preencha todos os campos!", text_color="#dd1842")    
            return
        
        success, result = Database.authenticate_user(email, senha)
        if success:
            self.controller.current_user = result
            self.controller.show_frames("HomePlaceHolderFrame")
        else:
            self.feedback_label.configure(text=result, text_color="#f02641")
    
    def apply_theme(self, theme):
        self.card.configure(
            fg_color=(theme["card_light"], theme["card_dark"]),
            border_color=theme["primary"]
        )
        self.login_btn.configure(fg_color=theme["primary"], hover_color=theme["hover"])
        self.email_entry.configure(border_color=theme["accent"])
        self.senha_entry.configure(border_color=theme["accent"])
        self.register_btn.configure(text_color=theme["primary"])
    
#Tela de Cadastro
class RegisterFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
    
        self.card = ctk.CTkFrame(self, width=480, height=600, corner_radius=20, border_width=2)
        self.card.place(relx=0.5, rely=0.5, anchor="center")
        self.card.pack_propagate(False)
        
        self.title_label = ctk.CTkLabel(
            self.card,
            text="Novo Usuário",
            font= ctk.CTkFont(size=28, weight="bold")
        )
        self.title_label.pack(pady=(40,10), padx=30)
        
        self.feedback_label = ctk.CTkLabel(self.card, text="", font=ctk.CTkFont(size=14))
        self.feedback_label.pack(pady=(0, 10))
        
        self.name_entry = ctk.CTkEntry( 
            self.card, width=360, height=50, font= ctk.CTkFont(size=16),
            placeholder_text="Nome Completo", placeholder_text_color=("gray50", "gray60")
        )
        self.name_entry.pack(pady=8, padx=30)
        
        self.email_entry = ctk.CTkEntry(
            self.card, width=360, height=50, font= ctk.CTkFont(size=16),
            placeholder_text="Email de Contato", placeholder_text_color=("gray50", "gray60")
        )
        self.email_entry.pack(pady=8, padx=30)
        
        self.pass_entry = ctk.CTkEntry(
            self.card, width=360, height=50, font= ctk.CTkFont(size=16), show= "*",
            placeholder_text="Senha (mín. 4 caracteres)", placeholder_text_color=("gray50", "gray60")
        )
        self.pass_entry.pack(pady=8, padx=30)
        
        self.register_btn = ctk.CTkButton(
            self.card,
            text="Cadastrar e Salvar",
            width=360, height=55, font= ctk.CTkFont(size=16, weight="bold"),
            command = self.handle_register
        )
        self.register_btn.pack(pady=(0,20))
        
        self.back_btn = ctk.CTkButton(
            self.card,
            text="Já tenho uma conta (Voltar)",
            font= ctk.CTkFont(size=14),
            fg_color= "transparent", hover_color=("gray85", "gray25"),
            command = lambda: self.controller.show_frame("LoginFrame")
        )
        self.back_btn.pack(pady=(0,20))

    def on_show(self, **kwargs):
        self.feedback_label.configure(text="")
        self.name_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.pass_entry.delete(0, "end")
    
    def handle_register(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.pass_entry.get().strip()
        
        if not name or not email or not password:
            self.feedback_label.configure(text="Todos os campos são obrigatórios!", text_color= "#f8163c")
            return
        if len(password)<4:
            self.feedback_label.configure(text="A senha não pode ter menos de 4 caracteres!", text_color ="#f8163c")
        
        success, msg = Database.register_user(name, email, password)
        if success:
            self.controller.show_frame("LoginFrame")
            login_frame = self.controller.frames["LoginFrame"]
            login_frame.feedback_label.configure(text="Conta criada! Faça login para acessar.", text_color = "#12D494")
            login_frame.email_entry.delete(0, "end")
            login_frame.email_entry.insert(0, email)
        else:
            self.feedback_label.configure(text= msg, text_color="#f8163c")
            
    def apply_theme(self, theme):
        self.card.configure(
            fg_color=(theme["card_light"], theme["card_dark"]),
            border_color= theme["primary"],
        )
        self.register_btn.configure(fg_color= theme["primary"], hover_color = theme["hover"])
        self.name_entry.configure(border_color = theme["accent"])
        self.email_entry.configure(border_color = theme["accent"])
        self.pass_entry.configure(border_color = theme["accent"])
        self.back_btn.configure(text_color = theme["primary"])
        
#Tela Home
class HomePlaceHolderFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
            super().__init__(parent, fg_color="transparent")
            self.controller = controller
    pass

if __name__ == "__main__":
    app = App()
    app.mainloop()