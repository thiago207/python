def soma (x=None,y=None,z=None):
    if x and y and z is not None:
        try:
            print(f'x + y + z = {x+y+z}')
        except Exception as erro:
            print(f'ERRO {erro}')
    else:
        print('DIGITE OS 3 PARAMETROS')


soma(2,3)
soma(6,6,8)
soma('1',1,'u')