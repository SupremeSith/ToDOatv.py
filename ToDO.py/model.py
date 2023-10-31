import os
class ToDO:
    def __init__(self):
        self.lista = []
    def listarTarefa(self):
        return self.lista
    def addTarefa(self, tarefa):
        self.lista.append(tarefa)
        return 1
    def removeTarefa(self, tarefa):
        self.lista.pop(tarefa)
        return 1
def limpar():
    os.system("cls")
def parar():
    os.system("pause")