from DAO import *
from model import *
class ControllerListarTarefa:
    def __init__(self):
        listar_tarefas()

class ControllerAdicionarTarefa:
    def __init__(self, tarefa):
        self.tarefa = tarefa
        if len(self.tarefa) == 0:
            print("Escreva uma tarefa valida")
        else:
                adicionar_tarefa(self.tarefa)
                print("Tarefa Adicionada")

class ControllerExcluirTarefa:
    def __init__(self, excluir):
        try:
            excluir = int(excluir)
            if excluir <= 0:
                print(
                    "Digite o numero da tarefa que deseja excluir"
                )
            elif excluir >= len(listar_tarefas()):
                print("Digite um número valida")
            else:
                excluir_tarefas(excluir)
                print("Tarefa excluida")
        except Exception as e:
            print("Erro, tente novamente")

class ControllerConcluirTarefa:
    def __init__(self, tarefa):
        tarefa = int(tarefa)
        concluir_tarefa(tarefa)

class ControllerAlterarTarefa:
    def __init__(self, alterar):
            alterar = int(alterar)
            if alterar <= 0:
                print(
                    "Digite o numero da tarefa que deseja excluir")
class ControllerListaConcluidos:
    def __init__(self):
        try:
            listar_tarefas_concluidas()
        except Exception as e:
            print("Erro, tente novamente")

todo = ToDO()

def eh_numero_inteiro(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def obter_opcao():
    while True:
        opcao = input("Digite a opção desejada: ")
        if eh_numero_inteiro(opcao):
            return int(opcao)
        else:
            print("Escolha uma opção correspondente")