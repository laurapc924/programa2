import random
def rolar_dados(inteiro):
    dadosrolados = []  
    for i in range(inteiro): 
        dado = random.randint(1, 6)
        dadosrolados.append(dado)
    return dadosrolados    