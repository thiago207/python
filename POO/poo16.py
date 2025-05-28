import json
dados_pessoas = []

try:
    with open('teste3---.json', 'r', encoding='utf8') as arquivo:
        dados_pessoas = json.load(arquivo)  # Carrega os dados existentes no arquivo
except FileNotFoundError:
    
    pass
while True:
    dicionario = {}
    dicionario['nome'] = (input('Nome: '))
    dicionario['idade'] = (input('Nome: '))
    dados_pessoas.append(dicionario)
    print(dados_pessoas)
    digitos = input('>  ')
    if digitos == 'sair':
        break
    
with open('teste3---.json', 'w', encoding='utf8') as arquivo:
    json.dump(dados_pessoas, arquivo, indent=2, ensure_ascii=False)

with open('teste3---.json', 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)
    print(dados)
    