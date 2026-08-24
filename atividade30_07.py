# EXERCICIO 1
def analisar_notas(listaNotas):
    numApr = 0
    numRep = 0
    numNotas = len(listaNotas)
    notasSoma = 0
    for nota in listaNotas:
        notasSoma += nota
        if nota >= 7.0:
            numApr += 1
        else:
            numRep += 1
    media = notasSoma / numNotas
    return f"Número de  alunos aprovados: {numApr} \nNúmero de alunos reprovados: {numRep} \nMédia geral das notas: {media:.2f}"

notasTeste = [5.6, 7.0, 4.5, 1.8, 2.8, 9.0]
# print(analisar_notas(notasTeste))

# EXERCICIO 2

def separar_numeros():
    print("Digite números inteiros para separar em par ou impar!")
    print("(digite -1 para parar...)")
    numPares = []
    numImpares = []
    while True:
        numero = int(input("> "))
        if numero == -1:
            break
        elif numero % 2:
            numPares.append(numero)
        else:
            numImpares.append(numero)
        print("\n=== Resultado ===\n")
        print(f"Números pares: {numPares}")
        print(f"Números ímpares: {numImpares}")
        
# separar_numeros()

# EXERCICIO 3

def somar_diagonais(matriz):
    for linha in range(3):
        for coluna in range(3):
            if linha == coluna:
                print(f"{linha} + {coluna}")
                
# ? an 

# EXERCICIO 4

def verificar_cinema(sala):
    assentosOcupado = 0
    assentosLivre = 0
    for assento in sala:
        if assento == 1:
            assentosOcupado += 1
            return "O"
        elif assento == 0:
            assentosLivre += 1
            return "."
    
salaTeste = [[1,0,0], [0,1,1], [1,1,1]]
print (verificar_cinema(salaTeste))