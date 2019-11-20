# Autor: Aline Capucho
# Data: 19/11/19



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
        ativo.del(3)
    if(ativo)=="SIM":
        return True
    else:
        return False

