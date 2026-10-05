
contador = 0
print (contador)

def aumentar_contador():
    global contador
    contador += 1

def diminuir_contador():
    global contador
    contador -= 1 

aumentar_contador()
print(contador)