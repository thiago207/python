import random

# Solicita ao usuário quantos jogos ele deseja gerar
qtd_jogos = int(input("Quantos jogos você quer gerar? "))

# Lista para armazenar os jogos gerados
jogos_gerados = []

# Gera os jogos
for c in range(qtd_jogos):
    jogo = random.sample(range(1, 61), 6)  # Gera 6 números únicos entre 1 e 60
    jogos_gerados.append(sorted(jogo))  # Ordena e adiciona o jogo à lista

# Exibe os jogos gerados
print("\nSeus palpites para a Mega-Sena:")
for i, jogo in enumerate(jogos_gerados, 1):
    print(f"Jogo {i}: {jogo}")
