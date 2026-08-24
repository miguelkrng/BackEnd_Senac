# EXERCICIO 1

nome = "Migs"
idade = 16
altura = 1.69
# print(f"Olá, meu nome é {nome}. Eu tenho {idade} anos e minha altura é {altura}cm")

# EXERCICIO 2

# num1 = int(input("ei me fala 1 número aí "))
# num2 = int(input("agora me fala outro "))
# print(f"{num1} + {num2} = " (num1 + num2))

# EXERCICIO 3

# print("= GÊNIO DA IDADE =")
# print("Me informe sua idade e eu digo se você é de maior ou não !!!")
# idade = int(input("Qual a sua idade (Apenas números)? "))
# if idade <= 18:
#     print("Você é maior de idade !!!!")
# else:
#     print("Você é menor de idade !!!!")
    
# EXERCICIO 4

# for numero in range(2, 21, 2):
#     print(numero)

# EXERCICIO 5

# senha = "python"
# palpite = str
# while palpite != senha:
#     palpite = input("Tente adivinhar a palavra secreta! ")
# print("Parabéns, você acertou!!!!!")

# EXERCICIO 6

frutas = ["Banana", "Limão", "Uva", "Goiaba", "Pêssego"]
frutas.append("Mamão")
frutas[0] = ("Morango")
# print(frutas)

# EXERCICIO 7

produto = {
    'nome':"Caderno",
    'preco': 17.99,
    'estoque': 20
}
produto['preco'] = 27.99
# print(f"Estoque atual de cadernos na loja: {produto['estoque']}")

# EXERCICIO 8

def calcular_area_retangulo(base, altura):
    return (f"A área do retângulo é {base*altura}!")

teste = calcular_area_retangulo(12,34)
# print(teste)

# EXERCICIO 9

def eh_postivo(numero):
    if numero >= 0:
        return True
    else:
        return False
    
teste = eh_postivo(-50)
# print(teste)
    
# EXERCICIO 10

class carro:
    def __init__(self, modelo, ano, ligado):
        self.modelo = modelo
        self.ano = ano
        self.ligado = ligado
    
    
    def ligar(self):
        self.ligado = True
        pass

Carrinho = carro("Honda", 1995, False)
Carrinho.ligar()
print(Carrinho.ligado)