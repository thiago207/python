def fatorial(n, show=False):  
    fatorial = 1
    for f in range (n,0,-1):
        if show:
            print(f'{f}', end='')
            if f > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
            
        fatorial = f * fatorial

    return fatorial
    
print(fatorial(5,True))
