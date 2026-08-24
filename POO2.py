class Usuario:
    def __init__(self, usuario, email, senha):
        self.email = email
        self.senha = senha
        self.usuario = usuario
        
    def exibir_perfil(self):
        print(f"O usuário {self.usuario} tem o email: {self.email} e a senha: ******")
        
    def email(self):
        return self.email
        
    def verificar_senha(self, senhaDigitada):
        return self.senha == senhaDigitada 
        
    def login(self):
        print("Fazendo login...")
        print(f"Bem vindo {self.usuario}!!")
    
class Cliente(Usuario):
    def __init__(self, usuario, email, senha, saldoInicial = 0.0):
        super().__init__(usuario, email, senha)
        self.__saldo = saldoInicial
        self.compras = []
        
    @property
    def saldo(self):
        return f"R$ {self.__saldo:.2f}"
    
    def realizar_compra(self, item, valorItem):
        if self.__saldo >= valorItem:
            self.__saldo -= valorItem
            self.compras.append(item)
            return f"Compra de '{item}' (R$ {valorItem:.2f}) realizada com sucesso!"
        return f"Saldo insuficiente para comprar '{item}'."
    
    def Checar_saldo(self):
        return f"O saldo atual do cliente {self.usuario} é de: R${self.__saldo}"
        
class Admin(Usuario):
    def __init__(self, usuario, email, senha, nivelAcesso):
        super().__init__(usuario, email, senha)
        self.acesso = nivelAcesso
        
    def banir_usuario(self, usuarioAlvo):
        return f"O admin {self.nome} (Nível {self.acesso}) baniu o usuário {usuarioAlvo.nome}"
    
    def exibir_perfil(self):
        basePerfil = super().exibir_perfil()
        return f"{basePerfil} | Função: Administrador (Nível {self.acesso})"
        
Krng = Usuario("miguelkrng", "miguel@gmail.com", 123456)
cliente1 = Cliente("Fernandanãobanho", "fernandinha157@gmail.com", "123450", saldoInicial=500.00)
print(cliente1.realizar_compra("pelucia da emanuelle", 99.00))
print(cliente1.Checar_saldo())