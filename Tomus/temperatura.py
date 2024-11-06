def converter_temperatura(valor, unidade):
    if unidade.upper() == "C":
        fahrenheit = (valor * 1.8) + 32
        return fahrenheit
    
    elif unidade.upper() == "F":
        celsius = (valor - 32) / 1.8
        return celsius
    
    else:
        return "Unidade inválida! Use 'C' para Celsius ou 'F' para Fahrenheit."


temperatura = (100, "C")
saida = converter_temperatura(*temperatura)
print("Temperatura:", saida)  # Saída: 212