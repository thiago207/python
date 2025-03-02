frase = str(input('Digite sua frase : ')).upper().strip()
palavras = frase.split()
junto =''.join(palavras)
inverso = ''
for letras in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letras]
print(f'{frase}  {inverso}')
if frase == inverso:
    print('É UM POLINDROMO')
else:
    print('NAO É UM POLINDROMO')

