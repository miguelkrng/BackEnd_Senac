class Produto:
    """
    Representa um item do cardápio.
    Atributos: id (int), nome (str), preco (float).
    """
    def __init__(self, idProduto, nome, preco):
        self.id = idProduto
        self.nome = nome
        self.preco = preco
        pass

    def __str__(self):
        return (f"{self.id}. {self.nome:<18} R$ {self.preco:2f}")


class ItemCarrinho:
    """
    Associa um objeto Produto a uma quantidade comprada.
    """
    def __init__(self, produto, quantidade):
       self.produto = produto
       self.quantidade = quantidade
       pass
       

    def calcular_subtotal(self):
        return self.produto.preco * self.quantidade


class Carrinho:
    """
    Gerencia a lista de itens (ItemCarrinho) que o cliente escolheu.
    """
    def __init__(self):
       self.itens = []
        

    def adicionar_item(self, produto, quantidade):
        novo_item = ItemCarrinho (produto, quantidade)
        self.itens.append (novo_item)
        

    def calcular_total(self):
        total = 0.0
        for item in self.itens:
            total += item.calcular_subtotal()
        return total

    def esta_vazio(self):
        return len(self.itens) == 0

    def limpar(self):
      self.itens.clear()
        


class Totem:
    """
    Controla toda a execução e interface do sistema.
    """
    def __init__(self):
        self.cardapio = {}
        self.carrinho = Carrinho()
        self.proxima_senha = 1
        self.inicializar_cardapio()

    def inicializar_cardapio(self):
        """
        Método pronto: Cadastra os produtos disponíveis no sistema.
        """
        
        produtos_iniciais = [
            Produto(1, "Hambúrguer", 15.00),
            Produto(2, "Cheeseburger", 18.00),
            Produto(3, "Batata Frita", 9.00),
            Produto(4, "Refrigerante", 6.00),
            Produto(5, "Suco Natural", 8.00)
        ]
        for prod in produtos_iniciais:
            self.cardapio[prod.id] = prod

    def exibir_cardapio(self):
        print ("\n" + "="*35)
        print ("           TOTEM FAST FOOD          ")
        print ("="*35)
        for produto in self.cardapio.values():
            print (produto)
        print ("="*35)
        pass

    def processar_pagamento(self):
        total = self.carrinho.calcular_total()
        print (f"\n>>> total da sua compra: R${total:.2f}")
        print ("Escolha forma de pagamento \n")
        print("1 - Cartão de crédito \n2 - Cartão de Débito \n3 - PIX")
        
        while True:
            forma = input ("\n> ").strip()
            if forma in ['1', '2', '3']:
                print ("\n" + "-"*30 + "\n")
                print ("Pagamento aprovado!")
                print ("Retire seu cupom, bon appetit!")
                print ("\n" + "-"*30)
                break
            else:
                print ("\nopção inválida... Escolha entre 1, 2 ou 3.")
                pass
            

    def iniciar_atendimento(self):
        """
        Loop principal do Totem (Sempre ativo).
        """
        continuar = str
        
        while True:
            self.exibir_cardapio()
            
            print("\n=== BEM-VINDO AO FAST-FOOD! ===")
            input("Pressione [ENTER] para iniciar o seu pedido...")
            
            querPedir = True
            
            while querPedir == True:
                
                try:
                
                    opcao = int(input("Digite o número do item desejado: "))
                    if opcao in self.cardapio:
                        produto_selecionado = self.cardapio[opcao]
                        quantidade = int(input(f"quantas unidades de '{produto_selecionado.nome}' você deseja? "))
                        if quantidade > 0:
                            self.carrinho.adicionar_item (produto_selecionado,quantidade)
                            print (f"O produto foi adicionado com sucesso! Subtotal atual: R$ {self.carrinho.calcular_total():.2f}")
                        else:
                            print("Erro! A quantidade deve ser maior que zero.")
                    else:
                            print ("Erro!  O item não foi encontrado no cardápio.")
                except ValueError:
                    print("Por favor, insira um número válido.")
                    continue
                continuar = input("\n Deseja adicionar mais algum item? (S/N): "). strip().upper()
                
                if continuar == "N":
                    querPedir = False
                    if  not self.carrinho.esta_vazio():
                    
                        self.processar_pagamento()
                        self.proxima_senha += 1    
                        break
                    else: print ("O pedido foi cancelado (nenhum item adicionado). \n")
                    continue
                
                
                
                


# bloco principal para testar o sistema :p
if __name__ == "__main__":
    totem_loja = Totem()
    totem_loja.iniciar_atendimento()