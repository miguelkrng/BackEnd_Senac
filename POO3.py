from abc import ABC, abstractmethod

LIMITE_VELOCIDADE_RODOVIA = 120 #Variavel global (acesso do codigo inteiro)

class Automovel:
    def __init__(self, marca, modelo, ano, velocidade_maxima):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.__velocidadeMaxima = velocidade_maxima #variavel privada -> __
        self._velocidadeAtual = 0 #variavel protegida -> _
    
    @property #Metodo getter (para acessar variaveis protegidas/privadas)
    def velocidade_maxima(self):
        return self.__velocidadeMaxima
    
    #Ações do carro (metodos de comportamento)
    def acelerar(self, incremento):
        if self._velocidadeAtual + incremento <= self.__velocidadeMaxima:
            self._velocidadeAtual += incremento
        else:
            self._velocidadeAtual = self.__velocidadeMaxima
        
        if self._velocidadeAtual > LIMITE_VELOCIDADE_RODOVIA: #Variavel global sendo acessadad internamente
            print(f"AVISO: {self.modelo} ultrapassou o limite global de {LIMITE_VELOCIDADE_RODOVIA} KM/h !!!!!!!!!")
        return f"{self.modelo} acelerou para {self._velocidadeAtual}km/h"
    
    def frear(self, decremento):
        self._velocidadeAtual = max(0, self._velocidadeAtual - decremento)
        return f"{self.modelo} reduziu para {self._velocidadeAtual}km/h"
    
    #INTERFACE
class CarroElegivelAutonomia(ABC): 
    @abstractmethod
    def carregar_bateria(self):
        pass
    
class CarroEletrico(Automovel, CarroElegivelAutonomia): #FILHO(PAI, PAIS)
    def __init__(self, marca, modelo, ano, velocidade_maxima, capacidade_bateria):
        super().__init__(marca, modelo, ano, velocidade_maxima)
        self.capacidade_bateria = capacidade_bateria
        self.__porcentagem_bateria = 100 #Atributo privado
    
    #IMPLEMENTAÇÃO DA INTERFACE (CarroElegivelAutonomia)
    def carregar_bateria(self):
        self.__porcentagem_bateria = 100
        return f"Bateria do {self.modelo} carregada em 100%"
    
    #POLIMORFISMO: Reescrever uma ação com um atributo diferente (aceleração)
    def acelerar(self, incremento):
        self.__porcentagem_bateria -= 2
        res = super().acelerar(incremento)
        return f"[SILENCIOSO] {res} (Bateria restante: {self.__porcentagem_bateria}%)"
    
    #2ª Herança
class CarroEsportivo(Automovel):
    def __init__(self, marca, modelo, ano, velocidade_maxima, tem_turbo = True):
        super().__init__(marca, modelo, ano, velocidade_maxima)
        self.tem_turbo = tem_turbo
            
    def acelerar(self, incremento):
        fator = 1.5 if self.tem_turbo else 1.0
        incremento_real = int(incremento * fator)
        res = super().acelerar(incremento_real)
        return f"[RONCO V8] {res} (ganho extra com turbo!!!!)"
        
eletrico = CarroEletrico("BYD", "Seal", 2024, velocidade_maxima=180, capacidade_bateria=90)
esportivo = CarroEsportivo("Porsche", "911 GT3", 2023, velocidade_maxima=310, tem_turbo=True)

#Teste de polimorfismo
# print(eletrico.acelerar(50))
# print(esportivo.acelerar(80))

#TEste de escopo global
# print(esportivo.acelerar(120))

#Teste de interface
# print(eletrico.carregar_bateria())