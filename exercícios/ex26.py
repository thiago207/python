frase = str(input('Digite uma frase: ')).upper().strip()

print(f'Quantas vezes aparece A? {frase.count('A')}')
print(f'A primeira vez aparece na posicao: {frase.find('A')+1}')
print(f'A ultima vez aparece na posicao: {frase.rfind('A')+1}')
