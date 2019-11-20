# Autor: Aline Capucho
# Data: 19/11/19



def inversao(mat):
    aux = 0
    for linhas in range(2):
        for colunas in range(2):
            print(mat[linhas][colunas], end='\t')
        print("\n")
    det = (mat[0][0]*mat[1][1]) - (mat[0][1]*mat[1][0])
    if det==0:
        return None
    else:
        aux = mat[0][0]
        mat[0][0] = mat[1][1]/det
        mat[1][1] = aux/det
        aux = mat[0][1]
        mat[0][1] = (-mat[1][0])/det
        mat[1][0] =  (-aux)/det
    return mat

def main():
    matriz=[0]*2
    for linhas in range(2):
        matriz[linhas]=[0]*2
    for linhas in range(2):
        for colunas in range(2):
            matriz[linhas][colunas] = float(input("Insira o elemento:"))
    matriz = inversao(matriz)
    for linhas in range(2):
        for colunas in range(2):
            print(mat[linhas][colunas], end ='\t')
        print("\n")
