lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

pessoa = {"nome": "Marcela", "idade": 35, "cidade": "Salto"}
for chave in pessoa.keys():
    print(chave)
for valor in pessoa.values():
    print(valor)
for chave, valor in pessoa.items():
    print("%s: %s" % (chave, valor))

# range() - Intervalo numérico em formato de lista
for numero in range(0,5):
    print(numero)

# len() - Quantidade de elementos
lista = list(range(0,10))
print(len(lista))

# Trazendo os resultados de uma lista com tamanho dinâmico - Trabalhando com o indice da lista
lista2 = [1, 2, 3, 4, 5, 6, 7, 8]
for indice in range(0, len(lista2)):
    print(indice)
    print(lista2[indice])

# enumerate()
lista3 = ["a", "b", "c"]
for indice, valor in enumerate(lista3):
    print("%s: %s" % (indice, valor))