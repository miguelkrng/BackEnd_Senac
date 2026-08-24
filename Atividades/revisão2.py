# precoPeca = float(input("Digite o preço da peça que você deseja checar: R$"))
# if precoPeca <= 350.00:
# print("A peça está com o preço ótimo, é recomendável comprar!")
# elif precoPeca > 350.00 and precoPeca <= 550.00:
# print("A peça está com preço padrão, compare o preço entre lojas e compre o melhor")
# elif precoPeca > 550.00 and precoPeca < 850.00:
# print("A peça está com preço alto, melhor esperar uma promoção ou procurar outra")
# else:    print("djabo de preço. nam. compra não D:")
        
#  ===========================================================================================
class produto:
    """
    Peças de computador.com
    """
    
    def __init__(self,nome:str, preco:float, tipo: str, marca: str):
        self.nome = nome
        self.preco = preco
        self.tipo = tipo
        self.marca = marca
    """
    Pode fazer
    """
    
    def checar_preco(self):
        if self.preco <= 350.00:
            return "O produto está com o preço ótimo. é recomendável comprar!"
        elif self.preco > 350.00 and self.preco <= 550.00:
            return "O produto está com preço padrão. compare o preço entre lojas e compre o melhor."
        elif self.preco > 550.00 and self.preco < 850.00:
            return "O produto está com preço alto. melhor esperar uma promoção ou procurar outra."
        else:
            return "Djabo de preço. nam. compra não D:"
        
    def exibir_resumo(self):
        categoria = self.checar_preco()
        print (f"> Produto: {self.nome} | Tipo: {self.tipo} | Marca: {self.marca} | Preço: R${self.preco:.2f}.\n- Recomendação: {categoria}")
        
mRam = produto("Memória RAM", 370.00, "DDR4 8gb", "Hyper")
mRam.checar_preco()
mRam.exibir_resumo()
placaVideo = produto("Placa de vídeo", 900.00, "Alpha rx580", "Husky")
placaVideo.checar_preco()
placaVideo.exibir_resumo()
print(produto.__doc__)