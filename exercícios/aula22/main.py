from uteis import numeros



num = int(input('digite o valor> '))

fat = numeros.fatorial(num)

print(f'Seu numero {num} fatorado fica {fat}')
print(f'Seu numero {num} dobrado fica {numeros.dobro(num)}')
print(f'Seu numero {num} triplo fica {numeros.triplo(num)}')