def soma (x=0,y=0,z=0):
    try:
        print(f'x + y + z = {x+y+z}')
    except Exception as erro:
        print(f'ERRO {erro}')
    
soma(2,3,8)
