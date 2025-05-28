n = s = 0
m = 1
tot = 0
while True:
    n = int(input('Digite seu numero: '))
    if n == 999:
        break
    tot += 1
    s += n
    m *= n


print(f'A soma entre eles foi {s} a multiplicacao entre eles foi {m} ---{tot}')
