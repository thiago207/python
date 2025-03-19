tupla = ('Casa',  'Celular', 'Python', 'Viagem', 'Estudos', 'Progama','Foco', 'Disciplina')
for p in tupla:
    print(f'Na palavra {p} temos: ')
    for letras in p:
        if letras in 'aeiou':
            print(letras)
    
