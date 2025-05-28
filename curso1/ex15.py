km = float(input('Digite seus km pecorridos: '))
dias = int(input('Quantidades de dias que foi alugado: '))


pago = (60 * dias) + (0.15 * km)
print(f'O total a pagar é de {pago:.2f}')