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

def calcula_pontos_regra_simples (listanum):
    dicionario = {} 
    soma1 = 0
    soma2 = 0
    soma3 = 0
    soma4 = 0 
    soma5 = 0
    soma6 = 0 
    for i in range(len(listanum)):
        if listanum[i] == 1:
            soma1 = soma1 + 1 
        dicionario[1] = soma1 
        if listanum[i] == 2: 
            soma2 = soma2 + 2
        dicionario[2] = soma2 
        if listanum[i] == 3:
            soma3 = soma3 + 3
        dicionario[3] = soma3 
        if listanum[i] == 4:
            soma4 = soma4 + 4  
        dicionario[4] = soma4  
        if listanum[i] == 5:
            soma5 = soma5 + 5 
        dicionario[5] = soma5 
        if listanum[i] == 6:
            soma6 = soma6 + 6 
        dicionario[6] = soma6 

    return dicionario 
        

def calcula_pontos_soma (listadenum):
    soma = 0 
    for i in range(len(listadenum)):
        soma = soma + listadenum[i] 
    return soma 


        
def calcula_pontos_sequencia_baixa (listadenum):
    
    if 1 in listadenum and  2 in listadenum and 3 in listadenum and 4 in listadenum: 
        return 15 
    if 2 in listadenum and  3 in listadenum and 4 in listadenum and 5 in listadenum: 
        return 15
    if 3 in listadenum and  4 in listadenum and 5 in listadenum and 6 in listadenum: 
        return 15
    else:
        return 0 


