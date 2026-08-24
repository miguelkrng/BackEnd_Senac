class Usuario:
    def __init__ (self, nUsuario="", email="", senha=""):
        self.usuario = nUsuario
        self.email = email
        self.__senha = senha
        self.ficha = FichaPerfil()
        
    def informacoes(self):
        print("\n" + "="*35)
        print("CADASTRAR INFORMAÇÕES DA CONTA")
        print("="*35 + "\n")
        self.usuario = input("Insira seu nome de usuário: ")
        self.email = input("Insira seu email: ")
        self.__senha = int(input("Insira uma senha: "))
        self.listaU.lista.append(self.usuario)
        
    @property
    def login(self) -> bool:
        tentativas = 3
        print(f"Bem vindo {self.usuario}!! Digite sua senha para fazer login:")
        while tentativas > 0:
            senhaDigitada = int(input("> "))
            if senhaDigitada == self.__senha:
                print("Pabens! Login feito com sucesso!")
                return True
            else:
                tentativas -= 1
                print(f"Erro! Senha digitada incorreta, tente novamente (tentativas restantes: {tentativas})")
                return False
    
    def verificacao(self):
        if self.usuario == self.usuario:
            return f"Nome de usuario existente"
        
    def exibir_dados(self):
        print(f"""=== INFORMAÇÕES DA CONTA ===\n
        Nome de Usuário: {self.usuario}
        Email: {self.email}
        Senha: *******
        """)
    
    @property
    def alterar_dados(self):
        print("Escolha o que você deseja alterar nos dados da sua conta:")
        print("""
        1 - Nome de Usuário
        2 - Endereço de Email
        3 - Senha
        """)
        opcao = int(input("> "))
        match opcao:
            case 1:
                self.novoUsu = input("Digite o novo nome de usuário: ")
                self.usuario = self.novoUsu
            case 2:
                self.novoEmail = input("Digite o no endereço de Email: ")
                self.email = self.novoEmail
            case 3:
                self.novaSenha = input("Digite a nova senha: ")
                self.__senha = self.novaSenha

class FichaPerfil:
    def __init__ (self, nomeCompleto="", dataNascimento="", cpf="", endereco=""):
        self.nome = nomeCompleto
        self._nasc = dataNascimento
        self.__cpf = cpf
        self.endereco = endereco
        
    def preencher_ficha(self):
        print("\n" + "="*35)
        print("PREENCHER FICHA PESSOAL")
        print("="*35 + "\n")
        self.nome = input("Insira seu nome completo: ")
        self._nasc = input("Insira sua data de nascimento: ")
        self.__cpf = input("Digite seu cpf: ")
        self.endereco = input("Informe seu endereço: ")
        
    def exibir_ficha(self):
        print(f"""\n=== SEU PERFIL ===\n
        Nome completo: {self.nome}
        Data de Nascimento: {self._nasc}
        CPF: {self.__cpf}
        Endereço: {self.endereco}
          """)
        
    @property
    def alterar_ficha(self):
        print("Escolha o que você deseja alterar na sua ficha:")
        print("""
        1 - Nome completo
        2 - Data de nascimento
        3 - CPF
        4 - Endereço""")
        self.opcao = int(input("> "))
        match self.opcao:
            case 1:
                self.novoNome = input("Digite o novo nome: ")
                self.nome = self.novoNome
            case 2:
                self.novaData = input("Digite a nova data de nascimento: ")
                self._nasc = self.novaData
            case 3:
                self.novoCpf = input("Digite o novo CPF: ")
                self.__cpf = self.novoCpf
            case 4:
                self.novoEndereco = input("Digite o novo endereço: ")
                self.endereco = self.novoEndereco

class Menu:
    def __init__(self, opcao="", opcaoMenu=""):
        self.opcao = opcao
        self.opcaoMenu = opcaoMenu
        self.ficha = FichaPerfil()
        self.usuario = Usuario()
        
    
    def iniciar_menu_deslogado(self):
        print("Bem vindo ao sistema! Vejo que você não fez login ainda. \nO que deseja fazer?")
        print("""
        1 - Fazer cadastro
        2 - Fazer login
        3 - Sair""")
        while True:
            opcaoMenuD = int(input("\n> "))
            match opcaoMenuD:
                case 1:
                    self.usuario.informacoes()
                    self.ficha.preencher_ficha()
                    print("Cadastro feito com sucesso!")
                case 2:
                    self.usuario.login()
                    self.iniciar_menu_logado()
                case 3:
                    print("Obrigado por usar o sistema! Tchau!")
                    break
                case _:
                    print("Opção inválida! tente novamente.")
    
    def iniciar_menu_logado(self):
        print(f"Boas vindas {self.usuario.usuario}!! O que deseja fazer?")
        print("""
        1 - Exibir dados
        2 - Preencher / Editar ficha de perfil
        3 - Editar dados da conta
        4 - Logout""")
        while True:
            opcaoMenuL = int(input("Escolha uma opção (1-4): "))
            match opcaoMenuL:
                case 1:
                    self.usuario.exibir_dados()
                    self.usuario.ficha.exibir_ficha()
                case 2:
                    self.usuario.ficha.atualizar_dados_ficha()
                case 3:
                    self.usuario.alterar_dados()
                case 4:
                    print("Saindo da conta...")
                    break
                case _:
                    print("Opção inválida.")

if __name__ == "__main__":
    usuarioPrincipal = Usuario()
    menu = Menu(usuarioPrincipal)
    menu.iniciar_menu_deslogado()