def vota(n=0):
    from datetime import datetime 
    n  = datetime.now().year - n
    if 18<= n <=70:
        return f'Com {n} seu voto é obrigatorio! '
    if 16<= n <= 17 or n >= 70:
        return f'Com {n} seu voto é opcional! '
    
nas = (int(input('Digite seu ano de nascimento: ')))
print(vota(nas))
