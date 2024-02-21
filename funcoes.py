def saudacao(nome):
    print("Olá, %s" % nome)

saudacao("Marcela")
saudacao("Rodrigo")

def quadrado(numero):
    resultado = numero ** 2
    return resultado

valor = quadrado(4)
print("A Raiz de 4 é %s" % valor)

def somatoria(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

somatoria = somatoria(4,5)
print ("4 + 5 = %s" % somatoria)