import os
class ToDO:
    def __init__(self):
        self.lista = []
    def removeTarefa(self, tarefa):
        self.lista.pop(tarefa)
        return 1
    def listarTarefa(self):
        return self.lista
    def addTarefa(self, tarefa):
        self.lista.append(tarefa)
        return 1

def parar():

    os.system("pause")

def limpe():
    
    os.system("cls")