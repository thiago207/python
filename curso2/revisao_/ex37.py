# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = 'aula-ex-37.txt'

#arquivo = open(caminho_arquivo, 'w+')
#arquivo.close()

#with open(caminho_arquivo, 'w+') as arquivo:
#    arquivo.write('Linha 1\n')
#    arquivo.write('Linha 2\n')
#    arquivo.write('linha 3\n')
#    arquivo.write('linha 4\n')
#    arquivo.writelines(
#        ('oi\n','ola')
#        )
#    arquivo.seek(0,0)
#    print('lendo com read')
#    print(arquivo.read())
#   print()

#arquivo.seek(0,0)
#print('lendo com readline')
# print(arquivo.readline())
#  print()
#
#    arquivo.seek(0,0)
#  print('READLINES')
#  for linha in arquivo.readlines():
#     print(linha.strip())
with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:
    arquivo.write('Atençao')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('linha 3\n')
    arquivo.write('linha 4\n')
    arquivo.writelines(
        ('oi\n','ola')
        )
    arquivo.seek(0,0)
    print(arquivo.read())