def inverter_palavras(frase):

    palavras = frase.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    frase_invertida = " ".join(palavras_invertidas)
    
    return frase_invertida


entrada = "estou aprendendo a programar"
saida = inverter_palavras(entrada)
print("Saída:", saida)
