# Tuplas - () - geralmente usado para cadastrar coisas privadas/imutaveis como cpf's ou senhas

# MANIPULAÇÃO DE LISTAS -

# adição direta -
lista = [0,1,2,3,4,5,6,7,8,9]
# print(lista)
lista.append(1) #adiciona algo a lista
lista.insert(0, 30) #adiciona com precisão num local específico da lista
lista.extend([10,20,30]) #extende a lista com mais de um valor no final - adiciona uma lista dentro da lista/j
# print(lista)

# Remoção direta -
lista.remove(30) #busca o item e remove o primeiro que aparecer
del lista[0:2] #remove todos os itens dentro do índicie informado
lista.clear() #limpa a lista 
print(lista)