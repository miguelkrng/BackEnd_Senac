class Humano:
    """
    ser humaninho
    """
    # METODO CONSTRUTOR
    def __init__(self, nome, idade, cpf, sexo, naturalidade):
        self.nome = nome
        self.idade = idade
        self._cpf = cpf #_ -> privado
        self.sexo = sexo
        self.naturalidade = naturalidade
    # METODO DE CLASSE (AÇÃO)
    def respirar(self):
        print (f"{self.nome} está respirando !!")
    
    def andar(self, km):
        print (f"{self.nome} andou {km}km hoje ! eba")
    
    def piscar(self):
        print (f"{self.nome} piscou :O")
    
    def rolar_dadinhos(self):
        import random
        resultado = random.randint(1,20)
        print (f"{self.nome} rolou 1d20 e tirou um {resultado} :p")
    
    def fazer_aniversario(self):
        self.idade += 1
        return f"{self.nome} fez aniversário e está com {self.idade} anos!!!1!"
    
    #ENCAPSULAMENTO - priva uma variavel, protegendo ela 
    #METODO GETTER = PEGA A VARIAVEL ENCAPSULADA
    @property
    def alterar_cpf(self): 
        return self._cpf
    
    @property
    def outro_getter_cpf(self):
        cpf_int = int(self._cpf)
        return cpf_int
    
    #METODO SETTER = PERMITE A ALTERAÇÃO DA VARIAVEL
    @alterar_cpf.setter
    def cpf_setter(self, novoCpf):
        self._cpf = int(novoCpf)
        print(f"O novo cpf alterado é: {novoCpf}")
        
    def mostrar_rg(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | Cpf: {self._cpf} \nSexo: {self.sexo} | Naturalidade: {self.naturalidade}")
    
manu = Humano("Manu", 15, "123456789-66", "feminino", "Brasilia DF")
# print(Humano.__doc__)
manu.fazer_aniversario()
manu.fazer_aniversario()
# manu.mostrar_rg()
# print(manu.rolar_dadinhos())
print(manu.andar(30))