#from aula2_package import modulo
from aula2_package import modulo
#from aula2_package.modulo import *
from aula2_package import modulo_b
import aula2_package
#FORMAS DIFERENTES DE IMPORTAR
print(__name__)

r = modulo.soma(1,2)
print(r)

r = modulo_b.subitracao(2,1)
print(r)

r = aula2_package.dobra(2)
print(r)

r = aula2_package.soma(5,5)
print(r)