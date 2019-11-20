# Autor: Aline Capucho
# Data: 19/11/19

import os

def func_data(data):
    ano = ""
    mes = ""
    dia = ""
    for cont in range(10):
        if cont<4:
            ano += str(data[cont])
        if 4<cont<7:
            mes += str(data[cont])
        if 7<cont:
            dia += str(data[cont])
    data_dic={
        "ano":int(ano),
        "mes":int(mes),
        "dia":int(dia)}
    return data_dic

def func_atv(ativo):
    if len(ativo)>3:
        ativo = ativo.replace('\n', '')
    if ativo=="SIM":
        return True
    else:
        return False

def func_list(texto):
    aux = 1
    for cont in range(len(texto)):
        if texto[cont]==":":
            aux+=1
    lista = [""]*aux
    aux = 0
    for cont in range(len(texto)):
        if texto[cont]!=":":
            lista[aux]+= texto[cont]
        else:        
            aux+=1
    return lista

def func_ler(arq):
    lista = []
    for line in arq:
        lista.append(line)
    return lista
        
def main():
    cwd = os.getcwd()
    arq = open(cwd + "\cadastro.txt", "r")
    arquivo = func_ler(arq)
    lista = []
    for cont in range(len(arquivo)):
        lista.append(func_list(arquivo[cont]))
    print(lista)    
    
main()
    
