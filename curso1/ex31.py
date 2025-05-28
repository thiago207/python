distancia = int(input('Distancia da sua viagem em KM: '))
p = 0.5 * distancia
l = 0.45 * distancia
if distancia <=200:
    print(f'cobrar RS0.50 por KM ate 200km, sua viagem de {distancia:.1f}Km')
    print(f'Sua viagem custara: RS{p:2f}')
else:
    print(f'Viagens acima de 200km cobra RS0.45 por KM, sua viagem tem {distancia:.1f}Km')
    print(f'sua viagem custara: RS{l:.2f}')

