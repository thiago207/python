dio = {
}

dio['nome'] = input('Digite seu nome')
dio['idade'] = input('Digite sua idade')
if dio.get('ola') is None:
    print('nao existe')
else:
    for k,v in dio.items():
        print(f'{k} - {v}', end='')

