def vota(n=0):
    from datetime import datetime 
    n = datetime.now().year - n
    if 18<= n <=70:
        print(f'Com {n} seu voto é obrigatorio! ')
    if 16<= n <= 17 or n >= 70:
        print(f'Com {n} seu voto é opcional! ')
    return n
nasc = vota(int(input('Digite seu ano de nascimento: ')))
