import random
def rolar_dados(inteiro):
    dadosrolados = []  
    for i in range(inteiro): 
        dado = random.randint(1, 6)
        dadosrolados.append(dado)
    return dadosrolados    

def guardar_dado(dadosrolados, dadosnoestoque, indice):
    listacompleta = [] 
    novalista = [] 
    
    
    dadosnoestoque.append(dadosrolados[indice])
    del dadosrolados[indice]
    
    listacompleta.append(dadosrolados)
    listacompleta.append(dadosnoestoque)
    return listacompleta 

def remover_dado(dadosrolados, dadosnoestoque, indice):
    listafinal = [] 
    dadosrolados.append(dadosnoestoque[indice])
    del dadosnoestoque[indice]
    listafinal.append(dadosrolados)
    listafinal.append(dadosnoestoque)
    return listafinal 



