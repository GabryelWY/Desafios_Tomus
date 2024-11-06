def contar_vogais(texto):
  """Conta o número de vogais em uma string.

  Args:
    texto: A string a ser analisada.

  Returns:
    O número de vogais na string.
  """

  vogais = "aeiouAEIOU"
  contador = 0
  for letra in texto:
    if letra in vogais:
      contador += 1
  return contador

texto = "Hello World"
resultado = contar_vogais(texto)
print("O número de vogais é:", resultado)