# Exemplo de importação de módulo padrão

# Importação de módulo completo
import math 

raiz_quadrada = math.sqrt(4)
print(raiz_quadrada)

# Importando funções específicas do módulo
from math import sqrt 
raiz = sqrt(25)
print(raiz)

# Exemplo de criação e utilização de módulo personalisado
import meu_modulo
mensagem = meu_modulo.saudacao("Marcela")
print(mensagem)