def palindromo(palavra):
    palavra = palavra.lower()
    
    return palavra == palavra[::-1]

print(palindromo("ana"))