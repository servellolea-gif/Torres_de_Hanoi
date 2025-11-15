def mover_disco(origem, destino): #A torre de origem e a torre de destino não são fixas, elas alteram conforme a movimentação dos discos
    disco = origem.pop() #Remove o último disco da torre de origem
    destino.append(disco) # Adiciona o disco removido à torre de destino

def imprimir_torres(torre_A, torre_B, torre_C):
    print("Torre A:", torre_A)
    print("Torre B:", torre_B)
    print("Torre C:", torre_C)
    print() #Linha em branco para melhor visualização

def torres_de_hanoi_recursivo(num_discos, origem, destino, auxiliar):
    if num_discos == 1:
        mover_disco(origem, destino)
        imprimir_torres(torre_A, torre_B, torre_C)
    else:
        torres_de_hanoi_recursivo(num_discos - 1, origem, auxiliar, destino)
        mover_disco(origem, destino)
        imprimir_torres(torre_A, torre_B, torre_C)
        torres_de_hanoi_recursivo(num_discos - 1, auxiliar, destino, origem)

#Resolvendo o problema recursivamente
num_discos = 5
# Inicializando as torres e os discos
torre_A = list(range(num_discos, 0, -1)) # Torre A começa com todos os discos
torre_B = [] # Torre B começa vazia
torre_C = [] # Torre C começa vazia

# Mostrando o estado inicial das torres
imprimir_torres(torre_A, torre_B, torre_C)
torres_de_hanoi_recursivo(num_discos, torre_A, torre_C, torre_B)
