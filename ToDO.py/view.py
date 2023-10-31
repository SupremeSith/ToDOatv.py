from controller import *

sair = True

while sair == True:
    print("Menu ToDo")
    print(" 1.  Adicionar Tarefa\n 2.  Listar\n 3.  Alterar Tarefa\n 4.  Concluir Tarefa\n 5.  Listar Tarefas Concluidas\n 6.  Excluir Tarefas\n 7. Sair ")

    opcao = menu_opcao()

    match opcao:
        case 1:
            limpar()
            tarefa = input("Digite a tarefa: \n  ")
            adicionartarefa = AdicionarTarefaController(tarefa)
            parar()
            limpar()

        case 2:
            limpar()
            listar_tarefas()
            parar()
            limpar()
        case 3:
            limpar()
            print("-- Lista de Tarefas do arquivo -- ")
            listarTarefa = ListarTarefaController()
            alterar = input("\nDigite o número da tarefa que deseja alterar: ")
            alterarTarefa = AlterarTarefaController(alterar)
            parar()
            limpar()
        case 4:
            limpar()
            print("-- Lista de Tarefas do arquivo -- ")
            listarTarefa = ListarTarefaController()
            concluir = input("\nDigite o Id da tarefa que quer concluir: ")
            limpar()
            ConcluirTarefa = ConcluirTarefaController(concluir)
            listarTarefa = ListarTarefaController()
            parar()
            limpar()
        case 5:
            limpar()
            ListarTarefasConcluidas = ListaConcluidosController()
            parar()

        case 6:
            limpar()
            print("-- Lista de Tarefas do arquivo -- ")
            listarTarefa = ListarTarefaController()
            excluir = input("Digite o número da tarefa que deseja excluir: ")
            excluirTarefa = ExcluirTarefaController(excluir)
            limpar()
            print("-- Nova Lista de Tarefas --")
            listarTarefa = ListarTarefaController()
            parar()
            limpar()
        case 7:
            limpar()
            print("\n programa fechado ")
            parar()
            sair = False
        case _:
            limpar()
            print("erro \n erro \n erro")
            print("")
            parar()
            limpar()