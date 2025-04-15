def avaliacao_notas(*resp, sit=False):
    avaliacao = {
    }
    total = len(resp)
    media = sum(resp) / len(resp)
    avaliacao['total'] = len(resp)
    avaliacao['maior'] = max(resp) 
    avaliacao['menor'] = min(resp)
    avaliacao['media'] = sum(resp) /len(resp)
    
    if sit:
        if media >= 7:
            situacao = 'Boa!'
        else:
            situacao = 'Razualvel!'
        avaliacao['situacao'] = situacao
    return avaliacao
resp = avaliacao_notas(9.6,7,8.9,8,7, sit=True)
print(resp)