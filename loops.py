def contarAteVinte():
    for i in range(21):
        print(i)
contarAteVinte()

def contadorUser():
    number = int(input("Digite um número inteiro: "))
    counter = 1
    while (counter <= number):
        print(counter)
        counter = counter + 1
contadorUser()

def somaUser():
    value = int(input("Digite um número inteiro: "))
    sum = 1
    while (sum <= value):
        operation = value + sum
        print(f"{value} + {sum} = {operation}")
        sum = sum + 1
somaUser()

def tabuada():
    valor = int(input("Digite um número inteiro: "))
    times = 1
    while (times <= 10):
        operation = valor * times
        print(f"{valor} x {times} = {operation}")
        times = times + 1
tabuada()

def callName():
    print("Calling the name of function!")
callName()