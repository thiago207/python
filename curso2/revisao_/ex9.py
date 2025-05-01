def criar_mut(multiplicador):
    def mutiplicar(numero):
        return numero * multiplicador
    return mutiplicar


d = criar_mut(2)
t = criar_mut(3)
q = criar_mut(4)  
print(d(2))         
print(q(2))           
print(q(2))


