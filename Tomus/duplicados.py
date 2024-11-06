def remover_duplicados(lista):

    lista_unica = []

    for elemento in lista:
        if elemento not in lista_unica:
            lista_unica.append(elemento)
    
    return lista_unica

numeros = [1, 2, 2, 3, 4, 4, 5, 6, 6]
saida = remover_duplicados(numeros)
print("Não duplicados:", saida)