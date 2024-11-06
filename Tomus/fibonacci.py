def fibonacci_ate_limite(limite):
  
  sequencia = [0, 1]
  while sequencia[-1] + sequencia[-2] <= limite:
    proximo = sequencia[-1] + sequencia[-2]
    sequencia.append(proximo)
  return sequencia[:-1]

limite = 20
resultado = fibonacci_ate_limite(limite)
print(resultado)