def ordenar_string(frase):

    palavras = frase.split()
    palavras_ordenadas = sorted(palavras)
    resultado = " ".join(palavras_ordenadas)
    return resultado

entrada = "o rato roeu a roupa do rei de roma"
saida = ordenar_string(entrada)
print("Saída:", saida)
