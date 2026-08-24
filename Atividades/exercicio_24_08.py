tarefas = []
while True:
    print("""
    Informe a próxima tarefa:
    (digite 'sair' para encerrar.)
    """)
    tarefaNova = input("> ")
    if tarefaNova == "sair":
        break
    else:
        tarefas.append(tarefaNova)
    print("\nTAREFAS ATUAIS -")
    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"{indice} - {tarefa}")
        if not tarefas:
            print("Nenhuma tarefa registrada")
    print("\nDeseja remover alguma tarefa? (S/N)")
    opcaoRem = input("> ")
    if opcaoRem == "S":
        try:
            tarefaRem = int(input("\nInforme o número da tarefa a ser removida: "))-1
            tarefas.pop(tarefaRem)
            print("Tarefa removida com sucesso!")
        except ValueError:
            print("O número inserido não está na lista.")
                