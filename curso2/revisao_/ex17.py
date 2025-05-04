pessoas = {
    'nome': 'Thiago', 
    'sobrenome': 'Felipe',

}
def mostar(args):
    for k,v in args.items():
        print(f'{k} - {v}')
    
mostar(pessoas)