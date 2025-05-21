questions = [
    {
        'question': 'Quanto é 2+2?',
        'options': ['1', '2', '4', '5'],
        'response': '4',
    },
    {
        'question': 'Quanto é 8-3?',
        'options': ['1', '2', '4', '5'],
        'response': '5',
    },
    {
        'question': 'Quanto é 5*5?',
        'options': ['25', '55', '10', '51'],
        'response': '25',
    },
    {
        'question': 'Quanto é 10/2?',
        'options': ['4', '5', '2', '1'],
        'response': '5',
    },
    
]

questions_certas = 0
questions_erradas = 0

for opcs in range(len(questions)):
    questao = questions[opcs]['question']
    opcaos = questions[opcs]['options']
    resposta = questions[opcs]['response']

    print(questao)
    print(f'{opcaos[0]}\n{opcaos[1]}\n{opcaos[2]}\n{opcaos[3]}\n')
    sua_resposta = input('-->')

    if sua_resposta == resposta:
        print('ACERTOU')
        questions_certas += 1
    else:
        print('ERROU')
        questions_erradas += 1
    
print(f'Acertos: {questions_certas}\nErradas: {questions_erradas}')
