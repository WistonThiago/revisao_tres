def mostrarNomes():
    nomesOne = ["Maria", "João","Roberto", "Thiago"]
    print("1 - ", nomesOne[0])
    print("2 - ", nomesOne[1])
    print("3 - ", nomesOne[2])
    print("4 - ", nomesOne[3])
mostrarNomes()

def tarefaDois():
    nomesTwo = ["Marcos", "Rogério", "Joana", "Rafaela"]
    print("Primeiro nome: ", nomesTwo[0])
    print("Último nome: ", nomesTwo[3])
tarefaDois()

def tarefaTres():
    nomesThree = ["Emílio", "Jonas", "Patrícia", "Laís"]
    print("Segundo nome: ", nomesThree[1])
    print("Terceiro nome: ", nomesThree[2])
tarefaTres()

def tarefaQuatro():
    alimentos = ["Macarrão", "Pepino", "Batata"]
    alimentoUm = input("Escolha um alimento: ")
    alimentoDois = input("Escolha outro alimento: ")
    alimentoTres = input("Escolha o último alimento: ")
    alimentos[0] = alimentoUm
    alimentos[1] = alimentoDois
    alimentos[2] = alimentoTres
    print("1 - ", alimentos[0])
    print("2 - ", alimentos[1])
    print("3 - ", alimentos[2])
tarefaQuatro()