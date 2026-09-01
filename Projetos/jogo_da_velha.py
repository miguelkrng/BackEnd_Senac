import customtkinter as ctk
from tkinter import messagebox
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class BatalhaNaval(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.titulo = "Batalha Naval dos Auras+++"
        self.resizable(False, False)
        self.tamanho = 6
        self.totalNavios = 4
        self.tentativas = 0
        self.acertos = 0
        self.navios = set()
        self.botoes = {}
        self.criar_interface()
        self.novo_jogo()
        
    def criar_interface(self):
        self.etiqueta_titulo = ctk.CTkLabel(self, text="🚢 Batalha Naval ⚓", font= ctk.CTkFont(size=32, weight="bold"))
        self.etiqueta_titulo.pack(pady=(25,10))
        #Frame de status
        self.frame_status = ctk.CTkFrame(self, corner_radius=12)
        self.frame_status.pack(pady=10, padx=40, fill="x")
        self.etiqueta_navios = ctk.CTkLabel(self.frame_status, text=f"Navios restantes = {self.totalNavios}", font= ctk.CTkFont(size=18, weight="bold"))
        self.etiqueta_navios.pack(pady=12, padx=25, side="left")
        self.etiqueta_tentativas = ctk.CTkLabel(self.frame_status, text="Tentativas = 0", font= ctk.CTkFont(size=18, weight="bold"))
        self.etiqueta_tentativas.pack(side="right", padx=25, pady=12)
        #Frame do Tabuleiro 
        self.frame_tabuleiro = ctk.CTkFrame(self, corner_radius=15)
        self.frame_tabuleiro.pack(pady=20, padx=30)
        for r in range(self.tamanho):
            for c in range(self.tamanho):
                btn = ctk.CTkButton(
                    self.frame_tabuleiro,
                    text="~",
                    width=80,
                    height=80,
                    font= ctk.CTkFont(size=26, weight="bold"),
                    fg_color= "#cc0808",
                    hover_color= "#ec5a5a",
                    command = lambda row=r, col=c: self.atirar(row, col)
                )
                btn.grid(row=r, column=c, padx=5, pady=5)
                self.botoes[(r,c)]=btn
                
        self.btn_reiniciar = ctk.CTkButton(
            self,
            text="Novo jogo",
            width=220,
            height=50,
            corner_radius=10,
            font= ctk.CTkFont(size=18, weight="bold"),
            fg_color= "#242424",
            hover_color= "#585858",
            command= self.novo_jogo
        )
        self.btn_reiniciar.pack(pady=20)
        
    def novo_jogo(self):
        self.tentativas = 0
        self.acertos = 0
        self.navios.clear()
        
        while len(self.navios) < self.totalNavios:
            pos = (random.randint(0, self.tamanho - 1)), random.randint(0, self.tamanho - 1)
            self.navios.add(pos)
        for(r,c), btn in self.botoes.items():
            btn.configure(text="~", state="normal", fg_color="#1958ce", hover_color="#0d4abd")
        self.atualizar_status()
        
    def atualizar_status(self):
        restantes = self.totalNavios - self.acertos
        self.etiqueta_navios.configure(text=f"Navios restantes: {restantes}")
        self.etiqueta_tentativas.configure(text=f"Tentativas restantes: {self.tentativas}")
    
    def atirar(self, row, col):
        btn = self.botoes[(row,col)]
        self.tentativas += 1
        if (row, col)in self.navios:
            self.acertos += 1
            btn.configure(text="💥", fg_color="#d80b4f", hover_color="#ad053d", state="disabled")
        else:
            btn.configure(text="🌊", fg_color="#0b64d8", hover_color="#0350c5", state="disabled")
        self.atualizar_status()
        
        if self.acertos == self.totalNavios:
            messagebox.showinfo(
                "VENCEMOOOOOO !!!!!!!!!",
                f"Pabens, você destruiu todos os navios em {self.tentativas} disparos!"
            )
            for b in self.botoes.values():
                b.configure(state="disabled")
        
if __name__ == "__main__":
    app=BatalhaNaval()
    app.mainloop()