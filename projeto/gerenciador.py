def adicionar_tarefas(lista_tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    lista_tarefas.append(tarefa)

def exibir_tarefas(lista_tarefas):
    for id, tarefa in enumerate(lista_tarefas):
        if tarefa["completada"] == False:
            print("%s - %s" % (id+1, tarefa["tarefa"]))

def atualizar_tarefas(lista_tarefas):
    opcao = input("Qual tarefa deseja editar? ")
    id_tarefa = int(opcao) - 1
    tarefa = lista_tarefas[id_tarefa]["tarefa"]
    tarefa_editada = input("Edite a tarefa '%s': " % tarefa)
    lista_tarefas[id_tarefa]["tarefa"] = tarefa_editada

def completar_tarefa(lista_tarefas):
    opcao = input("Qual tarefa deseja completar? ")
    id_tarefa = int(opcao) - 1
    lista_tarefas[id_tarefa]["completada"] = True

lista_de_tarefas = []

while True:
    print("\nGerenciador de lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Sair")

    opcao = input("Digite a opção: ")
    if opcao == "1":
        tarefa = input("Qual é a tarefa? ")
        adicionar_tarefas(lista_de_tarefas, tarefa)

    if opcao == "2":
        exibir_tarefas(lista_de_tarefas)

    elif opcao == "3":
        atualizar_tarefas(lista_de_tarefas)

    elif opcao == "4":
        completar_tarefa(lista_de_tarefas)

    elif opcao == "5":
        print("Gerenciador de tarefas finalizado")
        break