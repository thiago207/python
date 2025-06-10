# Teoria: python Special Methods, Magic Methods ou Dunder MethodsAdd commentMore actions
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str ##
# __repr__(self) - str ####


class Ponto:
    def __init__(self, x , y, z='String'):
        self.x = x
        self.y = y
        self.z = z
        
    #def __str__(self):
        #return f'Ponto>>> str (X={self.x}, Y={self.x})'

    def __repr__(self):
        return f'Ponto [repr] (X={self.x!r}, Y={self.x!r}, Z={self.z!r})'


p1 = Ponto(100,65)
print(p1)
print(repr(p1))

#__STR__ É QUANDO QUERO RETORNAR APENAS UMA STRING
#__repr__ É QUANDO TN QUERO RETORNAR UMA STRING SO QUE ME COMUNIVANDO COM OUTROS DESENVOLVEDORES