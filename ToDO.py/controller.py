from DAO import *
from model import *

def menu_opcao():
    while True:
        opcao = input("Digite a opção desejada: ")
        if eh_numero_inteiro(opcao):
            return int(opcao)


class ListaConcluidosController:
    def __init__(self):
        try:
            listar_tarefas_concluidas()
        except Exception as e:
            print("Ocorreu um erro ao listar tarefas concluídas")


class AdicionarTarefaController:
    def __init__(self, tarefa):
        self.tarefa = tarefa
        if not self.tarefa:
            print("Por favor, digite uma tarefa antes de adicionar.")
        else:
            try:
                adicionar_tarefa(self.tarefa)
                print("Tarefa adicionada com sucesso!")
            except Exception as e:
                print("Erro ao adicionar tarefa")


class ExcluirTarefaController:
    def __init__(self, numero_tarefa):
        try:
            numero_tarefa = int(numero_tarefa)
            if numero_tarefa <= 0:
                print("Digite um número inteiro positivo maior que zero para excluir uma tarefa.")
            elif numero_tarefa >= len(listar_tarefas()):
                print("Número de tarefa a excluir está fora do alcance.")
            else:
                excluir_tarefas(numero_tarefa)
                print("Tarefa excluída com sucesso!")
        except ValueError:
            print(" Digite um número válido para excluir uma tarefa.")


class AlterarTarefaController:
    def __init__(self, numero_tarefa):
        try:
            numero_tarefa = int(numero_tarefa)
            if numero_tarefa <= 0:
                print("Digite um número inteiro positivo maior que zero para alterar uma tarefa.")
            elif numero_tarefa >= len(listar_tarefas()):
                print("Número de tarefa a alterar está fora do alcance.")
            else:
                try:
                    alterar_tarefa(numero_tarefa)
                    print("Tarefa alterada com sucesso!")
                except Exception as erro:
                    print(f"Erro ao alterar tarefa")
        except ValueError:
            print("Digite um número válido para alterar uma tarefa.")


class ListarTarefaController:
    def __init__(self):
        try:
            listar_tarefas()
        except Exception as erro:
            print("Erro ao listar tarefas")


class ConcluirTarefaController:
    def __init__(self, numero_tarefa):
        try:
            numero_tarefa = int(numero_tarefa)
            concluir_tarefa(numero_tarefa)
            print("Tarefa concluída com sucesso!")
        except ValueError:
            print("Digite um número válido para concluir uma tarefa.")


todo = ToDO()


def eh_numero_inteiro(s):
    try:
        int(s)
        return True
    except ValueError:
        return False