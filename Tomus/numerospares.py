def numeros_pares(intervalo_inicio, intervalo_fim):
    return [num for num in range(intervalo_inicio, intervalo_fim + 1) if num % 2 == 0]

resultado = numeros_pares(6, 20)
print(resultado)