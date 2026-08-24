# variaveis

variavel = "variavel"
variaNum = 10
variaFloat = 5.50
BoloDeChocolate = "bolo de chocolate"

fruta1, fruta2, fruta3 = "Morango", "Uva", "Maçã"
#print(fruta1)
#print(fruta2)
#print(fruta3)

#---------------------------------------------------------------------------------------------------------------

#operations mathematics

num1 = 1
num2 = 2
num3 = 3

soma = (num1+num2+num3)
#print(soma)
#print(5+2) 

#---------------------------------------------------------------------------------------------------------------

#operadores logicos
# '=' -> recebe / '==' -> igual
# '!=' -> diferente

x = 10
y = 20
#print(x == y)
#print(x > y)
#print(x != y)

#print(x > 30 and x < 9) # AND = e
#print(x < 12 or x > 30) # OR  = ou
#print(not(x > 12 and x < 9)) # NOT = não

#----------------------------------------------------------------------------------------------------------------

# concatenação

nome = "miguel"
idade = "16"
#print(f"Meu nome é {nome} e eu tenho {idade} anos")

#entrada de dados

#nome = input("Qual seu nome? ")
#print(f"O nome do usuário é {nome}")
#idade = input("Qual a sua idade? ")
#print(f"A idade do usuário é {idade} anos")

#----------------------------------------------------------------------------------------------------------------

#Listas

listaFruta = ["uva", "morango", "maçã", "banana"]
fruta1, fruta2, fruta3, fruta4 = listaFruta
#print(fruta1, fruta2, fruta3, fruta4)

#tipos de dados

#a = "eu sou uma string" #string (str)
#b = 10 #inteiro (Int)
#c = 10.5 #float (Flt)
#d = "A1" #string com numero
#e = ["item1", "item2", "item3"] #Lista (lst)
#f = True #booleano (bln)

#print(type(c))
#---------------------------------------------------------------------------------------------------------------
#ESTRUTURAS CONDICIONAIS
a = 5000
b = 500

#if a < b: #SE
    #print("B é maior que A")
#else: #SE NÃO
    #print("A é maior")
    
#if a < b: print() else: print()

#----------------------------------------------------------------------------------------------------------------

nome1 = "Julia"
nome2 = "Julia"
nome3 = "Giulia" 
nome4 = "Julia"

#if nome1 == nome2 and nome1 == nome3:#And -> E (ambas as condições são verdadeiras)
    #print("Os nomes são iguas")
#elif nome1 == nome2  or nome1 == nome3: #OER -> OU (Ao menos uma das checagens tem que ser verdadeira)
   # print("Apenas um dos nomes são iguais")
#elif nome1 == nome4 or nome1 != nome2:
    #print("Um dos nomes é igual e o outro é diferente")
#else:
    #print("Os nomes são diferentes")
 
 #---------------------------------------------------------------------------------------------------------------
   
    #LOPS = Estrutura de repetição
   
numeroMaior = 0
    
#while numeroMaior <= 10:
    #print(numeroMaior)
    #numeroMaior += 1
#else:
    #print("A variável numeroMaior não é mais menor que 10")   
    #print("Fim do Programa")
    
#----------------------------------------------------------------------------------------------------------------

#nomes = ['Cleytin', 'Valdemar', 'Xerocleyde', 'Xequira', 'Carimbo']
#sobrenomes = ['Santos', 'Silva']

#for nome in nomes
    #for sobrenome in sobrenomes
            #nome = nome + " " sobrenome
        #print(nome)
      
# for x in "Emanuelle:
    # print(x)

# for numeros in range(10):
#     print(numeros)
    
for numero in range (1, 30, 3):
    print(numero)