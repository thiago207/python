s = set() # set vazios
s = {1,2,3,'Thaigo'} # set com dados

s1 = set()
s1.add(1) #Adiciona um valor
s1.add(6) #Adiciona um valor
s1.add('Thiago') #Adiciona um valor

s1.update('Ola mundo!') #Add letra por letra
s1.update(('Ola mundo!', 1,2,3)) #Add elemento todo, podendo ser mais de um

s1.clear() # Limpa o set

s1.discard('Ola mundo!') # Elimina um valor

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1  |  s2 # Junta os elementos

s3 = s2 & s2 # Mostra a intersecao dos SETS

s3 = s1 - s2  # Pega o UNICOS elementos presente no s1(pega os unicos do que tiver do lado esquerdo da operaçao)

s3 = s1 ^ s3 #  Itens que nao estao em ambos!!!!