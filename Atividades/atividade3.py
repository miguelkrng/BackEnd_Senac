while True:
    valorTotal = 0.0
    print("="*35 + "\n")
    print("LOJA DE AUTOMÓVEIS")
    print("\n" + "="*35 + "\n")
    input("Pressione [ENTER] para iniciar o atendimento.")
        
    print("Estes são os carros disponíveis a venda:")
    print("1 - Carro popular. R$ 60.000,00") 
    print("2 - Carro Sedan - R$ 90.000,00")
    print("3 - Carro SUV - R$ 130.000,00")
    escolhaCarro = int(input("\nEscolha uma opção para comprar (1, 2 ou 3): "))
    if escolhaCarro == 1:
        print("Carro popular escolhido!")
        valorTotal += 60.000
    elif escolhaCarro == 2:
        print("Carro Sedan escolhido!")
        valorTotal += 90.000
    elif escolhaCarro == 3:
        print("Carro SUV escolhido!")
        valorTotal += 130.000
    else:
        print("Erro! Escolha um dos carros indicados.")
        
    querOpc = input("\nVocê deseja adicionar algum pacote de opcionais ao pedido? (S/N): ")
    if querOpc == "S":
        print("Lista de opcionais disponíveis:")
        print("1 - Teto Solar - R$ 5.000,00")
        print("2 - Bancos de couro - R$ 3.000,00")
        print("3 - Sensor de estacionamento dianteiro - R$ 12.000,00")
        escolhaOpc = int(input("\nQual opcional você deseja? (1, 2 ou 3) "))
        if escolhaOpc == 1:
            print("Teto solar adicionado ao pedido!")
            valorTotal += 5.000
        elif escolhaOpc == 2:
            print("Bancos de couro adicionados ao pedido!")
            valorTotal += 3.000
        elif escolhaOpc == 3:
            print("Sensor de estacionamento dianteiro adiocionado ao pedido!")
            valorTotal += 12.000
        else:
            print("Erro! Escolha um dos pacotes indicados.")
    elif querOpc == "N":
        print("Sem pacotes de opcionais então!")
    
    print("\n" + "="*35)      
    print("PAGAMENTO")
    print("="*35 +"\n")
    print(f"Valor total da sua compra: R${valorTotal:.3f},00")
    print("Selecione uma forma de pagamento: \n")
    print("1 - À vista (5% de desconto)")
    print("2 - Parcelado (Sem desconto)")
    escolhaPag = int(input("\n> "))
    if escolhaPag == 1:
        print("'À vista' selecionado!")
        print(f"Preço total: R${valorTotal - valorTotal*0.05:.3f},00")
        print("\nPagamento efetivado com sucesso! Aproveite seu automóvel! >> ō͡≡o ")
        input()
    elif escolhaPag == 2:
        print("'Parcelado' selecionado! ")
        print(f"Preço total: R${valorTotal:.3f},00")
        print("\nPagamento efetivado com sucesso! Aproveite seu automóvel! >> ō͡≡o ")
        input()
    else:
        print("Erro! Escolha uma opção indicada.")
    
    
    