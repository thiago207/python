letras = set()
while True:
    letra = input('Digite: ').strip().lower()
    letras.add(letra)

    if 'l' in letras:
        break

    print(letras)
