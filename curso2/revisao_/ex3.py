palavra = 'perfume'
cont = 0
acerto = ''
while True:
    cont += 1
    letra_digitada = input('Digite uma letra: ') 
    if len(letra_digitada) > 1:
        print('DIGITE APENAS UMA LETRA')
    else:
        if letra_digitada in palavra:
            quiz = letra_digitada
            acerto += letra_digitada
            print(f'A sua letra {quiz} tem na palavra')
       
        else:
            print(f'ERROU {letra_digitada} NAO TEM NA PALAVRA..')
    if acerto == palavra:
        break
print(f'A PALAVRA ERA {palavra} VOCE ACERTOU COM {cont}.. parabens!')