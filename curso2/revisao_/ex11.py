perguntas = [
    {
        'Pergunta': 'Quanto é 2+2',
        'Opcoes': ['1','2','3','4'],
        'Resposta': '4',
    }
    ,
    {
        'Pergunta': 'Quanto é 5x5',
        'Opcoes': ['10','15','25','20'],
        'Resposta': '25',
    }
]
acertou = False
while True:
    for pergunta in perguntas:
        print(pergunta['Pergunta'])
        print()

        opcoes = pergunta['Opcoes']

        for e,opcao in enumerate(opcoes):
            print(f'{e})  {opcao}')
        
        print()
        qtd_opc = len(opcoes)
        try:
            escolha = input('Escolha uma opçao: ')
            escolha_int = int(escolha)
            if escolha_int >= 0 and escolha_int < qtd_opc:
                if opcoes[escolha_int] == pergunta['Resposta']:
                    print(f'ACERTOU')
                    acertou = True
                else:
                    print('ERROU')
                
    
        except:
            print('Digite um valor valido')
        print()
    if acertou:
        break
        
