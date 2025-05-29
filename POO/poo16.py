# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.


class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegigo'
        self.__private = 'isso é privado'

    def metodo_publico(self):
        print(self.__private)
        return 'METODO PUBLICO'

    def _metodo_protegido(self):
        return '_METODO_PROTEGIGO'
    
   
f1 = Foo()
print(f1.public)
print(f1.metodo_publico())
print()
print(f1._protected)
print(f1._metodo_protegido())
print()
#print(f1.__private)
