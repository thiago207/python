# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]
for item in lista:
    print()
    if isinstance(item, set):
        item.add(5)
        print(item)
        print('SET')

    elif isinstance(item,dict):
        for k,v in item.items():
            print(f'{k} - {v}')
        print('DICT')

    elif isinstance(item, str):
        print(item.upper())
        print('STR')

    elif isinstance(item, (int, float)):
        print(f'{item} - {item * 2}')
        print('NUM')
    
    else:
        print(item)
        print('OUTRO')