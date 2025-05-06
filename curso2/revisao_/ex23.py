# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))
def generator(n=0, max=10,ord=1):
    while True:
        if ord == 1:
            yield n
            n += 1    
            if n > max:
                return n
        else:
            while True:
                yield n
                n += ord
                if n > max:
                    return n
gen = generator(0,50,5)
for n in gen:
    print(n)
    
    


