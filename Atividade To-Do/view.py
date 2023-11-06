from controller import *
sair = True
while sair == True:
    limpe()
    print("To-Do Menu")
    print(" 1.  Adicionar tarefa\n 2.  Listar tarefas\n 3.  Alterar tarefas\n 4.  Concluir Tarefa\n 5.  Listar tarefas concluidas\n 6.  Excluir tarefa\n 7.  Sair\n")
    opcao = obter_opcao()
    match opcao:
        case 1:
            limpe()
            tarefa = input("Digite a sua tarefa: ")
            adicionartarefa = ControllerAdicionarTarefa(tarefa)
            parar()
        case 2:
            limpe()
            print("")
            listar_tarefas()
            print("")
            parar()
        case 3:
            limpe()
            listarTarefa = ControllerListarTarefa()
            alterar = input("\nDigite o número da tarefa que deseja alterar: ")
            alterarTarefa = ControllerAlterarTarefa(alterar)
            parar()
        case 4:
            limpe()
            listarTarefa = ControllerListarTarefa()
            concluir = input("\nDigite o ID da tarefa a ser concluida: ")
            ConcluirTarefa = ControllerConcluirTarefa(concluir)
            listarTarefa = ControllerListarTarefa()
            parar()
        case 5:
            limpe()
            ListarTarefasConcluidas = ControllerListaConcluidos()
            parar()
        case 6:
            limpe()
            listarTarefa = ControllerListarTarefa()
            excluir = input("Digite o número da tarefa que deseja excluir: ")
            excluirTarefa = ControllerExcluirTarefa(excluir)
            limpe()
            listarTarefa = ControllerListarTarefa()
            parar()
        case 7:
            limpe()
            parar()
            sair = False
        case _:
            limpe()
            print("Digite uma opção valida")
            print("")
            parar()