# EXERCICIO 1
numero = 15
# if numero%2:
#     print("É par")
# else:
#     print("É ímpar")

# EXERCICIO 2
num = 9
# for i in range(1, 11):
#     resultado = num * i
#     print(f"{num} x {i} = {resultado}")
    
# EXERCICIO 3
contagem = 5
# while contagem >= 0:
#     print(f"{contagem}...")
#     contagem -= 1
# print("Decolagem!")

# EXERCICIO 4
frutas = ["Maçã", "Banana", "Morango", "Melancia", "Uva"]
# for fruta in frutas:
#     if fruta.startswith("M"):
#         print(fruta)
        
def celsius_para_fahrenheit(Celsius):
    Fahrenheit = (Celsius*1.8)+32
    return (f"{Fahrenheit}F")

teste = celsius_para_fahrenheit(30)
print(f"A temperatura 30° em fahrenheint é {teste}")