def adicionar_tarefas(lista_tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    lista_tarefas.append(tarefa)

def exibir_tarefas(lista_tarefas):
    for id, tarefa in enumerate(lista_tarefas):
        print("%s: %s" % (id, tarefa))

lista_de_tarefas = []

while True:
    print("\nGerenciador de lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    opcao = input("Digite a opção: ")
    if opcao == "1":
        tarefa = input("Qual é a tarefa? ")
        adicionar_tarefas(lista_de_tarefas, tarefa)

    if opcao == "2":
        exibir_tarefas(lista_de_tarefas)

    if opcao == "6":
        print("Gerenciador de tarefas finalizado")
        break