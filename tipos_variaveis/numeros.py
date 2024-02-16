# Inteiro
numero_inteiro = 15
print("Inteiro:", numero_inteiro)

# Real com ponto flutuante (float)
numero_real = 3.14
print("Real com ponto flutuante:", numero_real)

# type() - verifica o tipo da variável
tipo_variavel = type(numero_inteiro)
print(tipo_variavel)

# operações aritméticas
soma = 1 + 1
subtracao = 1 - 1
multiplicacao = 2 * 3
divisao = 4 / 2 # O resultado sempre será um float
int(divisao) # Converte o float para inteiro
float(soma) # Converte o inteiro para float

# Módulo - Retorna o restante de uma divisão
modulo = 5%2

if modulo == 1:
    print("Número impar")
else:
    print("Número Par")