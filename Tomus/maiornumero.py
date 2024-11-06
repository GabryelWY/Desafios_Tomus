def maior_numero(lista):

  if not lista:
    return None

  maior = lista[0]
  for numero in lista[1:]:
    if numero > maior:
      maior = numero
  return maior

numeros = [5, 3, 9, 1]
resultado = maior_numero(numeros)
print("O maior número é:", resultado)