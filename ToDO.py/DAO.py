import random
def adicionar_tarefa(tarefa):
    with open("ToDo.txt", "r") as arquivo:
        tarefas = arquivo.readlines()
        id = random.randint(1000, 9999)
        listaids = []
        while id in tarefas:
            id = random.randint(1000, 9999)
        if id not in listaids:
            listaids.append(id)
        else:
            pass
        with open("ToDo.txt", "a") as arquivo:
            arquivo.write(f"\nA        {id}    {tarefa}")

def listar_tarefas_concluidas():
    with open("ToDo.txt", "r") as arquivo:
        tarefas = arquivo.readlines()
        tarefas_sem_numero = []
        for item in tarefas:
            item_sem_numeros = "".join(
                caractere for caractere in item if not caractere.isdigit()
            )
            tarefas_sem_numero.append(item_sem_numeros)
        
           
                x, item in enumerate(tarefas_sem_numero):
            if index == 0:
                print("Id   Status  Tarefa")
            elif item.startswith("C"):
                print(f"{index}     {item.strip()}")
    return tarefas
    
def listar_tarefas():
    with open("ToDo.txt", "r") as arquivo:
        tarefas = arquivo.readlines()
        tarefas_sem_numero = []
        for item in tarefas:
            item_sem_numeros = "".join(
                caractere for caractere in item if not caractere.isdigit()
            )
            tarefas_sem_numero.append(item_sem_numeros)
        for index, item in enumerate(tarefas_sem_numero):
            if index == 0:
                print("Id   Status  Tarefa")
            elif item.startswith("A"):
                print(f"{index}     {item.strip()}")
    return tarefas


def excluir_tarefas(tarefa):
    with open("ToDo.txt", "r") as arquivo:
        tarefas = arquivo.readlines()
        index = 0
        if 0 <= tarefa < len(tarefas):
            with open("ToDo.txt", "w") as arquivo:
                for i, t in enumerate(tarefas):
                    if index == 0:
                        print("Id   Status  Tarefa")
                        index += 1
                    if i == tarefa:
                        t = t[1:]
                        arquivo.write(f"E{t}")
                    else:
                        arquivo.write(f"{t}")

def concluir_tarefa(tarefa):
    with open("ToDo.txt", "r") as arquivo:
        tarefas = arquivo.readlines()
        index = 0

        if 0 <= tarefa < len(tarefas):
            with open("ToDoo.txt", "w") as arquivo:
                for i, t in enumerate(tarefas):
                    if index == 0:
                        print("Id   Status  Tarefa")
                        index += 1
                    if i == tarefa:
                        t = t[1:]
                        arquivo.write(f"C{t}")
        
def alterar_tarefa(tarefa):
    with open("ToDo.txt", "r") as arquivo:
        tarefas = arquivo.readlines()
        index = 0
        for item in tarefas:
            if index == tarefa:
                id_tarefa = "".join(filter(str.isdigit, item))
                status_tarefa = item[0]
                tarefas.pop(index)
                nova_tarefa = input("Digite a nova tarefa: ")
                tarefas.insert(
                    index, f"{status_tarefa}        {id_tarefa}    {nova_tarefa}\n"
                )
            index += 1
    with open("ToDo.txt", "w") as arquivo:
        for item in tarefas:
            arquivo.write(f"{item}")
