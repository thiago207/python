nome = str(input('Qual seu nome? '))
if nome.upper() == 'JULIANA':
    print('Amor da vida de thiago')
else:
    print('nao presta.')
    
if nome.upper() == 'THIAGO':
    print('Que nome lindo!')
         
print(f'bom dia {nome}!')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua media foi {m:.1f}')
if m >= 7.0:
    print('passou')
else:
    print('reprovou')